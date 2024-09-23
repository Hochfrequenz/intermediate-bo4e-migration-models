import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Tarifzeit(str, Enum):
    """
    Zur Kennzeichnung verschiedener Tarifzeiten, beispielsweise zur Bepreisung oder zur Verbrauchsermittlung.
    """

    TZ_STANDARD = "TZ_STANDARD"
    TZ_HT = "TZ_HT"
    TZ_NT = "TZ_NT"
