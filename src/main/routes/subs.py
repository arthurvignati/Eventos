from flask import Blueprint, jsonify, request
subs_route_bp = Blueprint("subs_route", __name__)

from src.main.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.model.repositories.subscribers_repository import SubscribersRepository

from src.controllers.subscribers.subscribers_creator import SubscribersCreator




@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_subs():
    subscribers_creator_validator(request)
    # subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json) #Conseguimos ver aqui todos os "atributos" de um request que estão na padronização 
    print(http_request.body)
    
    subscriber_repo = SubscribersRepository()
    subscribe_creator = SubscribersCreator(subscriber_repo)
    http_response = subscribe_creator.create(http_request)


    # http_response = HttpResponse(body={ "estou": "aqui" }, status_code=201)
    return jsonify(http_response.body), http_response.status_code   