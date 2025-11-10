from src.model.repositories.interfaces.eventos_repositories import EventosRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
class EventsCreator:
    def __init__(self, events_repo: EventosRepositoryInterface):
        self.__events_repo = events_repo
        #self.__events_repo. Utilizar a interface nesse caso é muito útil pois conseguimos ver todos os métodos importados, utilizando . por exemplo

    def create(self, http_request: HttpRequest ) -> HttpResponse:
        events_info = http_request.body["data"]
        event_name = events_info["name"]

        self.__check_event(event_name)
        self.__insert_event(event_name)

        return self.__format_response(event_name)

    def __check_event(self, event_name: str) -> None:
        response = self.__events_repo.select_event(event_name)
        if response: raise Exception("Event Already Exists!")

    def __insert_event(self, event_name: str) -> None:
        self.__events_repo.insert(event_name)


    def __format_response(self, event_name: str) -> HttpResponse:
        return HttpResponse(
            body = {
                "data": {
                    "Type": "Event",
                     "count": 1,
                     "attributes": {
                        "event_name": event_name
                     }
                }
            },
            status_code=201
        )


