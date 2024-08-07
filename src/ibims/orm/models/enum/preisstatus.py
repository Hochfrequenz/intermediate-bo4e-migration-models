import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Preisstatus(str, Enum):
    """
    Statusinformation für Preise
    """

    VORLAEUFIG = "VORLAEUFIG"
    ENDGUELTIG = "ENDGUELTIG"
