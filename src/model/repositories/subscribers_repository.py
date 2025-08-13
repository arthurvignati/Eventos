from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos

class SubscribersRepository():
    def insert(self, subscribers_info: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Inscritos(
                    nome=subscribers_info.get('name'),
                    email=subscribers_info.get('email'),
                    link=subscribers_info.get('email'),
                    evento_id=subscribers_info.get('evento_id'),
                )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

        