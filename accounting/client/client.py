# coding: utf-8
"""This module implement the Client class
"""

class Client:
    """Client class
    """
    def __init__(self,name, id_=None):
        self._id_ = id_
        self._name = name

    @property
    def id_(self):
        return self._id
    @id_.setter
    def id_(self, val):
        self._id = val

    @property
    def name(self):
        return self._name

