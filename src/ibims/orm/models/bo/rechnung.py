import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.netznutzung_rechnungsart import NetznutzungRechnungsart
from ibims.orm.models.enum.netznutzung_rechnungstyp import NetznutzungRechnungstyp
from ibims.orm.models.enum.rechnungsstatus import Rechnungsstatus
from ibims.orm.models.enum.rechnungstyp import Rechnungstyp
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import (
    RechnungrechnungspositionenLink,
    RechnungsteuerbetraegeLink,
    RechnungzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.bo.messlokation import Messlokation
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.rechnungsposition import Rechnungsposition
    from ibims.orm.models.com.steuerbetrag import Steuerbetrag
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Rechnung(SQLModel, table=True):
    """
    Modell für die Abbildung von Rechnungen und Netznutzungsrechnungen im Kontext der Energiewirtschaft;

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Rechnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Rechnung.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    faelligkeitsdatum: datetime | None = Field(default=None, title="Faelligkeitsdatum")
    """
    Zu diesem Datum ist die Zahlung fällig
    """
    ist_original: bool | None = Field(default=None, alias="istOriginal", title="Istoriginal")
    """
    Kennzeichen, ob es sich um ein Original (true) oder eine Kopie handelt (false)
    """
    ist_simuliert: bool | None = Field(default=None, alias="istSimuliert", title="Istsimuliert")
    """
    Kennzeichen, ob es sich um eine simulierte Rechnung, z.B. zur Rechnungsprüfung handelt
    """
    ist_storno: bool | None = Field(default=None, alias="istStorno", title="Iststorno")
    """
    Eine im Verwendungskontext eindeutige Nummer für die Rechnung
    """
    original_rechnungsnummer: str | None = Field(
        default=None, alias="originalRechnungsnummer", title="Originalrechnungsnummer"
    )
    """
    Im Falle einer Stornorechnung (storno = true) steht hier die Rechnungsnummer der stornierten Rechnung
    """
    rechnungsdatum: datetime | None = Field(default=None, title="Rechnungsdatum")
    """
    Ausstellungsdatum der Rechnung
    """
    rechnungsnummer: str | None = Field(default=None, title="Rechnungsnummer")
    """
    Eine im Verwendungskontext eindeutige Nummer für die Rechnung
    """
    rechnungstitel: str | None = Field(default=None, title="Rechnungstitel")
    """
    Bezeichnung für die vorliegende Rechnung
    """
    ist_selbstausgestellt: bool | None = Field(default=None, alias="istSelbstausgestellt", title="Istselbstausgestellt")
    ist_reverse_charge: bool | None = Field(default=None, alias="istReverseCharge", title="Istreversecharge")
    rechnung_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ | None = Field(Typ.RECHNUNG)
    gesamtbrutto_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    gesamtbrutto: "Betrag" = Relationship(
        back_populates="rechnung_gesamtbrutto",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.gesamtbrutto_id]"},
    )
    gesamtnetto_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    gesamtnetto: "Betrag" = Relationship(
        back_populates="rechnung_gesamtnetto",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.gesamtnetto_id]"},
    )
    gesamtsteuer_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    gesamtsteuer: "Betrag" = Relationship(
        back_populates="rechnung_gesamtsteuer",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.gesamtsteuer_id]"},
    )
    marktlokation_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktlokation.marktlokation_sqlid", ondelete="SET NULL"),
        )
    )
    marktlokation: "Marktlokation" = Relationship(
        back_populates="rechnung_marktlokation",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.marktlokation_id]"},
    )
    messlokation_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("messlokation.messlokation_sqlid", ondelete="SET NULL"),
        )
    )
    messlokation: "Messlokation" = Relationship(
        back_populates="rechnung_messlokation",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.messlokation_id]"},
    )
    netznutzungrechnungsart: NetznutzungRechnungsart | None = Field(None)
    netznutzungrechnungstyp: NetznutzungRechnungstyp | None = Field(None)
    rabattBrutto_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    rabattBrutto: "Betrag" = Relationship(
        back_populates="rechnung_rabattBrutto",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.rabattBrutto_id]"},
    )
    rechnungsempfaenger_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    rechnungsempfaenger: "Geschaeftspartner" = Relationship(
        back_populates="rechnung_rechnungsempfaenger",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.rechnungsempfaenger_id]"},
    )
    rechnungsersteller_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    rechnungsersteller: "Geschaeftspartner" = Relationship(
        back_populates="rechnung_rechnungsersteller",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.rechnungsersteller_id]"},
    )
    rechnungsperiode_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    rechnungsperiode: "Zeitraum" = Relationship(
        back_populates="rechnung_rechnungsperiode",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.rechnungsperiode_id]"},
    )
    rechnungspositionen: List["Rechnungsposition"] = Relationship(
        back_populates="rechnung_rechnungspositionen_link",
        link_model=RechnungrechnungspositionenLink,
    )
    rechnungsstatus: Rechnungsstatus | None = Field(None)
    rechnungstyp: Rechnungstyp | None = Field(None)
    sparte: Sparte | None = Field(None)
    steuerbetraege: List["Steuerbetrag"] = Relationship(
        back_populates="rechnung_steuerbetraege_link",
        link_model=RechnungsteuerbetraegeLink,
    )
    vorausgezahlt_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    vorausgezahlt: "Betrag" = Relationship(
        back_populates="rechnung_vorausgezahlt",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.vorausgezahlt_id]"},
    )
    zuZahlen_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    zuZahlen: "Betrag" = Relationship(
        back_populates="rechnung_zuZahlen",
        sa_relationship_kwargs={"foreign_keys": "[Rechnung.zuZahlen_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="rechnung_zusatzattribute_link",
        link_model=RechnungzusatzAttributeLink,
    )
