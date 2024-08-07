import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Kontaktart(str, Enum):
    """
    Gibt an, auf welchem Weg die Person oder der Geschäftspartner kontaktiert werden kann.
    """

    POSTWEG = "POSTWEG"
    TELEFON = "TELEFON"
    FAX = "FAX"
    E_MAIL = "E_MAIL"
    SMS = "SMS"
