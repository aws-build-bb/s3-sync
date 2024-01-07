import unittest
from pydantic import ValidationError
from s3sync.schemas import LocalConfig


class TestLocalConfig(unittest.TestCase):
    def test_valid_local_config(self):
        # Test case with a valid LocalConfig instance
        local_config_data = {"path": "/valid/path"}
        local_config_instance = LocalConfig(**local_config_data)
        self.assertEqual(local_config_instance.path, "/valid/path")

    def test_invalid_empty_path(self):
        # Test case with an empty path, which should raise a ValidationError
        with self.assertRaises(ValidationError):
            LocalConfig(path="")

    def test_invalid_short_path(self):
        # Test case with a path that is too short, which should raise a ValidationError
        with self.assertRaises(ValidationError):
            LocalConfig(path="a")

    def test_invalid_missing_path(self):
        # Test case with missing 'path' field, which should raise a ValidationError
        with self.assertRaises(ValidationError):
            LocalConfig()


if __name__ == "__main__":
    unittest.main()
