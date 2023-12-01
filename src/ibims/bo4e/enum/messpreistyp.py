from enum import Enum


class Messpreistyp(str, Enum):
    """
    Festlegung, welcher Typ von Messung mit einem Preis belegt wird
    """

    MESSPREIS_G2_5 = "MESSPREIS_G2_5"
    MESSPREIS_G4 = "MESSPREIS_G4"
    MESSPREIS_G6 = "MESSPREIS_G6"
    MESSPREIS_G10 = "MESSPREIS_G10"
    MESSPREIS_G16 = "MESSPREIS_G16"
    MESSPREIS_G25 = "MESSPREIS_G25"
    MESSPREIS_G40 = "MESSPREIS_G40"
    ELEKTRONISCHER_AUFSATZ = "ELEKTRONISCHER_AUFSATZ"
    SMART_METER_MESSPREIS_G2_5 = "SMART_METER_MESSPREIS_G2_5"
    SMART_METER_MESSPREIS_G4 = "SMART_METER_MESSPREIS_G4"
    SMART_METER_MESSPREIS_G6 = "SMART_METER_MESSPREIS_G6"
    SMART_METER_MESSPREIS_G10 = "SMART_METER_MESSPREIS_G10"
    SMART_METER_MESSPREIS_G16 = "SMART_METER_MESSPREIS_G16"
    SMART_METER_MESSPREIS_G25 = "SMART_METER_MESSPREIS_G25"
    SMART_METER_MESSPREIS_G40 = "SMART_METER_MESSPREIS_G40"
    VERRECHNUNGSPREIS_ET_WECHSEL = "VERRECHNUNGSPREIS_ET_WECHSEL"
    VERRECHNUNGSPREIS_ET_DREH = "VERRECHNUNGSPREIS_ET_DREH"
    VERRECHNUNGSPREIS_ZT_WECHSEL = "VERRECHNUNGSPREIS_ZT_WECHSEL"
    VERRECHNUNGSPREIS_ZT_DREH = "VERRECHNUNGSPREIS_ZT_DREH"
    VERRECHNUNGSPREIS_L_ET = "VERRECHNUNGSPREIS_L_ET"
    VERRECHNUNGSPREIS_L_ZT = "VERRECHNUNGSPREIS_L_ZT"
    VERRECHNUNGSPREIS_SM = "VERRECHNUNGSPREIS_SM"
    AUFSCHLAG_WANDLER = "AUFSCHLAG_WANDLER"
    AUFSCHLAG_TARIFSCHALTUNG = "AUFSCHLAG_TARIFSCHALTUNG"
