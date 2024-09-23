import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Angebotsstatus(str, Enum):
    """
    Gibt den Status eines Angebotes an.
    """

    KONZEPTION = "KONZEPTION"
    UNVERBINDLICH = "UNVERBINDLICH"
    VERBINDLICH = "VERBINDLICH"
    BEAUFTRAGT = "BEAUFTRAGT"
    UNGUELTIG = "UNGUELTIG"
    ABGELEHNT = "ABGELEHNT"
    NACHGEFASST = "NACHGEFASST"
    AUSSTEHEND = "AUSSTEHEND"
    ERLEDIGT = "ERLEDIGT"
