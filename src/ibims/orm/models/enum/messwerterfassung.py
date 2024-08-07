import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Messwerterfassung(str, Enum):
    """
    Specify data acquisition method
    """

    FERNAUSLESBAR = "FERNAUSLESBAR"
    MANUELL_AUSGELESENE = "MANUELL_AUSGELESENE"
