#TESTES DE INTEGRAÇÃO com PYTEST -- INTEGRA NOSSO PROJETO COM UM ELEMENTO TERCEIRO
#pytest -s -v F:\Users\Arthur\projects\eventos\Eventos\src\model\repositories\eventos_repositories_test.py
#se der passed é porque deu certo, e verifica no banco de dados se foi atualizado, ou seja, se subiu o nome do evento.

import pytest
from src.model.repositories.subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB") #Deixa como freeze para fazer outros testes (ja que esse faz um insert)
def test_insert_subscribers():
    subscriber_info = {
        "name": "meuNome",
        "email": "email@email.com",
        "evento_id": 2
    }    
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)
@pytest.mark.skip("Select in DB") 
def test_select_subscriber():
    email = "email@email.com"
    evento_id = 2
    subs_repo = SubscribersRepository() 
    resp  = subs_repo.select_subscriber(email, evento_id)
    print(f'resp --> {resp} || email --> {resp.email} || email --> {resp.nome}')
