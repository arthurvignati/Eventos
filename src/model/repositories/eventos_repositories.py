from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos import Eventos
from src.model.repositories.interfaces.eventos_repositories import EventosRepositoryInterface


class EventosRepository(EventosRepositoryInterface):
    def insert(self, event_name: str) -> None:
        with DBConnectionHandler() as db: 
        #Ao criar o contexto (with ...) é criado a sessão em banco de dados e nesse momento temos acesso a tudo
        #que a classe oferece. O __enter__ já é inicializado ao chamar a classe, e o __exit__ é chamado quando
        #todas as operações dessa sessão forem finalizadas, isto é, quando nao tiver mais comando no contexto
        #with DBConnectionHandler() as db: ou cair no except
            try:
                new_event = Eventos(nome=event_name) #é criado na tabela eventos um novo evento na coluna nome
                db.session.add(new_event) # novo evento add
                db.session.commit() #salva a transação
            except Exception as exception:
                db.session.rollback() #volta ao banco no estado anterior de ter feito qualquer coisa, ou seja, antes da sessão
                raise exception
            

    def select_event(self, event_name: str) -> Eventos: #vai retornar um elemento de "Eventos"
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session
                    .query(Eventos)
                    .filter(Eventos.nome == event_name)
                    .one_or_none()
                )
                return data
            except Exception as exception:
                raise exception