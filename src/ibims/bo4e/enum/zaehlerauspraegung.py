from enum import Enum


class Zaehlerauspraegung(str, Enum):
    """
    Gibt an, ob es sich um einen Einrichtungs- oder ZweirichtungszÃ¤hler handelt.
    """

    EINRICHTUNGSZAEHLER = "EINRICHTUNGSZAEHLER"
    ZWEIRICHTUNGSZAEHLER = "ZWEIRICHTUNGSZAEHLER"
