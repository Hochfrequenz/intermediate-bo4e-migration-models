from enum import Enum


class Geraetetyp(str, Enum):
    """
    Auflistung mÃ¶glicher abzurechnender GerÃ¤tetypen.
    """

    MULTIPLEXANLAGE = "MULTIPLEXANLAGE"
    PAUSCHALANLAGE = "PAUSCHALANLAGE"
    VERSTAERKERANLAGE = "VERSTAERKERANLAGE"
    SUMMATIONSGERAET = "SUMMATIONSGERAET"
    IMPULSGEBER = "IMPULSGEBER"
    MENGENUMWERTER = "MENGENUMWERTER"
    STROMWANDLER = "STROMWANDLER"
    SPANNUNGSWANDLER = "SPANNUNGSWANDLER"
    KOMBIMESSWANDLER = "KOMBIMESSWANDLER"
    BLOCKSTROMWANDLER = "BLOCKSTROMWANDLER"
    DATENLOGGER = "DATENLOGGER"
    KOMMUNIKATIONSANSCHLUSS = "KOMMUNIKATIONSANSCHLUSS"
    MODEM = "MODEM"
    TELEKOMMUNIKATIONSEINRICHTUNG = "TELEKOMMUNIKATIONSEINRICHTUNG"
    MODERNE_MESSEINRICHTUNG = "MODERNE_MESSEINRICHTUNG"
    INTELLIGENTES_MESSYSTEM = "INTELLIGENTES_MESSYSTEM"
    STEUEREINRICHTUNG = "STEUEREINRICHTUNG"
    TARIFSCHALTGERAET = "TARIFSCHALTGERAET"
    RUNDSTEUEREMPFAENGER = "RUNDSTEUEREMPFAENGER"
    OPTIONALE_ZUS_ZAEHLEINRICHTUNG = "OPTIONALE_ZUS_ZAEHLEINRICHTUNG"
    MESSWANDLERSATZ_IMS_MME = "MESSWANDLERSATZ_IMS_MME"
    KOMBIMESSWANDLER_IMS_MME = "KOMBIMESSWANDLER_IMS_MME"
    TARIFSCHALTGERAET_IMS_MME = "TARIFSCHALTGERAET_IMS_MME"
    RUNDSTEUEREMPFAENGER_IMS_MME = "RUNDSTEUEREMPFAENGER_IMS_MME"
    TEMPERATUR_KOMPENSATION = "TEMPERATUR_KOMPENSATION"
    HOECHSTBELASTUNGS_ANZEIGER = "HOECHSTBELASTUNGS_ANZEIGER"
    SONSTIGES_GERAET = "SONSTIGES_GERAET"
    EDL_21 = "EDL_21"
    EDL_40_ZAEHLERAUFSATZ = "EDL_40_ZAEHLERAUFSATZ"
    EDL_40 = "EDL_40"
    TELEFONANSCHLUSS = "TELEFONANSCHLUSS"
    MODEM_GSM = "MODEM_GSM"
    MODEM_GPRS = "MODEM_GPRS"
    MODEM_FUNK = "MODEM_FUNK"
    MODEM_GSM_O_LG = "MODEM_GSM_O_LG"
    MODEM_GSM_M_LG = "MODEM_GSM_M_LG"
    MODEM_FESTNETZ = "MODEM_FESTNETZ"
    MODEM_GPRS_M_LG = "MODEM_GPRS_M_LG"
    PLC_KOM = "PLC_KOM"
    ETHERNET_KOM = "ETHERNET_KOM"
    DSL_KOM = "DSL_KOM"
    LTE_KOM = "LTE_KOM"
    KOMPAKT_MU = "KOMPAKT_MU"
    SYSTEM_MU = "SYSTEM_MU"
    TEMPERATUR_MU = "TEMPERATUR_MU"
    ZUSTANDS_MU = "ZUSTANDS_MU"
