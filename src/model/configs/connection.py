#Classe para organizar conexão com o banco
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler: #gerente de conexão
    def __init__(self): 
        self.__connection_string = "sqlite:///schema.db" #mostra para o sqlite onde o banco de dados está
        self.__engine = self.__create_database_engine() #toda vez que a classe DBConnectionHandler foi chamada a conexão é feita
        self.session = None #começar a sessão zerado

    #método de mecanismo de conexão
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    #criar uma sessão para o banco de dados (abre uma sessão, dentro dela faz uma busca, inserção, etc, e depois fecha a sessão)
    #a interação sobre o banco de dados é feita através de sessões
    #espaço permitido para fazer qualquer tipo de alteração/interação dentro do banco

    def __enter__(self):  #__enter__ é utilizado como comando principal para rodar algo. é sempre o primeiro ato a ser executado
        session_make = sessionmaker(bind=self.__engine) #cria a sessão com o mecanismo de sessão
        self.session = session_make() #na hora que entrar (que vai para a funcao enter), a session da instancia é alterada
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):#exit é utilizado como comando final.o último ato a ser executado
        self.session.close() #fechar a sessão
        

