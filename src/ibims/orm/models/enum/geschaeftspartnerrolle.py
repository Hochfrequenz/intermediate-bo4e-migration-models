import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Geschaeftspartnerrolle(str, Enum):
    """
    Diese Rollen kann ein Geschäftspartner einnehmen.
    """

    LIEFERANT = "LIEFERANT"
    DIENSTLEISTER = "DIENSTLEISTER"
    KUNDE = "KUNDE"
    INTERESSENT = "INTERESSENT"
    MARKTPARTNER = "MARKTPARTNER"
