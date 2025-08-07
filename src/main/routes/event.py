from flask import Blueprint, jsonify

#criar um agregador de rotas
#todas as rotas relacionadas a eventos estarão aqui
#EX: para criar uma rota /event, basta chamar o agregador @event_route_bp.route("/event", method=["POST"])
event_route_bp = Blueprint("event_route", __name__)


@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    return jsonify({ "estou": "aqui" }), 201