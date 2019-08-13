import accounting.invoicing.invoice as invoicing
import datetime

def test_create_invoice():
    new_invoice = invoicing.Invoice('2019-001', datetime.datetime.today(), 'CL000')
