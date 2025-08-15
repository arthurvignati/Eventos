from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos

class SubscribersRepository():
    def insert(self, subscribers_info: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Inscritos(
                    nome=subscribers_info.get('name'),
                    email=subscribers_info.get('email'),
                    link=subscribers_info.get('link'),
                    evento_id=subscribers_info.get('evento_id'),
                )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

    def select_subscriber(self, email: str, evento_id: int) -> Inscritos: #retorna necessáriamente um elemento de inscritos
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(Inscritos.email == email, Inscritos.evento_id == evento_id)
                .one_or_none()
            )
            return data
            
