# coding: utf-8
"""Provides a set of utility functions
"""
import os
import pickle

def check_client_list(clients):
    """Check that a client list is valid
    """
    seen = []
    has_doublons = any(client.name in seen or seen.append(client.name) for client in clients)
    return not has_doublons

def save_clients(clients, file_):
    """Save a list of clients

    Parameters
    ----------
    clients: iterable
        list of clients
    file_: str
        path of file where database should be saved

    Raises
    ------
    ValueError
        If the client list has doublons
    """
    if check_client_list(clients):
        with open(file_, 'wb') as f:
            pickle.dump(clients, f)
    else:
        raise ValueError("Clients should all be unique!")

def load_clients(file_):
    """Load a list of clients, return a dict

    Parameters
    ----------
    clients: iterable
        list of clients
    file_: str
        path of file where database should be saved

    Returns
    -------
    list
        List of :obj:accounting.client.client.Client instances
    """
    with open(file_, 'rb') as f:
        clients = pickle.load(f)
    return clients

def get_client_from_db(clients, name):
    """Get a given client from a list of clients

    Parameters
    ----------
    name: str
        name of the client
    clients: iterable
        list of clients

    Raises
    ------
    KeyError
        If the client is not in the database
    """
    out = next((client for client in clients if client.name == name), None)
    if out is None:
        raise KeyError("Client {} could not be found in database.")


def get_client_from_file(file_, name):
    """Get a given client from a clients file

    Parameters
    ----------
    clients: iterable
        list of clients
    file_: str
        path of database file

    Raises
    ------
    KeyError
        If the client is not in the database
    """
    clients = load_clients(file_)
    return get_client_from_db(clients, name)

def invoice_fname(invoice_id):
    return 'invoice_{}.pickle'.format(invoice_id)


def save_invoice(invoice, dir_=None):
    """Save an invoice

    Parameters
    ----------
    invoice: :class:invoice
        invoice
    dir_: str, optional
        path of directory where invoice should be saved
    """
    fname = invoice_fname(invoice.id_)
    fpath = fname if dir_ is None else os.path.join(dir_, fname)
    with open(fpath, 'wb') as f:
        pickle.dump(invoice, f)

def load_invoice(invoice_id, dir_=None):
    """Load an invoice from its id

    Parameters
    ----------
    invoice_id: str
        invoice id
    dir_: str, optional
        path of directory where invoice is stored
    """
    fname = invoice_fname(invoice_id)
    fpath = fname if dir_ is None else os.path.join(dir_, fname)
    with open(fpath, 'rb') as f:
        invoice = pickle.load(f)
    return invoice

def next_client_id(curr_id=None):
    curr_ind = 0
    if curr_id is not None:
        curr_ind = int(curr_id.split('CL')[-1])
    out = 'CL{0:04d}'.format(curr_ind+1)
    return out

def append_client_to_db(clients, new_client):
    try:
        new_client.id_ = next_client_id(curr_id=clients[-1].id_)
    except IndexError:
        # database was empty
        new_client.id_ = next_client_id()
    clients.append(new_client)
    print(clients)
