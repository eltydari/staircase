import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import tempfile
import os

ACCOUNT_ID = "362764577362"
DATASET_ID = "8b37060b-d5ea-4950-b5a0-22e9ed3d2cd3"
INVOCATION_FILENAME = "logs/invocations.csv"


def lambda_handler(event, context):
    log_new_invocation()
    report_invocation()
    return "helloworld"


def log_new_invocation():
    ifile = InvocationFile()
    ifile.log_invocation()


def report_invocation():
    quicksight = boto3.client('quicksight')
    try:
        quicksight.create_dashboard(
            AwsAccountId = ACCOUNT_ID,
            DashboardId = "staircase-demo",
            Name = "Staircase Demo",
            SourceEntity = {
                "SourceTemplate": {
                    "Arn": "arn:aws:quicksight:us-east-2:%s:template/invokation-template" % ACCOUNT_ID,
                    "DataSetReferences": [
                        {
                            "DataSetPlaceholder": "invocations",
                            "DataSetArn": "arn:aws:quicksight:us-east-2:%s:dataset/%s" % (ACCOUNT_ID, DATASET_ID)
                        }
                    ]
                }
            },
            Permissions = [
                {
                    "Principal": "arn:aws:quicksight:us-east-2:362764577362:namespace/default",
                    "Actions": [
                        "quicksight:DescribeDashboard",
                        "quicksight:ListDashboardVersions",
                        "quicksight:QueryDashboard"
                    ]
                }
            ]
        )
    except quicksight.exceptions.ResourceExistsException:
        pass  # move on if already created
    quicksight.create_ingestion(
        DataSetId = DATASET_ID,
        IngestionId = datetime.utcnow().strftime("%Y%m%d-%H%M%S-%f"),
        AwsAccountId = ACCOUNT_ID
    )


class InvocationFile(object):
    def __init__(self):
        self._bucket = boto3.resource('s3').Bucket("staircase-demo")
        _, self._filename = tempfile.mkstemp()
        try:
            with open(self._filename, 'wb') as f:
                self._bucket.download_fileobj(INVOCATION_FILENAME, f)
        except ClientError:
            with open(self._filename, 'a') as f:
                f.write("time_invoked\n")

    def __del__(self):
        try:
            os.remove(self._filename)
        finally:
            return

    def log_invocation(self):
        with open(self._filename, 'a') as f:
            f.write(datetime.utcnow().isoformat() + "\n")
        self._bucket.upload_file(self._filename, INVOCATION_FILENAME)
