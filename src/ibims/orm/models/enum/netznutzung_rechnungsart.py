import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class NetznutzungRechnungsart(str, Enum):
    """
    Abbildung verschiedener in der INVOIC angegebenen Rechnungsarten.
    """

    HANDELSRECHNUNG = "HANDELSRECHNUNG"
    SELBSTAUSGESTELLT = "SELBSTAUSGESTELLT"
