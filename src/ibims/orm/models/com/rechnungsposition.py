import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.bdew_artikelnummer import BDEWArtikelnummer
from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.many import RechnungrechnungspositionenLink, RechnungspositionzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.rechnung import Rechnung
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.com.preis import Preis
    from ibims.orm.models.com.steuerbetrag import Steuerbetrag
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Rechnungsposition(SQLModel, table=True):
    """
    Über Rechnungspositionen werden Rechnungen strukturiert.
    In einem Rechnungsteil wird jeweils eine in sich geschlossene Leistung abgerechnet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Rechnungsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnungsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Rechnungsposition.json>`_
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
    artikel_id: str | None = Field(default=None, alias="artikelId", title="Artikelid")
    """
    Standardisierte vom BDEW herausgegebene Liste, welche im Strommarkt die BDEW-Artikelnummer ablöst
    """
    lieferung_bis: datetime | None = Field(default=None, alias="lieferungBis", title="Lieferungbis")
    """
    Ende der Lieferung für die abgerechnete Leistung (exklusiv)
    """
    lieferung_von: datetime | None = Field(default=None, alias="lieferungVon", title="Lieferungvon")
    """
    Start der Lieferung für die abgerechnete Leistung (inklusiv)
    """
    lokations_id: str | None = Field(default=None, alias="lokationsId", title="Lokationsid")
    """
    Marktlokation, die zu dieser Position gehört
    """
    positionsnummer: int | None = Field(default=None, title="Positionsnummer")
    """
    Fortlaufende Nummer für die Rechnungsposition
    """
    positionstext: str | None = Field(default=None, title="Positionstext")
    """
    Bezeichung für die abgerechnete Position
    """
    rechnungsposition_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    rechnung_rechnungspositionen_link: List["Rechnung"] = Relationship(
        back_populates="rechnungspositionen", link_model=RechnungrechnungspositionenLink
    )
    artikelnummer: BDEWArtikelnummer | None = Field(None)
    einzelpreis_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("preis.preis_sqlid", ondelete="SET NULL"))
    )
    einzelpreis: "Preis" = Relationship(
        back_populates="rechnungsposition_einzelpreis",
        sa_relationship_kwargs={"foreign_keys": "[Rechnungsposition.einzelpreis_id]"},
    )
    positionsMenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    positionsMenge: "Menge" = Relationship(
        back_populates="rechnungsposition_positionsMenge",
        sa_relationship_kwargs={"foreign_keys": "[Rechnungsposition.positionsMenge_id]"},
    )
    teilrabattNetto_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    teilrabattNetto: "Betrag" = Relationship(
        back_populates="rechnungsposition_teilrabattNetto",
        sa_relationship_kwargs={"foreign_keys": "[Rechnungsposition.teilrabattNetto_id]"},
    )
    teilsummeNetto_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    teilsummeNetto: "Betrag" = Relationship(
        back_populates="rechnungsposition_teilsummeNetto",
        sa_relationship_kwargs={"foreign_keys": "[Rechnungsposition.teilsummeNetto_id]"},
    )
    teilsummeSteuer_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("steuerbetrag.steuerbetrag_sqlid", ondelete="SET NULL"),
        )
    )
    teilsummeSteuer: "Steuerbetrag" = Relationship(
        back_populates="rechnungsposition_teilsummeSteuer",
        sa_relationship_kwargs={"foreign_keys": "[Rechnungsposition.teilsummeSteuer_id]"},
    )
    zeitbezogeneMenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    zeitbezogeneMenge: "Menge" = Relationship(
        back_populates="rechnungsposition_zeitbezogeneMenge",
        sa_relationship_kwargs={"foreign_keys": "[Rechnungsposition.zeitbezogeneMenge_id]"},
    )
    zeiteinheit: Mengeneinheit | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="rechnungsposition_zusatzattribute_link",
        link_model=RechnungspositionzusatzAttributeLink,
    )
