from enum import Enum


class Speicherart(str, Enum):
    """
    Art der Speicherung
    """

    WASSERSTOFFSPEICHER = "WASSERSTOFFSPEICHER"
    PUMPSPEICHER = "PUMPSPEICHER"
    BATTERIESPEICHER = "BATTERIESPEICHER"
    SONSTIGE_SPEICHERART = "SONSTIGE_SPEICHERART"
