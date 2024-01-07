from typing import Any, Union

from tinydb import TinyDB, Query
from tinydbstorage.storage import MemoryStorage

from s3sync.repository.interface import RepositoryInterface


class TinyDbRepository(RepositoryInterface):
    def __init__(self, db: TinyDB):
        self.db = db

    @classmethod
    def init_connection(cls) -> "TinyDbRepository":
        conn = TinyDB(storage=MemoryStorage)
        return cls(conn)

    def insert_multiple(self, table: str, data: list[dict[str, Any]]):
        self.db.table(table).insert_multiple(data)

    def count(self, table: str) -> int:
        q = Query()
        return self.db.table(table).count(q)

    def all(self, table: str) -> list[dict[str, Any]]:
        return self.db.table(table).all()

    def get(self, table: str, id: Union[int, str]) -> dict[str, Any]:
        q = Query()
        resp = self.db.search(q.id == id)
        if len(resp) == 0:
            return {}

        return resp[0]

    def drop_db(self):
        self.db.drop_tables()
