import datetime

from accounting import utils
from accounting.client import client
from accounting.invoicing import invoice

db_filename = 'client_test_database.pickle'

client = utils.get_client_from_file(db_filename, 'client1')
date = datetime.datetime.today()
id_ = '2019_001'

invoice = invoice.Invoice(id_, date, client)
utils.save_invoice(invoice)
