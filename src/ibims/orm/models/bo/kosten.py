import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.kostenklasse import Kostenklasse
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import KostenkostenbloeckeLink, KostensummeKostenLink, KostenzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.tarifkosten import Tarifkosten
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.kostenblock import Kostenblock
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Kosten(SQLModel, table=True):
    """
    Dieses BO wird zur Übertagung von hierarchischen Kostenstrukturen verwendet.
    Die Kosten werden dabei in Kostenblöcke und diese wiederum in Kostenpositionen strukturiert.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Kosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Kosten.json>`_
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
    kosten_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ | None = Field(Typ.KOSTEN)
    gueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    gueltigkeit: "Zeitraum" = Relationship(
        back_populates="kosten_gueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[Kosten.gueltigkeit_id]"},
    )
    kostenbloecke: List["Kostenblock"] = Relationship(
        back_populates="kosten_kostenbloecke_link", link_model=KostenkostenbloeckeLink
    )
    kostenklasse: Kostenklasse | None = Field(None)
    summeKosten: List["Betrag"] = Relationship(
        back_populates="kosten_summekosten_link", link_model=KostensummeKostenLink
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="kosten_zusatzattribute_link",
        link_model=KostenzusatzAttributeLink,
    )
    tarifkosten_kosten: List["Tarifkosten"] = Relationship(
        back_populates="kosten",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifkosten.kosten_id==Kosten.kosten_sqlid",
            "lazy": "joined",
        },
    )
