import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Titel(str, Enum):
    """
    Übersicht möglicher Titel, z.B. eines Geschäftspartners.
    """

    DR = "DR"
    PROF = "PROF"
    PROF_DR = "PROF_DR"
