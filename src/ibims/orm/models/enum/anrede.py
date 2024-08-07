import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Anrede(str, Enum):
    """
    Übersicht möglicher Anreden, z.B. eines Geschäftspartners.
    """

    HERR = "HERR"
    FRAU = "FRAU"
    EHELEUTE = "EHELEUTE"
    FIRMA = "FIRMA"
    FAMILIE = "FAMILIE"
    ERBENGEMEINSCHAFT = "ERBENGEMEINSCHAFT"
    GRUNDSTUECKSGEMEINSCHAFT = "GRUNDSTUECKSGEMEINSCHAFT"
