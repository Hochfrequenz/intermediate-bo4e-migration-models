import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class MesstechnischeEinordnung(str, Enum):
    """
    An enum for the messtechnische Einordnung
    """

    IMS = "IMS"
    KME_MME = "KME_MME"
    KEINE_MESSUNG = "KEINE_MESSUNG"
