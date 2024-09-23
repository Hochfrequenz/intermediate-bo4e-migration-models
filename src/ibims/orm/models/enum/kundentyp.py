import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Kundentyp(str, Enum):
    """
    Auflistung der Typen von Endkunden. Daraus kann das Verbrauchsprofil abgeleitet werden.
    """

    GEWERBE = "GEWERBE"
    PRIVAT = "PRIVAT"
    LANDWIRT = "LANDWIRT"
    SONSTIGE = "SONSTIGE"
    HAUSHALT = "HAUSHALT"
    DIREKTHEIZUNG = "DIREKTHEIZUNG"
    GEMEINSCHAFT_MFH = "GEMEINSCHAFT_MFH"
    KIRCHE = "KIRCHE"
    KWK = "KWK"
    LADESAEULE = "LADESAEULE"
    BELEUCHTUNG_OEFFENTLICH = "BELEUCHTUNG_OEFFENTLICH"
    BELEUCHTUNG_STRASSE = "BELEUCHTUNG_STRASSE"
    SPEICHERHEIZUNG = "SPEICHERHEIZUNG"
    UNTERBR_EINRICHTUNG = "UNTERBR_EINRICHTUNG"
    WAERMEPUMPE = "WAERMEPUMPE"
