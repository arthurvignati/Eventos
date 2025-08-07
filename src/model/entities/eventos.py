from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer #para declarar as colunas


class Eventos(Base): #colocar a base declarativa nos parametros para declarar que nós temos essa tabela
    __tablename__ = "Eventos" #minha classe Eventos esta relacionada com minha tabela de Eventos do banco

    #declarar as colunas
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    
