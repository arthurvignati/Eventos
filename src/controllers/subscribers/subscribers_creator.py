from src.model.repositories.subscribers_repository import SubscribersRepository
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class SubscribersCreator:

    def __init__(self, subscribers_repo: SubscribersRepository):
        self.__subscribers_repo = SubscribersRepository

    def create(self, http_request: HttpRequest):
        subscribers_info = http_request.body["data"]  

        subscriber_email = subscribers_info['email']
        subscribers_evento_id = subscribers_info['evento_id']

        self.__check_subscriber(subscriber_email, subscribers_evento_id)
        self.__inser_subscriber(subscribers_info)
        return self.__format_response(subscribers_info)

    def __check_subscriber(self, subscriber_email: str, subscribers_evento_id: int) -> None:
        response = self.__subscribers_repo.select_subscriber(subscriber_email, subscribers_evento_id)
        if response: raise Exception('Subscriber already Existis')

    def __inser_subscriber(self, subscriber_info: dict) -> None:
        self.__subscribers_repo.insert(subscriber_info)


    def __format_response(self, subscriber_info: dict) -> HttpResponse:
        return HttpResponse(
            body = {
                "data": {
                    "Type": "Subscriber",
                     "count": 1,
                     "attributes": {
                        "event_name": subscriber_info
                     }
                }
            },
            status_code=201
        )


