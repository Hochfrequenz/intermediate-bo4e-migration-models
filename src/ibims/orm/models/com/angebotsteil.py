import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import (
    AngebotsteillieferstellenangebotsteilLink,
    AngebotsteilpositionenLink,
    AngebotsteilzusatzAttributeLink,
    AngebotsvarianteteileLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.com.angebotsposition import Angebotsposition
    from ibims.orm.models.com.angebotsvariante import Angebotsvariante
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Angebotsteil(SQLModel, table=True):
    """
    Mit dieser Komponente wird ein Teil einer Angebotsvariante abgebildet.
    Hier werden alle Angebotspositionen aggregiert.
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsteil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Angebotsteil.json>`_
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
    anfrage_subreferenz: str | None = Field(default=None, alias="anfrageSubreferenz", title="Anfragesubreferenz")
    """
    Identifizierung eines Subkapitels einer Anfrage, beispielsweise das Los einer Ausschreibung
    """
    angebotsteil_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    gesamtkostenangebotsteil_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    gesamtkostenangebotsteil: "Betrag" = Relationship(
        back_populates="angebotsteil_gesamtkostenangebotsteil",
        sa_relationship_kwargs={"foreign_keys": "[Angebotsteil.gesamtkostenangebotsteil_id]"},
    )
    gesamtmengeangebotsteil_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    gesamtmengeangebotsteil: "Menge" = Relationship(
        back_populates="angebotsteil_gesamtmengeangebotsteil",
        sa_relationship_kwargs={"foreign_keys": "[Angebotsteil.gesamtmengeangebotsteil_id]"},
    )
    lieferstellenangebotsteil: List["Marktlokation"] = Relationship(
        back_populates="angebotsteil_lieferstellenangebotsteil_link",
        link_model=AngebotsteillieferstellenangebotsteilLink,
    )
    lieferzeitraum_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    lieferzeitraum: "Zeitraum" = Relationship(
        back_populates="angebotsteil_lieferzeitraum",
        sa_relationship_kwargs={"foreign_keys": "[Angebotsteil.lieferzeitraum_id]"},
    )
    positionen: List["Angebotsposition"] = Relationship(
        back_populates="angebotsteil_positionen_link",
        link_model=AngebotsteilpositionenLink,
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="angebotsteil_zusatzattribute_link",
        link_model=AngebotsteilzusatzAttributeLink,
    )
    angebotsvariante_teile_link: List["Angebotsvariante"] = Relationship(
        back_populates="teile", link_model=AngebotsvarianteteileLink
    )
