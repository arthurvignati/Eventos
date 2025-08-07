#TESTES DE INTEGRAÇÃO com PYTEST -- INTEGRA NOSSO PROJETO COM UM ELEMENTO TERCEIRO
#pytest -s -v F:\Users\Arthur\projects\eventos\Eventos\src\model\repositories\eventos_repositories_test.py
#se der passed é porque deu certo, e verifica no banco de dados se foi atualizado, ou seja, se subiu o nome do evento.

import pytest
from src.model.repositories.eventos_repositories import EventosRepository

@pytest.mark.skip("Insert in DB") #Deixa como freeze para fazer outros testes (ja que esse faz um insert)
def test_insert_eventos():
    event_name = "eventoTeste2"
    event_repo = EventosRepository() 
    event_repo.insert(event_name)

@pytest.mark.skip("Select in DB") #Deixa como freeze para fazer outros testes
def test_select_event():
    event_name = "eventoTeste2"
    event_repo = EventosRepository() 
    event = event_repo.select_event(event_name)
    # print(f'event --> {event} || name --> {event.nome}')
