import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Zaehlerauspraegung(str, Enum):
    """
    Gibt an, ob es sich um einen Einrichtungs- oder Zweirichtungszähler handelt.
    """

    EINRICHTUNGSZAEHLER = "EINRICHTUNGSZAEHLER"
    ZWEIRICHTUNGSZAEHLER = "ZWEIRICHTUNGSZAEHLER"
