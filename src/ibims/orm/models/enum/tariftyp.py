import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Tariftyp(str, Enum):
    """
    Zur Differenzierung von Grund/Ersatzversorgungstarifen und sonstigen angebotenen Tarifen.
    """

    GRUND_ERSATZVERSORGUNG = "GRUND_ERSATZVERSORGUNG"
    GRUNDVERSORGUNG = "GRUNDVERSORGUNG"
    ERSATZVERSORGUNG = "ERSATZVERSORGUNG"
    SONDERTARIF = "SONDERTARIF"
