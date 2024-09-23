import uuid as uuid_pkg
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import (
    AdressezusatzAttributeLink,
    AngebotspositionzusatzAttributeLink,
    AngebotsteilzusatzAttributeLink,
    AngebotsvariantezusatzAttributeLink,
    AngebotzusatzAttributeLink,
    AufAbschlagProOrtzusatzAttributeLink,
    AufAbschlagRegionalzusatzAttributeLink,
    AufAbschlagstaffelProOrtzusatzAttributeLink,
    AufAbschlagzusatzAttributeLink,
    AusschreibungsdetailzusatzAttributeLink,
    AusschreibungsloszusatzAttributeLink,
    AusschreibungzusatzAttributeLink,
    BetragzusatzAttributeLink,
    BilanzierungzusatzAttributeLink,
    BuendelvertragzusatzAttributeLink,
    DienstleistungzusatzAttributeLink,
    DokumentzusatzAttributeLink,
    EnergieherkunftzusatzAttributeLink,
    EnergiemengezusatzAttributeLink,
    EnergiemixzusatzAttributeLink,
    FremdkostenblockzusatzAttributeLink,
    FremdkostenpositionzusatzAttributeLink,
    FremdkostenzusatzAttributeLink,
    GeokoordinatenzusatzAttributeLink,
    GeraetzusatzAttributeLink,
    GeschaeftspartnerzusatzAttributeLink,
    HinweiszusatzAttributeLink,
    KampagnezusatzAttributeLink,
    KatasteradressezusatzAttributeLink,
    KontaktwegzusatzAttributeLink,
    KonzessionsabgabezusatzAttributeLink,
    KostenblockzusatzAttributeLink,
    KostenpositionzusatzAttributeLink,
    KostenzusatzAttributeLink,
    KriteriumWertzusatzAttributeLink,
    LastgangzusatzAttributeLink,
    MarktgebietInfozusatzAttributeLink,
    MarktlokationzusatzAttributeLink,
    MarktteilnehmerzusatzAttributeLink,
    MengezusatzAttributeLink,
    MesslokationszuordnungzusatzAttributeLink,
    MesslokationzusatzAttributeLink,
    PersonzusatzAttributeLink,
    PositionsAufAbschlagzusatzAttributeLink,
    PreisblattDienstleistungzusatzAttributeLink,
    PreisblattHardwarezusatzAttributeLink,
    PreisblattKonzessionsabgabezusatzAttributeLink,
    PreisblattMessungzusatzAttributeLink,
    PreisblattNetznutzungzusatzAttributeLink,
    PreisblattzusatzAttributeLink,
    PreisgarantiezusatzAttributeLink,
    PreispositionzusatzAttributeLink,
    PreisstaffelzusatzAttributeLink,
    PreiszusatzAttributeLink,
    RechnungspositionzusatzAttributeLink,
    RechnungzusatzAttributeLink,
    RegionaleGueltigkeitzusatzAttributeLink,
    RegionalePreisgarantiezusatzAttributeLink,
    RegionalePreisstaffelzusatzAttributeLink,
    RegionalerAufAbschlagzusatzAttributeLink,
    RegionaleTarifpreispositionzusatzAttributeLink,
    RegionaltarifzusatzAttributeLink,
    RegionskriteriumzusatzAttributeLink,
    RegionzusatzAttributeLink,
    SigmoidparameterzusatzAttributeLink,
    StandorteigenschaftenGaszusatzAttributeLink,
    StandorteigenschaftenStromzusatzAttributeLink,
    StandorteigenschaftenzusatzAttributeLink,
    SteuerbetragzusatzAttributeLink,
    TarifberechnungsparameterzusatzAttributeLink,
    TarifeinschraenkungzusatzAttributeLink,
    TarifinfozusatzAttributeLink,
    TarifkostenzusatzAttributeLink,
    TarifpreisblattzusatzAttributeLink,
    TarifpreispositionProOrtzusatzAttributeLink,
    TarifpreispositionzusatzAttributeLink,
    TarifpreisstaffelProOrtzusatzAttributeLink,
    TarifpreiszusatzAttributeLink,
    TarifzusatzAttributeLink,
    UnterschriftzusatzAttributeLink,
    VerbrauchzusatzAttributeLink,
    VertragskonditionenzusatzAttributeLink,
    VertragsteilzusatzAttributeLink,
    VertragzusatzAttributeLink,
    VerwendungszweckProMarktrollezusatzAttributeLink,
    ZaehlerGaszusatzAttributeLink,
    ZaehlerzusatzAttributeLink,
    ZaehlwerkzusatzAttributeLink,
    ZaehlzeitregisterzusatzAttributeLink,
    ZeitraumzusatzAttributeLink,
    ZeitreihenwertzusatzAttributeLink,
    ZeitreihezusatzAttributeLink,
    ZeitspannezusatzAttributeLink,
    ZustaendigkeitzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.angebot import Angebot
    from ibims.orm.models.bo.ausschreibung import Ausschreibung
    from ibims.orm.models.bo.bilanzierung import Bilanzierung
    from ibims.orm.models.bo.buendelvertrag import Buendelvertrag
    from ibims.orm.models.bo.dokument import Dokument
    from ibims.orm.models.bo.energiemenge import Energiemenge
    from ibims.orm.models.bo.fremdkosten import Fremdkosten
    from ibims.orm.models.bo.geraet import Geraet
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.bo.hinweis import Hinweis
    from ibims.orm.models.bo.kampagne import Kampagne
    from ibims.orm.models.bo.kosten import Kosten
    from ibims.orm.models.bo.lastgang import Lastgang
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.bo.marktteilnehmer import Marktteilnehmer
    from ibims.orm.models.bo.messlokation import Messlokation
    from ibims.orm.models.bo.person import Person
    from ibims.orm.models.bo.preisblatt import Preisblatt
    from ibims.orm.models.bo.preisblatt_dienstleistung import PreisblattDienstleistung
    from ibims.orm.models.bo.preisblatt_hardware import PreisblattHardware
    from ibims.orm.models.bo.preisblatt_konzessionsabgabe import PreisblattKonzessionsabgabe
    from ibims.orm.models.bo.preisblatt_messung import PreisblattMessung
    from ibims.orm.models.bo.preisblatt_netznutzung import PreisblattNetznutzung
    from ibims.orm.models.bo.rechnung import Rechnung
    from ibims.orm.models.bo.region import Region
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.bo.standorteigenschaften import Standorteigenschaften
    from ibims.orm.models.bo.tarif import Tarif
    from ibims.orm.models.bo.tarifinfo import Tarifinfo
    from ibims.orm.models.bo.tarifkosten import Tarifkosten
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.bo.vertrag import Vertrag
    from ibims.orm.models.bo.zaehler import Zaehler
    from ibims.orm.models.bo.zaehler_gas import ZaehlerGas
    from ibims.orm.models.bo.zeitreihe import Zeitreihe
    from ibims.orm.models.com.adresse import Adresse
    from ibims.orm.models.com.angebotsposition import Angebotsposition
    from ibims.orm.models.com.angebotsteil import Angebotsteil
    from ibims.orm.models.com.angebotsvariante import Angebotsvariante
    from ibims.orm.models.com.auf_abschlag import AufAbschlag
    from ibims.orm.models.com.auf_abschlag_pro_ort import AufAbschlagProOrt
    from ibims.orm.models.com.auf_abschlag_regional import AufAbschlagRegional
    from ibims.orm.models.com.auf_abschlagstaffel_pro_ort import AufAbschlagstaffelProOrt
    from ibims.orm.models.com.ausschreibungsdetail import Ausschreibungsdetail
    from ibims.orm.models.com.ausschreibungslos import Ausschreibungslos
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.dienstleistung import Dienstleistung
    from ibims.orm.models.com.energieherkunft import Energieherkunft
    from ibims.orm.models.com.energiemix import Energiemix
    from ibims.orm.models.com.fremdkostenblock import Fremdkostenblock
    from ibims.orm.models.com.fremdkostenposition import Fremdkostenposition
    from ibims.orm.models.com.geokoordinaten import Geokoordinaten
    from ibims.orm.models.com.katasteradresse import Katasteradresse
    from ibims.orm.models.com.kontaktweg import Kontaktweg
    from ibims.orm.models.com.konzessionsabgabe import Konzessionsabgabe
    from ibims.orm.models.com.kostenblock import Kostenblock
    from ibims.orm.models.com.kostenposition import Kostenposition
    from ibims.orm.models.com.kriterium_wert import KriteriumWert
    from ibims.orm.models.com.marktgebiet_info import MarktgebietInfo
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.com.messlokationszuordnung import Messlokationszuordnung
    from ibims.orm.models.com.positions_auf_abschlag import PositionsAufAbschlag
    from ibims.orm.models.com.preis import Preis
    from ibims.orm.models.com.preisgarantie import Preisgarantie
    from ibims.orm.models.com.preisposition import Preisposition
    from ibims.orm.models.com.preisstaffel import Preisstaffel
    from ibims.orm.models.com.rechnungsposition import Rechnungsposition
    from ibims.orm.models.com.regionale_gueltigkeit import RegionaleGueltigkeit
    from ibims.orm.models.com.regionale_preisgarantie import RegionalePreisgarantie
    from ibims.orm.models.com.regionale_preisstaffel import RegionalePreisstaffel
    from ibims.orm.models.com.regionale_tarifpreisposition import RegionaleTarifpreisposition
    from ibims.orm.models.com.regionaler_auf_abschlag import RegionalerAufAbschlag
    from ibims.orm.models.com.regionskriterium import Regionskriterium
    from ibims.orm.models.com.sigmoidparameter import Sigmoidparameter
    from ibims.orm.models.com.standorteigenschaften_gas import StandorteigenschaftenGas
    from ibims.orm.models.com.standorteigenschaften_strom import StandorteigenschaftenStrom
    from ibims.orm.models.com.steuerbetrag import Steuerbetrag
    from ibims.orm.models.com.tarifberechnungsparameter import Tarifberechnungsparameter
    from ibims.orm.models.com.tarifeinschraenkung import Tarifeinschraenkung
    from ibims.orm.models.com.tarifpreis import Tarifpreis
    from ibims.orm.models.com.tarifpreisposition import Tarifpreisposition
    from ibims.orm.models.com.tarifpreisposition_pro_ort import TarifpreispositionProOrt
    from ibims.orm.models.com.tarifpreisstaffel_pro_ort import TarifpreisstaffelProOrt
    from ibims.orm.models.com.unterschrift import Unterschrift
    from ibims.orm.models.com.verbrauch import Verbrauch
    from ibims.orm.models.com.vertragskonditionen import Vertragskonditionen
    from ibims.orm.models.com.vertragsteil import Vertragsteil
    from ibims.orm.models.com.verwendungszweck_pro_marktrolle import VerwendungszweckProMarktrolle
    from ibims.orm.models.com.zaehlwerk import Zaehlwerk
    from ibims.orm.models.com.zaehlzeitregister import Zaehlzeitregister
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.com.zeitreihenwert import Zeitreihenwert
    from ibims.orm.models.com.zeitspanne import Zeitspanne
    from ibims.orm.models.com.zustaendigkeit import Zustaendigkeit


class ZusatzAttribut(SQLModel, table=True):
    """
    Viele Datenobjekte weisen in unterschiedlichen Systemen eine eindeutige ID (Kundennummer, GP-Nummer etc.) auf.
    Beim Austausch von Datenobjekten zwischen verschiedenen Systemen ist es daher hilfreich,
    sich die eindeutigen IDs der anzubindenden Systeme zu merken.

    .. raw:: html

        <object data="../_static/images/bo4e/com/ZusatzAttribut.svg" type="image/svg+xml"></object>

    .. HINT::
        `ZusatzAttribut JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/ZusatzAttribut.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )
    name: str | None = Field(..., title="Name")
    """
    Bezeichnung der externen Referenz (z.B. "microservice xyz" oder "SAP CRM GP-Nummer")
    """
    zusatzattribut_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    wert: Any = Field(None, sa_column=Column(PickleType))
    angebot_zusatzattribute_link: List["Angebot"] = Relationship(
        back_populates="zusatzAttribute", link_model=AngebotzusatzAttributeLink
    )
    ausschreibung_zusatzattribute_link: List["Ausschreibung"] = Relationship(
        back_populates="zusatzAttribute", link_model=AusschreibungzusatzAttributeLink
    )
    bilanzierung_zusatzattribute_link: List["Bilanzierung"] = Relationship(
        back_populates="zusatzAttribute", link_model=BilanzierungzusatzAttributeLink
    )
    buendelvertrag_zusatzattribute_link: List["Buendelvertrag"] = Relationship(
        back_populates="zusatzAttribute", link_model=BuendelvertragzusatzAttributeLink
    )
    dokument_zusatzattribute_link: List["Dokument"] = Relationship(
        back_populates="zusatzAttribute", link_model=DokumentzusatzAttributeLink
    )
    energiemenge_zusatzattribute_link: List["Energiemenge"] = Relationship(
        back_populates="zusatzAttribute", link_model=EnergiemengezusatzAttributeLink
    )
    fremdkosten_zusatzattribute_link: List["Fremdkosten"] = Relationship(
        back_populates="zusatzAttribute", link_model=FremdkostenzusatzAttributeLink
    )
    geraet_zusatzattribute_link: List["Geraet"] = Relationship(
        back_populates="zusatzAttribute", link_model=GeraetzusatzAttributeLink
    )
    geschaeftspartner_zusatzattribute_link: List["Geschaeftspartner"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=GeschaeftspartnerzusatzAttributeLink,
    )
    hinweis_zusatzattribute_link: List["Hinweis"] = Relationship(
        back_populates="zusatzAttribute", link_model=HinweiszusatzAttributeLink
    )
    kampagne_zusatzattribute_link: List["Kampagne"] = Relationship(
        back_populates="zusatzAttribute", link_model=KampagnezusatzAttributeLink
    )
    kosten_zusatzattribute_link: List["Kosten"] = Relationship(
        back_populates="zusatzAttribute", link_model=KostenzusatzAttributeLink
    )
    lastgang_zusatzattribute_link: List["Lastgang"] = Relationship(
        back_populates="zusatzAttribute", link_model=LastgangzusatzAttributeLink
    )
    marktlokation_zusatzattribute_link: List["Marktlokation"] = Relationship(
        back_populates="zusatzAttribute", link_model=MarktlokationzusatzAttributeLink
    )
    marktteilnehmer_zusatzattribute_link: List["Marktteilnehmer"] = Relationship(
        back_populates="zusatzAttribute", link_model=MarktteilnehmerzusatzAttributeLink
    )
    messlokation_zusatzattribute_link: List["Messlokation"] = Relationship(
        back_populates="zusatzAttribute", link_model=MesslokationzusatzAttributeLink
    )
    person_zusatzattribute_link: List["Person"] = Relationship(
        back_populates="zusatzAttribute", link_model=PersonzusatzAttributeLink
    )
    preisblatt_zusatzattribute_link: List["Preisblatt"] = Relationship(
        back_populates="zusatzAttribute", link_model=PreisblattzusatzAttributeLink
    )
    preisblattdienstleistung_zusatzattribute_link: List["PreisblattDienstleistung"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=PreisblattDienstleistungzusatzAttributeLink,
    )
    preisblatthardware_zusatzattribute_link: List["PreisblattHardware"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=PreisblattHardwarezusatzAttributeLink,
    )
    preisblattkonzessionsabgabe_zusatzattribute_link: List["PreisblattKonzessionsabgabe"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=PreisblattKonzessionsabgabezusatzAttributeLink,
    )
    preisblattmessung_zusatzattribute_link: List["PreisblattMessung"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=PreisblattMessungzusatzAttributeLink,
    )
    preisblattnetznutzung_zusatzattribute_link: List["PreisblattNetznutzung"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=PreisblattNetznutzungzusatzAttributeLink,
    )
    rechnung_zusatzattribute_link: List["Rechnung"] = Relationship(
        back_populates="zusatzAttribute", link_model=RechnungzusatzAttributeLink
    )
    region_zusatzattribute_link: List["Region"] = Relationship(
        back_populates="zusatzAttribute", link_model=RegionzusatzAttributeLink
    )
    regionaltarif_zusatzattribute_link: List["Regionaltarif"] = Relationship(
        back_populates="zusatzAttribute", link_model=RegionaltarifzusatzAttributeLink
    )
    standorteigenschaften_zusatzattribute_link: List["Standorteigenschaften"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=StandorteigenschaftenzusatzAttributeLink,
    )
    tarif_zusatzattribute_link: List["Tarif"] = Relationship(
        back_populates="zusatzAttribute", link_model=TarifzusatzAttributeLink
    )
    tarifinfo_zusatzattribute_link: List["Tarifinfo"] = Relationship(
        back_populates="zusatzAttribute", link_model=TarifinfozusatzAttributeLink
    )
    tarifkosten_zusatzattribute_link: List["Tarifkosten"] = Relationship(
        back_populates="zusatzAttribute", link_model=TarifkostenzusatzAttributeLink
    )
    tarifpreisblatt_zusatzattribute_link: List["Tarifpreisblatt"] = Relationship(
        back_populates="zusatzAttribute", link_model=TarifpreisblattzusatzAttributeLink
    )
    vertrag_zusatzattribute_link: List["Vertrag"] = Relationship(
        back_populates="zusatzAttribute", link_model=VertragzusatzAttributeLink
    )
    zaehler_zusatzattribute_link: List["Zaehler"] = Relationship(
        back_populates="zusatzAttribute", link_model=ZaehlerzusatzAttributeLink
    )
    zaehlergas_zusatzattribute_link: List["ZaehlerGas"] = Relationship(
        back_populates="zusatzAttribute", link_model=ZaehlerGaszusatzAttributeLink
    )
    zeitreihe_zusatzattribute_link: List["Zeitreihe"] = Relationship(
        back_populates="zusatzAttribute", link_model=ZeitreihezusatzAttributeLink
    )
    adresse_zusatzattribute_link: List["Adresse"] = Relationship(
        back_populates="zusatzAttribute", link_model=AdressezusatzAttributeLink
    )
    angebotsposition_zusatzattribute_link: List["Angebotsposition"] = Relationship(
        back_populates="zusatzAttribute", link_model=AngebotspositionzusatzAttributeLink
    )
    angebotsteil_zusatzattribute_link: List["Angebotsteil"] = Relationship(
        back_populates="zusatzAttribute", link_model=AngebotsteilzusatzAttributeLink
    )
    angebotsvariante_zusatzattribute_link: List["Angebotsvariante"] = Relationship(
        back_populates="zusatzAttribute", link_model=AngebotsvariantezusatzAttributeLink
    )
    aufabschlag_zusatzattribute_link: List["AufAbschlag"] = Relationship(
        back_populates="zusatzAttribute", link_model=AufAbschlagzusatzAttributeLink
    )
    aufabschlagproort_zusatzattribute_link: List["AufAbschlagProOrt"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=AufAbschlagProOrtzusatzAttributeLink,
    )
    aufabschlagregional_zusatzattribute_link: List["AufAbschlagRegional"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=AufAbschlagRegionalzusatzAttributeLink,
    )
    aufabschlagstaffelproort_zusatzattribute_link: List["AufAbschlagstaffelProOrt"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=AufAbschlagstaffelProOrtzusatzAttributeLink,
    )
    ausschreibungsdetail_zusatzattribute_link: List["Ausschreibungsdetail"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=AusschreibungsdetailzusatzAttributeLink,
    )
    ausschreibungslos_zusatzattribute_link: List["Ausschreibungslos"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=AusschreibungsloszusatzAttributeLink,
    )
    betrag_zusatzattribute_link: List["Betrag"] = Relationship(
        back_populates="zusatzAttribute", link_model=BetragzusatzAttributeLink
    )
    dienstleistung_zusatzattribute_link: List["Dienstleistung"] = Relationship(
        back_populates="zusatzAttribute", link_model=DienstleistungzusatzAttributeLink
    )
    energieherkunft_zusatzattribute_link: List["Energieherkunft"] = Relationship(
        back_populates="zusatzAttribute", link_model=EnergieherkunftzusatzAttributeLink
    )
    energiemix_zusatzattribute_link: List["Energiemix"] = Relationship(
        back_populates="zusatzAttribute", link_model=EnergiemixzusatzAttributeLink
    )
    fremdkostenblock_zusatzattribute_link: List["Fremdkostenblock"] = Relationship(
        back_populates="zusatzAttribute", link_model=FremdkostenblockzusatzAttributeLink
    )
    fremdkostenposition_zusatzattribute_link: List["Fremdkostenposition"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=FremdkostenpositionzusatzAttributeLink,
    )
    geokoordinaten_zusatzattribute_link: List["Geokoordinaten"] = Relationship(
        back_populates="zusatzAttribute", link_model=GeokoordinatenzusatzAttributeLink
    )
    katasteradresse_zusatzattribute_link: List["Katasteradresse"] = Relationship(
        back_populates="zusatzAttribute", link_model=KatasteradressezusatzAttributeLink
    )
    kontaktweg_zusatzattribute_link: List["Kontaktweg"] = Relationship(
        back_populates="zusatzAttribute", link_model=KontaktwegzusatzAttributeLink
    )
    konzessionsabgabe_zusatzattribute_link: List["Konzessionsabgabe"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=KonzessionsabgabezusatzAttributeLink,
    )
    kostenblock_zusatzattribute_link: List["Kostenblock"] = Relationship(
        back_populates="zusatzAttribute", link_model=KostenblockzusatzAttributeLink
    )
    kostenposition_zusatzattribute_link: List["Kostenposition"] = Relationship(
        back_populates="zusatzAttribute", link_model=KostenpositionzusatzAttributeLink
    )
    kriteriumwert_zusatzattribute_link: List["KriteriumWert"] = Relationship(
        back_populates="zusatzAttribute", link_model=KriteriumWertzusatzAttributeLink
    )
    marktgebietinfo_zusatzattribute_link: List["MarktgebietInfo"] = Relationship(
        back_populates="zusatzAttribute", link_model=MarktgebietInfozusatzAttributeLink
    )
    menge_zusatzattribute_link: List["Menge"] = Relationship(
        back_populates="zusatzAttribute", link_model=MengezusatzAttributeLink
    )
    messlokationszuordnung_zusatzattribute_link: List["Messlokationszuordnung"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=MesslokationszuordnungzusatzAttributeLink,
    )
    positionsaufabschlag_zusatzattribute_link: List["PositionsAufAbschlag"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=PositionsAufAbschlagzusatzAttributeLink,
    )
    preis_zusatzattribute_link: List["Preis"] = Relationship(
        back_populates="zusatzAttribute", link_model=PreiszusatzAttributeLink
    )
    preisgarantie_zusatzattribute_link: List["Preisgarantie"] = Relationship(
        back_populates="zusatzAttribute", link_model=PreisgarantiezusatzAttributeLink
    )
    preisposition_zusatzattribute_link: List["Preisposition"] = Relationship(
        back_populates="zusatzAttribute", link_model=PreispositionzusatzAttributeLink
    )
    preisstaffel_zusatzattribute_link: List["Preisstaffel"] = Relationship(
        back_populates="zusatzAttribute", link_model=PreisstaffelzusatzAttributeLink
    )
    rechnungsposition_zusatzattribute_link: List["Rechnungsposition"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=RechnungspositionzusatzAttributeLink,
    )
    regionalegueltigkeit_zusatzattribute_link: List["RegionaleGueltigkeit"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=RegionaleGueltigkeitzusatzAttributeLink,
    )
    regionalepreisgarantie_zusatzattribute_link: List["RegionalePreisgarantie"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=RegionalePreisgarantiezusatzAttributeLink,
    )
    regionalepreisstaffel_zusatzattribute_link: List["RegionalePreisstaffel"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=RegionalePreisstaffelzusatzAttributeLink,
    )
    regionaleraufabschlag_zusatzattribute_link: List["RegionalerAufAbschlag"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=RegionalerAufAbschlagzusatzAttributeLink,
    )
    regionaletarifpreisposition_zusatzattribute_link: List["RegionaleTarifpreisposition"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=RegionaleTarifpreispositionzusatzAttributeLink,
    )
    regionskriterium_zusatzattribute_link: List["Regionskriterium"] = Relationship(
        back_populates="zusatzAttribute", link_model=RegionskriteriumzusatzAttributeLink
    )
    sigmoidparameter_zusatzattribute_link: List["Sigmoidparameter"] = Relationship(
        back_populates="zusatzAttribute", link_model=SigmoidparameterzusatzAttributeLink
    )
    standorteigenschaftengas_zusatzattribute_link: List["StandorteigenschaftenGas"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=StandorteigenschaftenGaszusatzAttributeLink,
    )
    standorteigenschaftenstrom_zusatzattribute_link: List["StandorteigenschaftenStrom"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=StandorteigenschaftenStromzusatzAttributeLink,
    )
    steuerbetrag_zusatzattribute_link: List["Steuerbetrag"] = Relationship(
        back_populates="zusatzAttribute", link_model=SteuerbetragzusatzAttributeLink
    )
    tarifberechnungsparameter_zusatzattribute_link: List["Tarifberechnungsparameter"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=TarifberechnungsparameterzusatzAttributeLink,
    )
    tarifeinschraenkung_zusatzattribute_link: List["Tarifeinschraenkung"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=TarifeinschraenkungzusatzAttributeLink,
    )
    tarifpreis_zusatzattribute_link: List["Tarifpreis"] = Relationship(
        back_populates="zusatzAttribute", link_model=TarifpreiszusatzAttributeLink
    )
    tarifpreisposition_zusatzattribute_link: List["Tarifpreisposition"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=TarifpreispositionzusatzAttributeLink,
    )
    tarifpreispositionproort_zusatzattribute_link: List["TarifpreispositionProOrt"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=TarifpreispositionProOrtzusatzAttributeLink,
    )
    tarifpreisstaffelproort_zusatzattribute_link: List["TarifpreisstaffelProOrt"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=TarifpreisstaffelProOrtzusatzAttributeLink,
    )
    unterschrift_zusatzattribute_link: List["Unterschrift"] = Relationship(
        back_populates="zusatzAttribute", link_model=UnterschriftzusatzAttributeLink
    )
    verbrauch_zusatzattribute_link: List["Verbrauch"] = Relationship(
        back_populates="zusatzAttribute", link_model=VerbrauchzusatzAttributeLink
    )
    vertragskonditionen_zusatzattribute_link: List["Vertragskonditionen"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=VertragskonditionenzusatzAttributeLink,
    )
    vertragsteil_zusatzattribute_link: List["Vertragsteil"] = Relationship(
        back_populates="zusatzAttribute", link_model=VertragsteilzusatzAttributeLink
    )
    verwendungszweckpromarktrolle_zusatzattribute_link: List["VerwendungszweckProMarktrolle"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=VerwendungszweckProMarktrollezusatzAttributeLink,
    )
    zaehlwerk_zusatzattribute_link: List["Zaehlwerk"] = Relationship(
        back_populates="zusatzAttribute", link_model=ZaehlwerkzusatzAttributeLink
    )
    zaehlzeitregister_zusatzattribute_link: List["Zaehlzeitregister"] = Relationship(
        back_populates="zusatzAttribute",
        link_model=ZaehlzeitregisterzusatzAttributeLink,
    )
    zeitraum_zusatzattribute_link: List["Zeitraum"] = Relationship(
        back_populates="zusatzAttribute", link_model=ZeitraumzusatzAttributeLink
    )
    zeitreihenwert_zusatzattribute_link: List["Zeitreihenwert"] = Relationship(
        back_populates="zusatzAttribute", link_model=ZeitreihenwertzusatzAttributeLink
    )
    zeitspanne_zusatzattribute_link: List["Zeitspanne"] = Relationship(
        back_populates="zusatzAttribute", link_model=ZeitspannezusatzAttributeLink
    )
    zustaendigkeit_zusatzattribute_link: List["Zustaendigkeit"] = Relationship(
        back_populates="zusatzAttribute", link_model=ZustaendigkeitzusatzAttributeLink
    )
