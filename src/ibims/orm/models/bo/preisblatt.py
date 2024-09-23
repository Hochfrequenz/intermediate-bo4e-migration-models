import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.preisstatus import Preisstatus
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import PreisblattpreispositionenLink, PreisblattzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.marktteilnehmer import Marktteilnehmer
    from ibims.orm.models.com.preisposition import Preisposition
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Preisblatt(SQLModel, table=True):
    """
    Das allgemeine Modell zur Abbildung von Preisen;
    Davon abgeleitet können, über die Zuordnung identifizierender Merkmale, spezielle Preisblatt-Varianten modelliert
    werden.

    Die jeweiligen Sätze von Merkmalen sind in der Grafik ergänzt worden und stellen jeweils eine Ausprägung für die
    verschiedenen Anwendungsfälle der Preisblätter dar.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Preisblatt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Preisblatt.json>`_
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
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Eine Bezeichnung für das Preisblatt
    """
    preisblatt_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ | None = Field(Typ.PREISBLATT)
    gueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    gueltigkeit: "Zeitraum" = Relationship(
        back_populates="preisblatt_gueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[Preisblatt.gueltigkeit_id]"},
    )
    herausgeber_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktteilnehmer.marktteilnehmer_sqlid", ondelete="SET NULL"),
        )
    )
    herausgeber: "Marktteilnehmer" = Relationship(
        back_populates="preisblatt_herausgeber",
        sa_relationship_kwargs={"foreign_keys": "[Preisblatt.herausgeber_id]"},
    )
    preispositionen: List["Preisposition"] = Relationship(
        back_populates="preisblatt_preispositionen_link",
        link_model=PreisblattpreispositionenLink,
    )
    preisstatus: Preisstatus | None = Field(None)
    sparte: Sparte | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="preisblatt_zusatzattribute_link",
        link_model=PreisblattzusatzAttributeLink,
    )
