import pytest


from accounting import utils
from accounting.client import client

db_filename_ok = 'client_test_database_ok.pickle'
db_filename_fail = 'client_test_database_fail.pickle'

def test_save_clients_ok():
    clients = []
    clients.append(client.Client('client1'))
    clients.append(client.Client('client2'))
    utils.save_clients(clients,  db_filename_ok)

def test_save_clients_fail():
    clients = []
    clients.append(client.Client('client1'))
    clients.append(client.Client('client2'))
    clients.append(client.Client('client2'))
    with pytest.raises(ValueError):
        utils.save_clients(clients,  db_filename_fail)

def test_load_clients():
    clients = utils.load_clients(db_filename_ok)

def test_load_client_from_db():
    clients = utils.load_clients(db_filename_ok)
    client = utils.get_client_from_db(clients, 'client1')

def test_load_client_from_file():
    client = utils.get_client_from_file(db_filename_ok, 'client1')
