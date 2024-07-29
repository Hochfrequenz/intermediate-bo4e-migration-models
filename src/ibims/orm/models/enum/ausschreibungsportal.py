import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Ausschreibungsportal(str, Enum):
    """
    Aufzählung der unterstützten Ausschreibungsportale.
    """

    ENPORTAL = "ENPORTAL"
    ENERGIE_AGENTUR = "ENERGIE_AGENTUR"
    BMWI = "BMWI"
    ENERGIE_HANDELSPLATZ = "ENERGIE_HANDELSPLATZ"
    BUND = "BUND"
    VERA_ONLINE = "VERA_ONLINE"
    ISPEX = "ISPEX"
    ENERGIEMARKTPLATZ = "ENERGIEMARKTPLATZ"
    EVERGABE = "EVERGABE"
    DTAD = "DTAD"
