from flask import Blueprint, jsonify, request
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.validators.events_creator_validator import events_creator_validator

#criar um agregador de rotas
#todas as rotas relacionadas a eventos estarão aqui
#EX: para criar uma rota /event, basta chamar o agregador @event_route_bp.route("/event", method=["POST"])
event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    events_creator_validator(request)
    http_request = HttpRequest(body=request.json) #Conseguimos ver aqui todos os "atributos" de um request que estão na padronização 
    print(http_request.body)

    http_response = HttpResponse(body={ "estou": "aqui" }, status_code=201)
    return jsonify(http_response.body), http_response.status_code   