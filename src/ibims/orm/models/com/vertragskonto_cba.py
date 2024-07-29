import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.kontaktart import Kontaktart

if TYPE_CHECKING:
    from ibims.orm.models.bo.vertrag import Vertrag
    from ibims.orm.models.com.adresse import Adresse
    from ibims.orm.models.com.vertragskonto_mba import VertragskontoMBA


class VertragskontoCBA(SQLModel, table=True):
    """
    Models a CBA (child billing account) which directly relates to a single contract. It contains information about
    locks and billing dates. But in the first place, CBAs will be grouped together by the address in their contracts.
    For each group of CBAs with a common address there will be created an MBA (master billing
    account) to support that the invoices for the CBAs can be bundled into a single invoice for the MBA.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    ouid: int = Field(..., title="Ouid")
    vertragskontonummer: str = Field(..., title="Vertragskontonummer")
    erstellungsdatum: datetime = Field(..., title="Erstellungsdatum")
    enddatum: datetime | None = Field(default=None, title="Enddatum")
    rechnungsdatum_start: datetime = Field(..., alias="rechnungsdatumStart", title="Rechnungsdatumstart")
    rechnungsdatum_naechstes: datetime = Field(..., alias="rechnungsdatumNaechstes", title="Rechnungsdatumnaechstes")
    vertragskontocba_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    vertragsAdresse: "Adresse" = Relationship(
        back_populates="vertragskontocba_vertragsAdresse",
        sa_relationship_kwargs={"foreign_keys": "[VertragskontoCBA.vertragsAdresse_id]"},
    )
    vertragsAdresse_id: uuid_pkg.UUID = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("adresse.adresse_sqlid", ondelete="SET NULL"))
    )
    rechnungsstellung: Kontaktart = Field(None)
    vertrag: "Vertrag" = Relationship(
        back_populates="vertragskontocba_vertrag",
        sa_relationship_kwargs={"foreign_keys": "[VertragskontoCBA.vertrag_id]"},
    )
    vertrag_id: uuid_pkg.UUID = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("vertrag.vertrag_sqlid", ondelete="SET NULL"))
    )
    vertragskontomba_cbas: List["VertragskontoMBA"] = Relationship(
        back_populates="cbas",
        sa_relationship_kwargs={
            "primaryjoin": "VertragskontoMBA.cbas_id==VertragskontoCBA.vertragskontocba_sqlid",
            "lazy": "joined",
        },
    )
