# coding: utf-8


# === #__LABELS__ = [
# === #    u'Numéro du document',
# === #    u'Date',
# === #    u'Code client',
# === #    u'Civilité',
# === #    u'Nom du client',
# === #    u'Adresse 1 (facturation)',
# === #    u'Adresse 2 (facturation)',
# === #    u'Adresse 3 (facturation)',
# === #    u'Adresse 4 (facturation)',
# === #    u'Code postal (facturation)',
# === #    u'Ville (facturation)',
# === #    u'Département (facturation)',
# === #    u'Code Pays (facturation)',
# === #    u'Nom (contact) (facturation)',
# === #    u'Prénom (facturation)',
# === #    u'Téléphone fixe (facturation)',
# === #    u'Téléphone portable (facturation)',
# === #    u'Fax (facturation)',
# === #    u'E-mail (facturation)',
# === #    u'Nom (adresse) (livraison)',
# === #    u'Civilité (adresse) (livraison)',
# === #    u'Adresse 1 (livraison)',
# === #    u'Adresse 2 (livraison)',
# === #    u'Adresse 3 (livraison)',
# === #    u'Adresse 4 (livraison)',
# === #    u'Code postal (livraison)',
# === #    u'Ville (livraison)',
# === #    u'Département (livraison)',
# === #    u'Code Pays (livraison)',
# === #    u'Nom (contact) (livraison)',
# === #    u'Prénom (livraison)',
# === #    u'Téléphone fixe (livraison)',
# === #    u'Téléphone portable (livraison)',
# === #    u'Fax (livraison)',
# === #    u'E-mail (livraison)',
# === #    u'Territorialité',
# === #    u'Numéro de TVA intracommunautaire',
# === #    u'% remise',
# === #    u'Montant de la remise',
# === #    u'% escompte',
# === #    u'Montant de l\'escompte',
# === #    u'Code frais de port',
# === #    u'Frais de port HT',
# === #    u'Taux de TVA port',
# === #    u'Code TVA port',
# === #    u'Port non soumis à escompte',
# === #    u'Total Brut HT',
# === #    u'Total TTC',
# === #    u'Notes',
# === #    u'Notes en texte brut',
# === #    u'Référence',
# === #    u'Code commercial/collaborateur',
# === #    u'Code mode de règlement',
# === #    u'Code ligne de document',
# === #    u'Code article',
# === #    u'Description',
# === #    u'Description commerciale en clair',
# === #    u'Date de livraison',
# === #    u'Quantité',
# === #    u'Taux de TVA',
# === #    u'Code TVA',
# === #    u'Type de ligne',
# === #    u'PV HT',
# === #    u'PV TTC',
# === #    u'% remise unitaire cumulé',
# === #    u'Montant de remise unitaire HT cumulé',
# === #    u'Montant Net HT',
# === #    u'Montant Net TTC',
# === #    u'Code commercial/collaborateur',
# === #    u'Codes des lignes de commandes',
# === #    u'Codes des commandes',
# === #    u'Quantités à livrer',
# === #    ]
# === #
# === #def parse_line(row):
# === #    global __LABELS__
# === #    # == convert row of cell into dict of values
# === #    line = dict(zip(__LABELS__, (cell.value for cell in row)))
# === #    return line

class InvoiceLine(object):
    """
    """
    def __init__(self, price, label):
        self.price = price
        self.label = label

class Invoice(object):
    """
    """
    def __init__(self, id_, date, client):
        self._id = id_
        self._date = date
        self._client = client
        self._items = []

    @property
    def id_(self):
        return self._id
    @id_.setter
    def id_(self, val):
        self._id = val

    @property
    def date(self):
        return self._date

    @property
    def client(self):
        return self._client

    def add_line(self, price, label):
        self._items.append(InvoiceLine(price, label))

    def __eq__(self, other):
        equal = False
        if isinstance(other, self.__class__):
            equal = self._id == other._id
            equal = self._date == other._date
            equal &= self._client == other._client
        return equal

    def __ne__(self, other):
        return not self.__eq__(other)

    # == #def __add__(self, other):
    # == #    result = None
    # == #    if isinstance(other, self.__class__):
    # == #        # == create result as copy of current instance
    # == #        result = Invoice(self._date, self._client)
    # == #        # == copy lines from current instance
    # == #        result._items = self._items.copy()
    # == #        # == add lines from other instance
    # == #        result._items += other._items
    # == #    else:
    # == #        raise(TypeError)
    # == #    return result

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self._items += other._items
            # ==  concatenate rows
            self._rows += other._rows
        else:
            raise(TypeError)
        return self

