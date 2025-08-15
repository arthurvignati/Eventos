from abc import ABC, abstractmethod
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos

class SubscribersRepositoryInterface(ABC):
    #deixar somente as assinaturas
    @abstractmethod
    def insert(self, subscribers_info: dict) -> None: pass

    @abstractmethod
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos: pass
