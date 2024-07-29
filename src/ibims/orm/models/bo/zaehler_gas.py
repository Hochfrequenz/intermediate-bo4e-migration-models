import uuid as uuid_pkg
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.messwerterfassung import Messwerterfassung
from ibims.orm.models.enum.netzebene import Netzebene
from ibims.orm.models.enum.registeranzahl import Registeranzahl
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.enum.zaehlerauspraegung import Zaehlerauspraegung
from ibims.orm.models.enum.zaehlergroesse import Zaehlergroesse
from ibims.orm.models.enum.zaehlertyp import Zaehlertyp
from ibims.orm.models.many import ZaehlerGaszaehlwerkeLink, ZaehlerGaszusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.com.zaehlwerk import Zaehlwerk
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class ZaehlerGas(SQLModel, table=True):
    """
    Resolve some ambiguity of `Strom` and `Gas`
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    id: str | None = Field(default=None, alias="_id", title=" Id")
    zaehlernummer: str | None = Field(default=None, title="Zaehlernummer")
    zaehlerkonstante: Decimal | None = Field(default=None, title="Zaehlerkonstante")
    eichung_bis: datetime | None = Field(default=None, alias="eichungBis", title="Eichungbis")
    letzte_eichung: datetime | None = Field(default=None, alias="letzteEichung", title="Letzteeichung")
    nachstes_ablesedatum: datetime | None = Field(
        default=None, alias="nachstesAblesedatum", title="Nachstesablesedatum"
    )
    zaehlergas_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ = Field(Typ.ZAEHLERGAS)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="zaehlergas_zusatzattribute_link",
        link_model=ZaehlerGaszusatzAttributeLink,
    )
    sparte: Sparte | None = Field(None)
    zaehlerauspraegung: Zaehlerauspraegung | None = Field(None)
    zaehlertyp: Zaehlertyp = Field(None)
    zaehlwerke: List["Zaehlwerk"] = Relationship(
        back_populates="zaehlergas_zaehlwerke_link", link_model=ZaehlerGaszaehlwerkeLink
    )
    registeranzahl: Registeranzahl | None = Field(None)
    zaehlerhersteller_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    zaehlerhersteller: "Geschaeftspartner" = Relationship(
        back_populates="zaehlergas_zaehlerhersteller",
        sa_relationship_kwargs={"foreign_keys": "[ZaehlerGas.zaehlerhersteller_id]"},
    )
    messwerterfassung: Messwerterfassung = Field(None)
    aktiverZeitraum_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    aktiverZeitraum: "Zeitraum" = Relationship(
        back_populates="zaehlergas_aktiverZeitraum",
        sa_relationship_kwargs={"foreign_keys": "[ZaehlerGas.aktiverZeitraum_id]"},
    )
    zaehlergroesse: Zaehlergroesse = Field(None)
    druckniveau: Netzebene = Field(None)
