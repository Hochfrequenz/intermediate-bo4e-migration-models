import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Steuerkennzeichen(str, Enum):
    """
    Zur Kennzeichnung verschiedener Steuersätze und Verfahren.
    """

    UST_0 = "UST_0"
    UST_19 = "UST_19"
    UST_16 = "UST_16"
    UST_7 = "UST_7"
    VST_0 = "VST_0"
    VST_19 = "VST_19"
    VST_16 = "VST_16"
    VST_7 = "VST_7"
    RCV = "RCV"
