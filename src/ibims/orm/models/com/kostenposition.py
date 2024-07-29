import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import KostenblockkostenpositionenLink, KostenpositionzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.kostenblock import Kostenblock
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.com.preis import Preis
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Kostenposition(SQLModel, table=True):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Kostenposition verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Kostenposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kostenposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Kostenposition.json>`_
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
    artikelbezeichnung: str | None = Field(default=None, title="Artikelbezeichnung")
    """
    Bezeichnung für den Artikel für den die Kosten ermittelt wurden. Beispiel: Arbeitspreis HT
    """
    artikeldetail: str | None = Field(default=None, title="Artikeldetail")
    """
    Detaillierung des Artikels (optional). Beispiel: 'Drehstromzähler'
    """
    bis: datetime | None = Field(default=None, title="Bis")
    """
    exklusiver bis-Zeitpunkt der Kostenzeitscheibe
    """
    positionstitel: str | None = Field(default=None, title="Positionstitel")
    """
    Ein Titel für die Zeile. Hier kann z.B. der Netzbetreiber eingetragen werden, wenn es sich um Netzkosten handelt.
    """
    von: datetime | None = Field(default=None, title="Von")
    """
    inklusiver von-Zeitpunkt der Kostenzeitscheibe
    """
    kostenposition_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    kostenblock_kostenpositionen_link: List["Kostenblock"] = Relationship(
        back_populates="kostenpositionen", link_model=KostenblockkostenpositionenLink
    )
    betragKostenposition_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    betragKostenposition: "Betrag" = Relationship(
        back_populates="kostenposition_betragKostenposition",
        sa_relationship_kwargs={"foreign_keys": "[Kostenposition.betragKostenposition_id]"},
    )
    einzelpreis_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("preis.preis_sqlid", ondelete="SET NULL"))
    )
    einzelpreis: "Preis" = Relationship(
        back_populates="kostenposition_einzelpreis",
        sa_relationship_kwargs={"foreign_keys": "[Kostenposition.einzelpreis_id]"},
    )
    menge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    menge: "Menge" = Relationship(
        back_populates="kostenposition_menge",
        sa_relationship_kwargs={"foreign_keys": "[Kostenposition.menge_id]"},
    )
    zeitmenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    zeitmenge: "Menge" = Relationship(
        back_populates="kostenposition_zeitmenge",
        sa_relationship_kwargs={"foreign_keys": "[Kostenposition.zeitmenge_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="kostenposition_zusatzattribute_link",
        link_model=KostenpositionzusatzAttributeLink,
    )
