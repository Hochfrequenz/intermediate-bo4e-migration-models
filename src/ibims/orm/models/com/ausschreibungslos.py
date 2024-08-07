import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.preismodell import Preismodell
from ibims.orm.models.enum.rechnungslegung import Rechnungslegung
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.vertragsform import Vertragsform
from ibims.orm.models.many import (
    AusschreibungloseLink,
    AusschreibungsloslieferstellenLink,
    AusschreibungsloszusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.ausschreibung import Ausschreibung
    from ibims.orm.models.com.ausschreibungsdetail import Ausschreibungsdetail
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Ausschreibungslos(SQLModel, table=True):
    """
    Eine Komponente zur Abbildung einzelner Lose einer Ausschreibung

    .. raw:: html

        <object data="../_static/images/bo4e/com/Ausschreibungslos.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibungslos JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Ausschreibungslos.json>`_
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
    anzahl_lieferstellen: int | None = Field(default=None, alias="anzahlLieferstellen", title="Anzahllieferstellen")
    """
    Anzahl der Lieferstellen in dieser Ausschreibung
    """
    bemerkung: str | None = Field(default=None, title="Bemerkung")
    """
    Bemerkung des Kunden zum Los
    """
    betreut_durch: str | None = Field(default=None, alias="betreutDurch", title="Betreutdurch")
    """
    Name des Lizenzpartners
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung der Ausschreibung
    """
    losnummer: str | None = Field(default=None, title="Losnummer")
    """
    Laufende Nummer des Loses
    """
    ausschreibungslos_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    ausschreibung_lose_link: List["Ausschreibung"] = Relationship(
        back_populates="lose", link_model=AusschreibungloseLink
    )
    energieart: Sparte | None = Field(None)
    gesamtMenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    gesamtMenge: "Menge" = Relationship(
        back_populates="ausschreibungslos_gesamtMenge",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungslos.gesamtMenge_id]"},
    )
    lieferstellen: List["Ausschreibungsdetail"] = Relationship(
        back_populates="ausschreibungslos_lieferstellen_link",
        link_model=AusschreibungsloslieferstellenLink,
    )
    lieferzeitraum_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    lieferzeitraum: "Zeitraum" = Relationship(
        back_populates="ausschreibungslos_lieferzeitraum",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungslos.lieferzeitraum_id]"},
    )
    preismodell: Preismodell | None = Field(None)
    wiederholungsintervall_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    wiederholungsintervall: "Zeitraum" = Relationship(
        back_populates="ausschreibungslos_wiederholungsintervall",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungslos.wiederholungsintervall_id]"},
    )
    wunschKuendingungsfrist_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    wunschKuendingungsfrist: "Zeitraum" = Relationship(
        back_populates="ausschreibungslos_wunschKuendingungsfrist",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungslos.wunschKuendingungsfrist_id]"},
    )
    wunschMaximalmenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    wunschMaximalmenge: "Menge" = Relationship(
        back_populates="ausschreibungslos_wunschMaximalmenge",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungslos.wunschMaximalmenge_id]"},
    )
    wunschMindestmenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    wunschMindestmenge: "Menge" = Relationship(
        back_populates="ausschreibungslos_wunschMindestmenge",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungslos.wunschMindestmenge_id]"},
    )
    wunschRechnungslegung: Rechnungslegung | None = Field(None)
    wunschVertragsform: Vertragsform | None = Field(None)
    wunschZahlungsziel_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    wunschZahlungsziel: "Zeitraum" = Relationship(
        back_populates="ausschreibungslos_wunschZahlungsziel",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungslos.wunschZahlungsziel_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="ausschreibungslos_zusatzattribute_link",
        link_model=AusschreibungsloszusatzAttributeLink,
    )
