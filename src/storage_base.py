from abc import ABC, abstractmethod


class StorageBase(ABC):

    @abstractmethod
    def add(self, vacancy):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, url):
        pass
