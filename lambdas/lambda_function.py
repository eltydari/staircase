import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import tempfile
import os

BUCKET_LOCATION = "staircase-demo"
INVOCATION_FILENAME = "logs/invocations.csv"


def lambda_handler(event, context):
    log_new_invocation()
    return "helloworld"


def log_new_invocation():
    ifile = InvocationFile()
    ifile.log_invocation()


class InvocationFile(object):
    def __init__(self):
        self._bucket = boto3.resource('s3').Bucket(BUCKET_LOCATION)
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
