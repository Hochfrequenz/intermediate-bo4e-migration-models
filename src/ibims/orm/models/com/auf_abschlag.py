import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.auf_abschlagstyp import AufAbschlagstyp
from ibims.orm.models.enum.auf_abschlagsziel import AufAbschlagsziel
from ibims.orm.models.enum.waehrungseinheit import Waehrungseinheit
from ibims.orm.models.many import (
    AufAbschlagstaffelnLink,
    AufAbschlagzusatzAttributeLink,
    TarifpreisblatttarifAufAbschlaegeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.com.preisstaffel import Preisstaffel
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class AufAbschlag(SQLModel, table=True):
    """
    Modell für die preiserhöhenden (Aufschlag) bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen wurden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/AufAbschlag.json>`_
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
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    """
    Beschreibung zum Auf-/Abschlag
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung des Auf-/Abschlags
    """
    website: str | None = Field(default=None, title="Website")
    """
    Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind.
    """
    aufabschlag_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    tarifpreisblatt_tarifaufabschlaege_link: List["Tarifpreisblatt"] = Relationship(
        back_populates="tarifAufAbschlaege",
        link_model=TarifpreisblatttarifAufAbschlaegeLink,
    )
    aufAbschlagstyp: AufAbschlagstyp | None = Field(None)
    aufAbschlagsziel: AufAbschlagsziel | None = Field(None)
    einheit: Waehrungseinheit | None = Field(None)
    gueltigkeitszeitraum_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    gueltigkeitszeitraum: "Zeitraum" = Relationship(
        back_populates="aufabschlag_gueltigkeitszeitraum",
        sa_relationship_kwargs={"foreign_keys": "[AufAbschlag.gueltigkeitszeitraum_id]"},
    )
    staffeln: List["Preisstaffel"] = Relationship(
        back_populates="aufabschlag_staffeln_link", link_model=AufAbschlagstaffelnLink
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="aufabschlag_zusatzattribute_link",
        link_model=AufAbschlagzusatzAttributeLink,
    )
