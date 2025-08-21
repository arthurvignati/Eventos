#validação do body
from cerberus import Validator

def events_creator_validator(request: any):
    Validator({
        "data":{
            "type": "dict"
        }
    })