import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.enum.vertragsart import Vertragsart
from ibims.orm.models.enum.vertragsstatus import Vertragsstatus
from ibims.orm.models.many import (
    BuendelvertrageinzelvertraegeLink,
    Buendelvertragunterzeichnervp1Link,
    Buendelvertragunterzeichnervp2Link,
    BuendelvertragvertragskonditionenLink,
    BuendelvertragzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.bo.vertrag import Vertrag
    from ibims.orm.models.com.unterschrift import Unterschrift
    from ibims.orm.models.com.vertragskonditionen import Vertragskonditionen
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Buendelvertrag(SQLModel, table=True):
    """
    Abbildung eines Bündelvertrags.
    Es handelt sich hierbei um eine Liste von Einzelverträgen, die in einem Vertragsobjekt gebündelt sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Buendelvertrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Buendelvertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Buendelvertrag.json>`_
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
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    """
    Beschreibung zum Vertrag
    """
    vertragsbeginn: datetime | None = Field(default=None, title="Vertragsbeginn")
    """
    Gibt an, wann der Vertrag beginnt (inklusiv)
    """
    vertragsende: datetime | None = Field(default=None, title="Vertragsende")
    """
    Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde (exklusiv)
    """
    vertragsnummer: str | None = Field(default=None, title="Vertragsnummer")
    """
    Eine im Verwendungskontext eindeutige Nummer für den Vertrag
    """
    buendelvertrag_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ | None = Field(Typ.BUENDELVERTRAG)
    einzelvertraege: List["Vertrag"] = Relationship(
        back_populates="buendelvertrag_einzelvertraege_link",
        link_model=BuendelvertrageinzelvertraegeLink,
    )
    sparte: Sparte | None = Field(None)
    unterzeichnervp1: List["Unterschrift"] = Relationship(
        back_populates="buendelvertrag_unterzeichnervp1_link",
        link_model=Buendelvertragunterzeichnervp1Link,
    )
    unterzeichnervp2: List["Unterschrift"] = Relationship(
        back_populates="buendelvertrag_unterzeichnervp2_link",
        link_model=Buendelvertragunterzeichnervp2Link,
    )
    vertragsart: Vertragsart | None = Field(None)
    vertragskonditionen: List["Vertragskonditionen"] = Relationship(
        back_populates="buendelvertrag_vertragskonditionen_link",
        link_model=BuendelvertragvertragskonditionenLink,
    )
    vertragspartner1_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    vertragspartner1: "Geschaeftspartner" = Relationship(
        back_populates="buendelvertrag_vertragspartner1",
        sa_relationship_kwargs={"foreign_keys": "[Buendelvertrag.vertragspartner1_id]"},
    )
    vertragspartner2_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    vertragspartner2: "Geschaeftspartner" = Relationship(
        back_populates="buendelvertrag_vertragspartner2",
        sa_relationship_kwargs={"foreign_keys": "[Buendelvertrag.vertragspartner2_id]"},
    )
    vertragsstatus: Vertragsstatus | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="buendelvertrag_zusatzattribute_link",
        link_model=BuendelvertragzusatzAttributeLink,
    )
