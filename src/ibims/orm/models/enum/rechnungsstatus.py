import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Rechnungsstatus(str, Enum):
    """
    Abbildung verschiedener Zustände, die im Rahmen der Rechnungsbearbeitung durchlaufen werden.
    """

    UNGEPRUEFT = "UNGEPRUEFT"
    GEPRUEFT_OK = "GEPRUEFT_OK"
    GEPRUEFT_FEHLERHAFT = "GEPRUEFT_FEHLERHAFT"
    GEBUCHT = "GEBUCHT"
    BEZAHLT = "BEZAHLT"
