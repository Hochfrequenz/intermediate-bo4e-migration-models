import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Profiltyp(str, Enum):
    """
    This enum specifies the forecast (Prognosegrundlage)
    """

    SLP_SEP = "SLP_SEP"
    TLP_TEP = "TLP_TEP"
