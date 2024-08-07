import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Waehrungseinheit(str, Enum):
    """
    In diesem Enum werden die Währungen und ihre Untereinheiten definiert, beispielsweise für die Verwendung in Preisen.
    """

    EUR = "EUR"
    CT = "CT"
