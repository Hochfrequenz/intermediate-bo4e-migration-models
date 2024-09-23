import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.many import ZeitraumzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.ausschreibung import Ausschreibung
    from ibims.orm.models.bo.fremdkosten import Fremdkosten
    from ibims.orm.models.bo.kosten import Kosten
    from ibims.orm.models.bo.preisblatt import Preisblatt
    from ibims.orm.models.bo.preisblatt_dienstleistung import PreisblattDienstleistung
    from ibims.orm.models.bo.preisblatt_hardware import PreisblattHardware
    from ibims.orm.models.bo.preisblatt_konzessionsabgabe import PreisblattKonzessionsabgabe
    from ibims.orm.models.bo.preisblatt_messung import PreisblattMessung
    from ibims.orm.models.bo.preisblatt_netznutzung import PreisblattNetznutzung
    from ibims.orm.models.bo.rechnung import Rechnung
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.bo.tarif import Tarif
    from ibims.orm.models.bo.tarifinfo import Tarifinfo
    from ibims.orm.models.bo.tarifkosten import Tarifkosten
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.bo.zaehler import Zaehler
    from ibims.orm.models.bo.zaehler_gas import ZaehlerGas
    from ibims.orm.models.com.angebotsteil import Angebotsteil
    from ibims.orm.models.com.auf_abschlag import AufAbschlag
    from ibims.orm.models.com.auf_abschlag_regional import AufAbschlagRegional
    from ibims.orm.models.com.ausschreibungsdetail import Ausschreibungsdetail
    from ibims.orm.models.com.ausschreibungslos import Ausschreibungslos
    from ibims.orm.models.com.preisgarantie import Preisgarantie
    from ibims.orm.models.com.regionale_preisgarantie import RegionalePreisgarantie
    from ibims.orm.models.com.regionaler_auf_abschlag import RegionalerAufAbschlag
    from ibims.orm.models.com.vertragskonditionen import Vertragskonditionen
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Zeitraum(SQLModel, table=True):
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher eine der drei Möglichkeiten angegeben sein:
    - Einheit und Dauer oder
    - Zeitraum: Startdatum bis Enddatum oder
    - Zeitraum: Startzeitpunkt (Datum und Uhrzeit) bis Endzeitpunkt (Datum und Uhrzeit)

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitraum.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitraum JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Zeitraum.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = None

    # pylint: disable=duplicate-code
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        extra="allow",
        # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create
        # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.
        # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375
        json_encoders={Decimal: str},
    )
    """
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    dauer: float | None = Field(default=None, title="Dauer")
    enddatum: datetime | None = Field(default=None, title="Enddatum")
    endzeitpunkt: datetime | None = Field(default=None, title="Endzeitpunkt")
    startdatum: datetime | None = Field(default=None, title="Startdatum")
    startzeitpunkt: datetime | None = Field(default=None, title="Startzeitpunkt")
    zeitraum_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    ausschreibung_abgabefrist: List["Ausschreibung"] = Relationship(
        back_populates="abgabefrist",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibung.abgabefrist_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibung_bindefrist: List["Ausschreibung"] = Relationship(
        back_populates="bindefrist",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibung.bindefrist_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    fremdkosten_gueltigkeit: List["Fremdkosten"] = Relationship(
        back_populates="gueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "Fremdkosten.gueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    kosten_gueltigkeit: List["Kosten"] = Relationship(
        back_populates="gueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "Kosten.gueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    preisblatt_gueltigkeit: List["Preisblatt"] = Relationship(
        back_populates="gueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "Preisblatt.gueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    preisblattdienstleistung_gueltigkeit: List["PreisblattDienstleistung"] = Relationship(
        back_populates="gueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattDienstleistung.gueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    preisblatthardware_gueltigkeit: List["PreisblattHardware"] = Relationship(
        back_populates="gueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattHardware.gueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    preisblattkonzessionsabgabe_gueltigkeit: List["PreisblattKonzessionsabgabe"] = Relationship(
        back_populates="gueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattKonzessionsabgabe.gueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    preisblattmessung_gueltigkeit: List["PreisblattMessung"] = Relationship(
        back_populates="gueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattMessung.gueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    preisblattnetznutzung_gueltigkeit: List["PreisblattNetznutzung"] = Relationship(
        back_populates="gueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattNetznutzung.gueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    rechnung_rechnungsperiode: List["Rechnung"] = Relationship(
        back_populates="rechnungsperiode",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.rechnungsperiode_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    regionaltarif_zeitlicheGueltigkeit: List["Regionaltarif"] = Relationship(
        back_populates="zeitlicheGueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "Regionaltarif.zeitlicheGueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    tarif_zeitlicheGueltigkeit: List["Tarif"] = Relationship(
        back_populates="zeitlicheGueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "Tarif.zeitlicheGueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    tarifinfo_zeitlicheGueltigkeit: List["Tarifinfo"] = Relationship(
        back_populates="zeitlicheGueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifinfo.zeitlicheGueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    tarifkosten_zeitlicheGueltigkeit: List["Tarifkosten"] = Relationship(
        back_populates="zeitlicheGueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifkosten.zeitlicheGueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    tarifpreisblatt_zeitlicheGueltigkeit: List["Tarifpreisblatt"] = Relationship(
        back_populates="zeitlicheGueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifpreisblatt.zeitlicheGueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    zaehler_aktiverZeitraum: List["Zaehler"] = Relationship(
        back_populates="aktiverZeitraum",
        sa_relationship_kwargs={
            "primaryjoin": "Zaehler.aktiverZeitraum_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    zaehlergas_aktiverZeitraum: List["ZaehlerGas"] = Relationship(
        back_populates="aktiverZeitraum",
        sa_relationship_kwargs={
            "primaryjoin": "ZaehlerGas.aktiverZeitraum_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    angebotsteil_lieferzeitraum: List["Angebotsteil"] = Relationship(
        back_populates="lieferzeitraum",
        sa_relationship_kwargs={
            "primaryjoin": "Angebotsteil.lieferzeitraum_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    aufabschlag_gueltigkeitszeitraum: List["AufAbschlag"] = Relationship(
        back_populates="gueltigkeitszeitraum",
        sa_relationship_kwargs={
            "primaryjoin": "AufAbschlag.gueltigkeitszeitraum_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    aufabschlagregional_gueltigkeitszeitraum: List["AufAbschlagRegional"] = Relationship(
        back_populates="gueltigkeitszeitraum",
        sa_relationship_kwargs={
            "primaryjoin": "AufAbschlagRegional.gueltigkeitszeitraum_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungsdetail_lieferzeitraum: List["Ausschreibungsdetail"] = Relationship(
        back_populates="lieferzeitraum",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungsdetail.lieferzeitraum_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungslos_lieferzeitraum: List["Ausschreibungslos"] = Relationship(
        back_populates="lieferzeitraum",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungslos.lieferzeitraum_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungslos_wiederholungsintervall: List["Ausschreibungslos"] = Relationship(
        back_populates="wiederholungsintervall",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungslos.wiederholungsintervall_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungslos_wunschKuendingungsfrist: List["Ausschreibungslos"] = Relationship(
        back_populates="wunschKuendingungsfrist",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungslos.wunschKuendingungsfrist_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungslos_wunschZahlungsziel: List["Ausschreibungslos"] = Relationship(
        back_populates="wunschZahlungsziel",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungslos.wunschZahlungsziel_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    preisgarantie_zeitlicheGueltigkeit: List["Preisgarantie"] = Relationship(
        back_populates="zeitlicheGueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "Preisgarantie.zeitlicheGueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    regionalepreisgarantie_zeitlicheGueltigkeit: List["RegionalePreisgarantie"] = Relationship(
        back_populates="zeitlicheGueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "RegionalePreisgarantie.zeitlicheGueltigkeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    regionaleraufabschlag_gueltigkeitszeitraum: List["RegionalerAufAbschlag"] = Relationship(
        back_populates="gueltigkeitszeitraum",
        sa_relationship_kwargs={
            "primaryjoin": "RegionalerAufAbschlag.gueltigkeitszeitraum_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    vertragskonditionen_abschlagszyklus: List["Vertragskonditionen"] = Relationship(
        back_populates="abschlagszyklus",
        sa_relationship_kwargs={
            "primaryjoin": "Vertragskonditionen.abschlagszyklus_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    vertragskonditionen_kuendigungsfrist: List["Vertragskonditionen"] = Relationship(
        back_populates="kuendigungsfrist",
        sa_relationship_kwargs={
            "primaryjoin": "Vertragskonditionen.kuendigungsfrist_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    vertragskonditionen_vertragslaufzeit: List["Vertragskonditionen"] = Relationship(
        back_populates="vertragslaufzeit",
        sa_relationship_kwargs={
            "primaryjoin": "Vertragskonditionen.vertragslaufzeit_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    vertragskonditionen_vertragsverlaengerung: List["Vertragskonditionen"] = Relationship(
        back_populates="vertragsverlaengerung",
        sa_relationship_kwargs={
            "primaryjoin": "Vertragskonditionen.vertragsverlaengerung_id==Zeitraum.zeitraum_sqlid",
            "lazy": "joined",
        },
    )
    einheit: Mengeneinheit | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="zeitraum_zusatzattribute_link",
        link_model=ZeitraumzusatzAttributeLink,
    )
