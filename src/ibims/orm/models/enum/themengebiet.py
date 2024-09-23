import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Themengebiet(str, Enum):
    """
    Über dieses ENUM kann eine thematische Zuordnung, beispielsweise eines Ansprechpartners, vorgenommen werden.
    """

    ALLGEMEINER_INFORMATIONSAUSTAUSCH = "ALLGEMEINER_INFORMATIONSAUSTAUSCH"
    AN_UND_ABMELDUNG = "AN_UND_ABMELDUNG"
    ANSPRECHPARTNER_ALLGEMEIN = "ANSPRECHPARTNER_ALLGEMEIN"
    ANSPRECHPARTNER_BDEW_DVGW = "ANSPRECHPARTNER_BDEW_DVGW"
    ANSPRECHPARTNER_IT_TECHNIK = "ANSPRECHPARTNER_IT_TECHNIK"
    BILANZIERUNG = "BILANZIERUNG"
    BILANZKREISKOORDINATOR = "BILANZKREISKOORDINATOR"
    BILANZKREISVERANTWORTLICHER = "BILANZKREISVERANTWORTLICHER"
    DATENFORMATE_ZERTIFIKATE_VERSCHLUESSELUNGEN = "DATENFORMATE_ZERTIFIKATE_VERSCHLUESSELUNGEN"
    DEBITORENMANAGEMENT = "DEBITORENMANAGEMENT"
    DEMAND_SIDE_MANAGEMENT = "DEMAND_SIDE_MANAGEMENT"
    EDI_VEREINBARUNG = "EDI_VEREINBARUNG"
    EDIFACT = "EDIFACT"
    ENERGIEDATENMANAGEMENT = "ENERGIEDATENMANAGEMENT"
    FAHRPLANMANAGEMENT = "FAHRPLANMANAGEMENT"
    ALOCAT = "ALOCAT"
    APERAK = "APERAK"
    CONTRL = "CONTRL"
    INVOIC = "INVOIC"
    MSCONS = "MSCONS"
    ORDERS = "ORDERS"
    ORDERSP = "ORDERSP"
    REMADV = "REMADV"
    UTILMD = "UTILMD"
    GABI = "GABI"
    GELI = "GELI"
    GERAETERUECKGABE = "GERAETERUECKGABE"
    GERAETEWECHSEL = "GERAETEWECHSEL"
    GPKE = "GPKE"
    INBETRIEBNAHME = "INBETRIEBNAHME"
    KAPAZITAETSMANAGEMENT = "KAPAZITAETSMANAGEMENT"
    KLAERFAELLE = "KLAERFAELLE"
    LASTGAENGE_RLM = "LASTGAENGE_RLM"
    LIEFERANTENRAHMENVERTRAG = "LIEFERANTENRAHMENVERTRAG"
    LIEFERANTENWECHSEL = "LIEFERANTENWECHSEL"
    MABIS = "MABIS"
    MAHNWESEN = "MAHNWESEN"
    MARKTGEBIETSVERANTWORTLICHER = "MARKTGEBIETSVERANTWORTLICHER"
    MARKTKOMMUNIKATION = "MARKTKOMMUNIKATION"
    MEHR_MINDERMENGEN = "MEHR_MINDERMENGEN"
    MSB_MDL = "MSB_MDL"
    NETZABRECHNUNG = "NETZABRECHNUNG"
    NETZENTGELTE = "NETZENTGELTE"
    NETZMANAGEMENT = "NETZMANAGEMENT"
    RECHT = "RECHT"
    REGULIERUNGSMANAGEMENT = "REGULIERUNGSMANAGEMENT"
    REKLAMATIONEN = "REKLAMATIONEN"
    SPERREN_ENTSPERREN_INKASSO = "SPERREN_ENTSPERREN_INKASSO"
    STAMMDATEN = "STAMMDATEN"
    STOERUNGSFAELLE = "STOERUNGSFAELLE"
    TECHNISCHE_FRAGEN = "TECHNISCHE_FRAGEN"
    UMSTELLUNG_INVOIC = "UMSTELLUNG_INVOIC"
    VERSCHLUESSELUNG_SIGNATUR = "VERSCHLUESSELUNG_SIGNATUR"
    VERTRAGSMANAGEMENT = "VERTRAGSMANAGEMENT"
    VERTRIEB = "VERTRIEB"
    WIM = "WIM"
    ZAEHLERSTAENDE_SLP = "ZAEHLERSTAENDE_SLP"
    ZAHLUNGSVERKEHR = "ZAHLUNGSVERKEHR"
    ZUORDNUNGSVEREINBARUNG = "ZUORDNUNGSVEREINBARUNG"
    EINSPEISUNG = "EINSPEISUNG"
    BEWEGUNGSDATEN = "BEWEGUNGSDATEN"
