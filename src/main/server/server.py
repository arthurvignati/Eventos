from flask import Flask
from src.main.routes.event import event_route_bp
from src.main.routes.subs import subs_route_bp
app = Flask(__name__) #criar servidor http Flask

app.register_blueprint(event_route_bp) #registrar o agregador de rotas do evento no servidor. 
#                                       Qualquer rota que seja criada no agregador, será cadastrada no servidor



app.register_blueprint(subs_route_bp)