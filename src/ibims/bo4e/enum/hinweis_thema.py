from enum import Enum


class HinweisThema(str, Enum):
    """
    Topics for the hints
    """

    SCHLECHTZAHLER = "SCHLECHTZAHLER"
    STROMLIEBHABER = "STROMLIEBHABER"
    STORNIERUNG = "STORNIERUNG"
    STAMMDATEN = "STAMMDATEN"
    LEGAL = "LEGAL"
    KUENDIGUNG = "KUENDIGUNG"
    BESCHWERDE = "BESCHWERDE"
    WIDERRUF = "WIDERRUF"
    KUNDENPORTAL = "KUNDENPORTAL"
    PREISANPASSUNG = "PREISANPASSUNG"
    ANMELDUNG = "ANMELDUNG"
    BONUS = "BONUS"
    LIEFERANTENWECHSEL = "LIEFERANTENWECHSEL"
    MAHNUNG = "MAHNUNG"
    RECHNUNG = "RECHNUNG"
    UMZUG = "UMZUG"
    VERTRAG = "VERTRAG"
    ZAHLUNG = "ZAHLUNG"
    ZAEHLERSTAND = "ZAEHLERSTAND"
    ABSCHLAG = "ABSCHLAG"
    CLEARINGDATEN = "CLEARINGDATEN"
    KLAERUNGMARKTPARTNER = "KLAERUNGMARKTPARTNER"
    MEHRVERBRAUCHTROCKNUNGSMASSNAHME = "MEHRVERBRAUCHTROCKNUNGSMASSNAHME"
    RECHNUNGSKORREKTUR = "RECHNUNGSKORREKTUR"
    REKLAMATION = "REKLAMATION"
    VERTRIEBSPARTNER = "VERTRIEBSPARTNER"
    VOLLMACHT = "VOLLMACHT"
    ENERGIEPREISMASSNAHMEN = "ENERGIEPREISMASSNAHMEN"
    ANDERE = "ANDERE"
    MARKETINGKAMPAGNE = "MARKETINGKAMPAGNE"
