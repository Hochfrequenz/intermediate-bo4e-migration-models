from enum import Enum


class Rechnungsstatus(str, Enum):
    """
    Abbildung verschiedener ZustÃ¤nde, die im Rahmen der Rechnungsbearbeitung durchlaufen werden.
    """

    UNGEPRUEFT = "UNGEPRUEFT"
    GEPRUEFT_OK = "GEPRUEFT_OK"
    GEPRUEFT_FEHLERHAFT = "GEPRUEFT_FEHLERHAFT"
    GEBUCHT = "GEBUCHT"
    BEZAHLT = "BEZAHLT"
