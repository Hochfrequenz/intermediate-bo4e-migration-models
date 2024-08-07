import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import AngebotspositionzusatzAttributeLink, AngebotsteilpositionenLink

if TYPE_CHECKING:
    from ibims.orm.models.com.angebotsteil import Angebotsteil
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.com.preis import Preis
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Angebotsposition(SQLModel, table=True):
    """
    Unterhalb von Angebotsteilen sind die Angebotspositionen eingebunden.
    Hier werden die angebotenen Bestandteile einzeln aufgeführt. Beispiel:
    Positionsmenge: 4000 kWh
    Positionspreis: 24,56 ct/kWh
    Positionskosten: 982,40 EUR

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Angebotsposition.json>`_
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
    positionsbezeichnung: str | None = Field(default=None, title="Positionsbezeichnung")
    """
    Bezeichnung der jeweiligen Position des Angebotsteils
    """
    angebotsposition_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    positionskosten_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    positionskosten: "Betrag" = Relationship(
        back_populates="angebotsposition_positionskosten",
        sa_relationship_kwargs={"foreign_keys": "[Angebotsposition.positionskosten_id]"},
    )
    positionsmenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    positionsmenge: "Menge" = Relationship(
        back_populates="angebotsposition_positionsmenge",
        sa_relationship_kwargs={"foreign_keys": "[Angebotsposition.positionsmenge_id]"},
    )
    positionspreis_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("preis.preis_sqlid", ondelete="SET NULL"))
    )
    positionspreis: "Preis" = Relationship(
        back_populates="angebotsposition_positionspreis",
        sa_relationship_kwargs={"foreign_keys": "[Angebotsposition.positionspreis_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="angebotsposition_zusatzattribute_link",
        link_model=AngebotspositionzusatzAttributeLink,
    )
    angebotsteil_positionen_link: List["Angebotsteil"] = Relationship(
        back_populates="positionen", link_model=AngebotsteilpositionenLink
    )
