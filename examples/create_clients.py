from accounting import utils
from accounting.client import client

clients = []
clients.append(client.Client('client1'))
clients.append(client.Client('client2'))

db_filename = 'client_test_database.pickle'
# save client list
print(' '.join([client.name for client in clients]))
utils.save_clients(clients,  db_filename)
# import client list
loaded_clients = utils.load_clients(db_filename)
print(loaded_clients)
print(' '.join([client.name for client in loaded_clients]))
