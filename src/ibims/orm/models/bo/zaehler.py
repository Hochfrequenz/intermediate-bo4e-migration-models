import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.befestigungsart import Befestigungsart
from ibims.orm.models.enum.messwerterfassung import Messwerterfassung
from ibims.orm.models.enum.registeranzahl import Registeranzahl
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.enum.zaehlerauspraegung import Zaehlerauspraegung
from ibims.orm.models.enum.zaehlergroesse import Zaehlergroesse
from ibims.orm.models.enum.zaehlertyp import Zaehlertyp
from ibims.orm.models.enum.zaehlertyp_spezifikation import ZaehlertypSpezifikation
from ibims.orm.models.many import (
    MesslokationmesslokationszaehlerLink,
    ZaehlergeraeteLink,
    ZaehlerzaehlwerkeLink,
    ZaehlerzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.geraet import Geraet
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.bo.messlokation import Messlokation
    from ibims.orm.models.bo.preisblatt_messung import PreisblattMessung
    from ibims.orm.models.com.zaehlwerk import Zaehlwerk
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Zaehler(SQLModel, table=True):
    """
    Object containing information about a meter/"Zaehler".

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zaehler.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehler JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Zaehler.json>`_
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
    eichung_bis: datetime | None = Field(default=None, alias="eichungBis", title="Eichungbis")
    """
    Zählerkonstante auf dem Zähler
    """
    ist_fernschaltbar: bool | None = Field(default=None, alias="istFernschaltbar", title="Istfernschaltbar")
    """
    Der Hersteller des Zählers
    """
    letzte_eichung: datetime | None = Field(default=None, alias="letzteEichung", title="Letzteeichung")
    """
    Bis zu diesem Datum (exklusiv) ist der Zähler geeicht.
    """
    zaehlerkonstante: float | None = Field(default=None, title="Zaehlerkonstante")
    """
    Spezifikation bezüglich unterstützter Tarif
    """
    zaehlernummer: str | None = Field(default=None, title="Zaehlernummer")
    """
    Nummerierung des Zählers,vergeben durch den Messstellenbetreiber
    """
    nachstes_ablesedatum: datetime | None = Field(
        default=None, alias="nachstesAblesedatum", title="Nachstesablesedatum"
    )
    zaehler_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    messlokation_messlokationszaehler_link: List["Messlokation"] = Relationship(
        back_populates="messlokationszaehler",
        link_model=MesslokationmesslokationszaehlerLink,
    )
    preisblattmessung_zaehler: List["PreisblattMessung"] = Relationship(
        back_populates="zaehler",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattMessung.zaehler_id==Zaehler.zaehler_sqlid",
            "lazy": "joined",
        },
    )
    typ: Typ | None = Field(Typ.ZAEHLER)
    befestigungsart: Befestigungsart | None = Field(None)
    geraete: List["Geraet"] = Relationship(back_populates="zaehler_geraete_link", link_model=ZaehlergeraeteLink)
    messwerterfassung: Messwerterfassung | None = Field(None)
    registeranzahl: Registeranzahl | None = Field(None)
    sparte: Sparte | None = Field(None)
    zaehlerauspraegung: Zaehlerauspraegung | None = Field(None)
    zaehlergroesse: Zaehlergroesse | None = Field(None)
    zaehlerhersteller_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    zaehlerhersteller: "Geschaeftspartner" = Relationship(
        back_populates="zaehler_zaehlerhersteller",
        sa_relationship_kwargs={"foreign_keys": "[Zaehler.zaehlerhersteller_id]"},
    )
    zaehlertyp: Zaehlertyp | None = Field(None)
    zaehlertypSpezifikation: ZaehlertypSpezifikation | None = Field(None)
    zaehlwerke: List["Zaehlwerk"] = Relationship(
        back_populates="zaehler_zaehlwerke_link", link_model=ZaehlerzaehlwerkeLink
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="zaehler_zusatzattribute_link",
        link_model=ZaehlerzusatzAttributeLink,
    )
    aktiverZeitraum_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    aktiverZeitraum: "Zeitraum" = Relationship(
        back_populates="zaehler_aktiverZeitraum",
        sa_relationship_kwargs={"foreign_keys": "[Zaehler.aktiverZeitraum_id]"},
    )
