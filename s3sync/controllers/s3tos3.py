from s3sync.controllers.interface import SyncInterface
from s3sync.repository.interface import RepositoryInterface
from s3sync.services.interface import BucketInterface


class S3ToS3Provider(SyncInterface):
    def __init__(
        self,
        db: RepositoryInterface,
        source: BucketInterface,
        target: BucketInterface,
    ):
        self.db = db
        self.source = source
        self.target = target

    @classmethod
    def init_connection(
        cls,
        db: RepositoryInterface,
        source: BucketInterface,
        target: BucketInterface,
    ):
        return cls(db, source, target)

    def sync_bucket(self):
        print("masuk")
