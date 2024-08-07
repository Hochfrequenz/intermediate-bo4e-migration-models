import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.angebotsstatus import Angebotsstatus
from ibims.orm.models.many import AngebotsvarianteteileLink, AngebotsvariantezusatzAttributeLink, AngebotvariantenLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.angebot import Angebot
    from ibims.orm.models.com.angebotsteil import Angebotsteil
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Angebotsvariante(SQLModel, table=True):
    """
    Führt die verschiedenen Ausprägungen der Angebotsberechnung auf

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsvariante.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsvariante JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Angebotsvariante.json>`_
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
    bindefrist: datetime | None = Field(default=None, title="Bindefrist")
    """
    Bis zu diesem Zeitpunkt gilt die Angebotsvariante
    """
    erstellungsdatum: datetime | None = Field(default=None, title="Erstellungsdatum")
    """
    Datum der Erstellung der Angebotsvariante
    """
    angebotsvariante_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    angebot_varianten_link: List["Angebot"] = Relationship(back_populates="varianten", link_model=AngebotvariantenLink)
    angebotsstatus: Angebotsstatus | None = Field(None)
    gesamtkosten_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    gesamtkosten: "Betrag" = Relationship(
        back_populates="angebotsvariante_gesamtkosten",
        sa_relationship_kwargs={"foreign_keys": "[Angebotsvariante.gesamtkosten_id]"},
    )
    gesamtmenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    gesamtmenge: "Menge" = Relationship(
        back_populates="angebotsvariante_gesamtmenge",
        sa_relationship_kwargs={"foreign_keys": "[Angebotsvariante.gesamtmenge_id]"},
    )
    teile: List["Angebotsteil"] = Relationship(
        back_populates="angebotsvariante_teile_link",
        link_model=AngebotsvarianteteileLink,
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="angebotsvariante_zusatzattribute_link",
        link_model=AngebotsvariantezusatzAttributeLink,
    )
