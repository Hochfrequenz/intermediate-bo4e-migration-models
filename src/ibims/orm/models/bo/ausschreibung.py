import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.ausschreibungsportal import Ausschreibungsportal
from ibims.orm.models.enum.ausschreibungsstatus import Ausschreibungsstatus
from ibims.orm.models.enum.ausschreibungstyp import Ausschreibungstyp
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import AusschreibungloseLink, AusschreibungzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.com.ausschreibungslos import Ausschreibungslos
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Ausschreibung(SQLModel, table=True):
    """
    Das BO Ausschreibung dient zur detaillierten Darstellung von ausgeschriebenen Energiemengen in der Energiewirtschaft

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Ausschreibung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Ausschreibung.json>`_
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
    ausschreibungsnummer: str | None = Field(default=None, title="Ausschreibungsnummer")
    """
    Vom Herausgeber der Ausschreibung vergebene eindeutige Nummer
    """
    ist_kostenpflichtig: bool | None = Field(default=None, alias="istKostenpflichtig", title="Istkostenpflichtig")
    """
    Kennzeichen, ob die Ausschreibung kostenpflichtig ist
    """
    veroeffentlichungszeitpunkt: datetime | None = Field(default=None, title="Veroeffentlichungszeitpunkt")
    """
    Gibt den Veröffentlichungszeitpunkt der Ausschreibung an
    """
    webseite: str | None = Field(default=None, title="Webseite")
    """
    Internetseite, auf der die Ausschreibung veröffentlicht wurde (falls vorhanden)
    """
    ausschreibung_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ | None = Field(Typ.AUSSCHREIBUNG)
    abgabefrist_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    abgabefrist: "Zeitraum" = Relationship(
        back_populates="ausschreibung_abgabefrist",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibung.abgabefrist_id]"},
    )
    ausschreibender_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    ausschreibender: "Geschaeftspartner" = Relationship(
        back_populates="ausschreibung_ausschreibender",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibung.ausschreibender_id]"},
    )
    ausschreibungportal: Ausschreibungsportal | None = Field(None)
    ausschreibungsstatus: Ausschreibungsstatus | None = Field(None)
    ausschreibungstyp: Ausschreibungstyp | None = Field(None)
    bindefrist_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    bindefrist: "Zeitraum" = Relationship(
        back_populates="ausschreibung_bindefrist",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibung.bindefrist_id]"},
    )
    lose: List["Ausschreibungslos"] = Relationship(
        back_populates="ausschreibung_lose_link", link_model=AusschreibungloseLink
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="ausschreibung_zusatzattribute_link",
        link_model=AusschreibungzusatzAttributeLink,
    )
