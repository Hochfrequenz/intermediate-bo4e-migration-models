import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import FremdkostenkostenbloeckeLink, FremdkostenzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.fremdkostenblock import Fremdkostenblock
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Fremdkosten(SQLModel, table=True):
    """
    Mit diesem BO werden die Fremdkosten, beispielsweise für eine Angebotserstellung oder eine Rechnungsprüfung,
    übertragen.
    Die Fremdkosten enthalten dabei alle Kostenblöcke, die von anderen Marktteilnehmern oder Instanzen erhoben werden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Fremdkosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Fremdkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Fremdkosten.json>`_
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
    fremdkosten_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ | None = Field(Typ.FREMDKOSTEN)
    gueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    gueltigkeit: "Zeitraum" = Relationship(
        back_populates="fremdkosten_gueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[Fremdkosten.gueltigkeit_id]"},
    )
    kostenbloecke: List["Fremdkostenblock"] = Relationship(
        back_populates="fremdkosten_kostenbloecke_link",
        link_model=FremdkostenkostenbloeckeLink,
    )
    summeKosten_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    summeKosten: "Betrag" = Relationship(
        back_populates="fremdkosten_summeKosten",
        sa_relationship_kwargs={"foreign_keys": "[Fremdkosten.summeKosten_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="fremdkosten_zusatzattribute_link",
        link_model=FremdkostenzusatzAttributeLink,
    )
