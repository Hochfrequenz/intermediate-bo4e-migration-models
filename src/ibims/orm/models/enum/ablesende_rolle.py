import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class AblesendeRolle(str, Enum):
    """
    Eine (Markt)Rolle, die Verbräuche abliest.
    """

    VNB = "VNB"
    ENDKUNDE = "ENDKUNDE"
    VORIGER_LIEFERANT = "VORIGER_LIEFERANT"
    MSB = "MSB"
    SYSTEM = "SYSTEM"
