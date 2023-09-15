"""
This module contains hints for contracts or customers
"""
from datetime import datetime

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt

from ibims.enum import HinweisThema


class Hinweis(Geschaeftsobjekt):
    """
    Contains specific hints for the handling of contracts and customers.
    Hints are meant to be read and written by agents or customer service employees.
    """

    erstellungsdatum: datetime

    thema: HinweisThema | str

    nachricht: str
