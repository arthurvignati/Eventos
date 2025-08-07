from src.model.configs.base import Base
from sqlalchemy import String, Column, Integer, ForeignKey


class EventosLink(Base):
    __tablename__ = "Eventos_link"
    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey("Evento.id"), nullable=False)
    inscrito_id = Column(Integer, ForeignKey("Inscritos.id"), nullable=False)
    text = Column(String)


