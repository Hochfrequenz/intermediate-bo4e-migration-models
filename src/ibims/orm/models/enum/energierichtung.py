import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Energierichtung(str, Enum):
    """
    Spezifiziert die Energierichtung einer Markt- und/oder Messlokation
    """

    AUSSP = "AUSSP"
    EINSP = "EINSP"
