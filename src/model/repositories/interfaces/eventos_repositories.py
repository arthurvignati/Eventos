from abc import ABC, abstractmethod
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos import Eventos

#Interface --> Contrato entre a classe com o mundo exterior
# Qualquer classe que a implemente deve ter necessariamente os metodos estabelecidos na interface (aqueles que tiverem abstractmethod)
#assim é bom que podemos descrever exatamente tudo que temos na classe Eventos, e também ajuda na tipagem necessária

class EventosRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, event_name: str) -> None: pass

    @abstractmethod
    def select_event(self, event_name: str) -> Eventos: pass