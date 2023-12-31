from enum import Enum


class Dienstleistungstyp(str, Enum):
    """
    Auflistung möglicher abzurechnender Dienstleistungen.
    """

    DATENBEREITSTELLUNG_TAEGLICH = "DATENBEREITSTELLUNG_TAEGLICH"
    DATENBEREITSTELLUNG_WOECHENTLICH = "DATENBEREITSTELLUNG_WOECHENTLICH"
    DATENBEREITSTELLUNG_MONATLICH = "DATENBEREITSTELLUNG_MONATLICH"
    DATENBEREITSTELLUNG_JAEHRLICH = "DATENBEREITSTELLUNG_JAEHRLICH"
    DATENBEREITSTELLUNG_HISTORISCHE_LG = "DATENBEREITSTELLUNG_HISTORISCHE_LG"
    DATENBEREITSTELLUNG_STUENDLICH = "DATENBEREITSTELLUNG_STUENDLICH"
    DATENBEREITSTELLUNG_VIERTELJAEHRLICH = "DATENBEREITSTELLUNG_VIERTELJAEHRLICH"
    DATENBEREITSTELLUNG_HALBJAEHRLICH = "DATENBEREITSTELLUNG_HALBJAEHRLICH"
    DATENBEREITSTELLUNG_MONATLICH_ZUSAETZLICH = "DATENBEREITSTELLUNG_MONATLICH_ZUSAETZLICH"
    DATENBEREITSTELLUNG_EINMALIG = "DATENBEREITSTELLUNG_EINMALIG"
    AUSLESUNG_2_X_TAEGLICH_FERNAUSLESUNG = "AUSLESUNG_2X_TAEGLICH_FERNAUSLESUNG"
    AUSLESUNG_TAEGLICH_FERNAUSLESUNG = "AUSLESUNG_TAEGLICH_FERNAUSLESUNG"
    AUSLESUNG_MANUELL_MSB = "AUSLESUNG_MANUELL_MSB"
    AUSLESUNG_MONATLICH_FERNAUSLESUNG = "AUSLESUNG_MONATLICH_FERNAUSLESUNG"
    AUSLESUNG_JAEHRLICH_FERNAUSLESUNG = "AUSLESUNG_JAEHRLICH_FERNAUSLESUNG"
    AUSLESUNG_MDE = "AUSLESUNG_MDE"
    ABLESUNG_MONATLICH = "ABLESUNG_MONATLICH"
    ABLESUNG_VIERTELJAEHRLICH = "ABLESUNG_VIERTELJAEHRLICH"
    ABLESUNG_HALBJAEHRLICH = "ABLESUNG_HALBJAEHRLICH"
    ABLESUNG_JAEHRLICH = "ABLESUNG_JAEHRLICH"
    AUSLESUNG_FERNAUSLESUNG = "AUSLESUNG_FERNAUSLESUNG"
    ABLESUNG_ZUSAETZLICH_MSB = "ABLESUNG_ZUSAETZLICH_MSB"
    ABLESUNG_ZUSAETZLICH_KUNDE = "ABLESUNG_ZUSAETZLICH_KUNDE"
    AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB = "AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB"
    AUSLESUNG_MOATLICH_FERNAUSLESUNG = "AUSLESUNG_MOATLICH_FERNAUSLESUNG"
    AUSLESUNG_STUENDLICH_FERNAUSLESUNG = "AUSLESUNG_STUENDLICH_FERNAUSLESUNG"
    AUSLESUNG_TEMPERATURMENGENUMWERTER = "AUSLESUNG_TEMPERATURMENGENUMWERTER"
    AUSLESUNG_ZUSTANDSMENGENUMWERTER = "AUSLESUNG_ZUSTANDSMENGENUMWERTER"
    AUSLESUNG_SYSTEMMENGENUMWERTER = "AUSLESUNG_SYSTEMMENGENUMWERTER"
    AUSLESUNG_VORGANG = "AUSLESUNG_VORGANG"
    AUSLESUNG_KOMPAKTMENGENUMWERTER = "AUSLESUNG_KOMPAKTMENGENUMWERTER"
    SPERRUNG = "SPERRUNG"
    ENTSPERRUNG = "ENTSPERRUNG"
    MAHNKOSTEN = "MAHNKOSTEN"
    INKASSOKOSTEN = "INKASSOKOSTEN"
