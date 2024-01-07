import unittest
from pydantic import ValidationError
from s3sync.schemas import S3Config


class TestS3Config(unittest.TestCase):
    def test_valid_s3_config(self):
        # Test case with a valid S3Config instance
        s3_config_data = {
            "bucket_name": "my_bucket",
            "region_name": "us-east-1",
            "access_key_id": "my_access_key",
            "secret_access_key": "my_secret_key",
        }
        s3_config_instance = S3Config(**s3_config_data)
        self.assertEqual(s3_config_instance.bucket_name, "my_bucket")
        self.assertEqual(s3_config_instance.region_name, "us-east-1")
        self.assertEqual(s3_config_instance.access_key_id, "my_access_key")
        self.assertEqual(s3_config_instance.secret_access_key, "my_secret_key")

    def test_invalid_empty_fields(self):
        # Test case with empty fields, expecting a ValidationError
        with self.assertRaises(ValidationError):
            S3Config(
                bucket_name="",
                region_name="",
                access_key_id="",
                secret_access_key="",
            )

    def test_invalid_short_fields(self):
        # Test case with fields that are too short, expecting a ValidationError
        with self.assertRaises(ValidationError):
            S3Config(
                bucket_name="b",
                region_name="r",
                access_key_id="a",
                secret_access_key="s",
            )

    def test_invalid_missing_fields(self):
        # Test case with missing fields, expecting a ValidationError
        with self.assertRaises(ValidationError):
            S3Config()


if __name__ == "__main__":
    unittest.main()
