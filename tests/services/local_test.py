import io
import os
import unittest
import shutil

from s3sync.schemas import LocalConfig
from s3sync.services import LocalServices


class TestLocalServices(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory for testing
        # Set up a temporary directory for testing
        self.temp_dir = "temp_test_directory"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

        # Create a LocalConfig instance for testing
        self.local_config = LocalConfig(path=self.temp_dir)

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.temp_dir)

    def test_init_connection(self):
        # Test the initialization of LocalServices using init_connection method
        local_services = LocalServices.init_connection(self.local_config)
        self.assertIsInstance(local_services, LocalServices)
        self.assertEqual(local_services.config.path, self.temp_dir)

    def test_scan_file(self):
        # Test the scan_file method
        local_services = LocalServices(self.local_config)
        test_file_path = os.path.join(self.temp_dir, "test_file.txt")
        open(test_file_path, "w").close()
        result = local_services.scan_file(self.temp_dir)
        # Update the assertion based on the format of "Key"
        self.assertTrue(
            any(os.path.basename(item["Key"]) == "test_file.txt" for item in result)
        )

    def test_get_list_files(self):
        # Test the get_list_files method
        local_services = LocalServices(self.local_config)
        test_file_path = os.path.join(self.temp_dir, "test_file.txt")
        open(test_file_path, "w").close()
        result = local_services.get_list_files()
        # Update the assertion based on the format of "Key"
        self.assertTrue(any(item["Key"].endswith("test_file.txt") for item in result))

    def test_get_detail_file(self):
        # Test the get_detail_file method
        local_services = LocalServices(self.local_config)
        test_file_path = os.path.join(self.temp_dir, "test_file.txt")
        with open(test_file_path, "w") as file:
            file.write("Test content")
        result = local_services.get_detail_file("test_file.txt")
        self.assertEqual(result["Key"], "test_file.txt")
        self.assertIsInstance(result["Body"], io.BytesIO)
        self.assertEqual(result["Body"].read(), b"Test content")

    def test_upload_file(self):
        # Test the upload_file method
        local_services = LocalServices(self.local_config)
        test_file_content = b"Test content"
        test_file_name = "test_file.txt"
        local_services.upload_file(io.BytesIO(test_file_content), test_file_name)
        test_file_path = os.path.join(self.temp_dir, test_file_name)
        with open(test_file_path, "rb") as file:
            uploaded_content = file.read()
        self.assertEqual(uploaded_content, test_file_content)

    def test_download_file_not_implemented(self):
        # Test that download_file raises NotImplementedError
        local_services = LocalServices(self.local_config)
        with self.assertRaises(NotImplementedError):
            local_services.download_file("path", "file.txt")


if __name__ == "__main__":
    unittest.main()
