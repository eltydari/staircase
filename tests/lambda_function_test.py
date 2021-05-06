from unittest import TestCase
from unittest.mock import patch, MagicMock
import src.lambda_function as module

class ModuleTests(TestCase):

    @patch.object(module, "log_new_invocation")
    def test_lambda_handler(self, invocation_mock):
        response = module.lambda_handler(MagicMock(), MagicMock())
        self.assertEqual("helloworld", response)
        self.assertEqual(1, invocation_mock.call_count)

    @patch("builtins.open")
    @patch("tempfile.mkstemp", return_value=("test", "test"))
    @patch("boto3.resource")
    def test_log_new_invocation(self, resource_mock, mkstemp_mock, _open_mock):
        module.log_new_invocation()
        s3_mock = resource_mock().Bucket()
        self.assertEqual(1, s3_mock.download_fileobj.call_count)
        self.assertEqual(1, s3_mock.upload_file.call_count)
        self.assertEqual(1, mkstemp_mock.call_count)
