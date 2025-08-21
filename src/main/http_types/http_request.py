
#Criação de um elemento padrão para request (nesse exemplo, só buscamos o body e os parametros, poderiamos inserir o header por ex)

#padronização para sempre ter um body e um param
class HttpRequest:
    def __init__(self, body: dict = None, param: dict = None) -> None:
        self.body = body
        self.param = param