import os.path
from typing import Any

from s3sync.schemas import LocalConfig
from s3sync.services.interface import BucketInterface


class LocalServices(BucketInterface):
    def __init__(self, config: LocalConfig):
        self.config = config

    @classmethod
    def init_connection(cls, config: LocalConfig) -> "LocalServices":
        return cls(config)

    def scan_file(self, path: str) -> list[dict[str, Any]]:
        ret = []
        for root_dir, folders, files in os.walk(path):
            for folder in folders:
                p = os.path.join(root_dir, folder)
                ret += self.scan_file(p)
                continue

            for file in files:
                path_file = os.path.join(root_dir, file)
                ret.append({"key": path_file})

        return ret

    def get_list_files(self) -> list[dict[str, Any]]:
        files = self.scan_file(self.config.path)
        return files

    def get_detail_file(self, file_name: str) -> dict[str, Any]:
        full_path = os.path.join(self.config.path, file_name)
        resp = {"key": full_path}
        with open(full_path, "rb") as file:
            resp["Body"] = file.read()

        return resp

    def upload_file(self, body: bytes, file_name: str) -> None:
        full_path = os.path.join(self.config.path, file_name)
        with open(full_path, "wb") as file:
            file.write(body)

        return None

    def download_file(self, path: str, file_name: str) -> None:
        raise NotImplementedError
