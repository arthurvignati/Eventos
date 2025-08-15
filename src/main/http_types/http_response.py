#Criação de um elemento padrão para respostas HTTP

#padronização para sempre ter um body e um status code
class HttpResponse:
    def __init__(self, body: dict, status_code: int) -> None:
        self.body = body
        self.status_code = status_code
