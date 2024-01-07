from abc import ABC, abstractmethod
from typing import Any, Union


class RepositoryInterface(ABC):
    @abstractmethod
    def insert_multiple(self, table: str, data: list[dict[str, Any]]):
        raise NotImplementedError

    @abstractmethod
    def count(
        self,
        table: str,
    ) -> int:
        raise NotImplementedError

    @abstractmethod
    def all(
        self,
        table: str,
    ) -> list[dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def get(self, table: str, id: Union[int, str]) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def drop_db(self):
        raise NotImplementedError
