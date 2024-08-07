import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Tarifregionskriterium(str, Enum):
    """
    Mit diesen Kriterien können regionale Bereiche definiert werden.
    """

    NETZ_NUMMER = "NETZ_NUMMER"
    POSTLEITZAHL = "POSTLEITZAHL"
    ORT = "ORT"
    GRUNDVERSORGER_NUMMER = "GRUNDVERSORGER_NUMMER"
    REGION = "REGION"
