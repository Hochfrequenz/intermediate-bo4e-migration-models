import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class ZaehlertypSpezifikation(str, Enum):
    """
    Bei diesem Enum handelt es sich um die Abbildung von besonderen Zählertyp-Spezifikationen der Sparten Strom und Gas.
    """

    EDL40 = "EDL40"
    EDL21 = "EDL21"
    SONSTIGER_EHZ = "SONSTIGER_EHZ"
    MME_STANDARD = "MME_STANDARD"
    MME_MEDA = "MME_MEDA"
