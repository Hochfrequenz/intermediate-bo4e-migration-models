import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import ARRAY, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.auf_abschlagstyp import AufAbschlagstyp
from ibims.orm.models.enum.auf_abschlagsziel import AufAbschlagsziel
from ibims.orm.models.enum.waehrungseinheit import Waehrungseinheit
from ibims.orm.models.many import (
    RegionalerAufAbschlagstaffelnLink,
    RegionalerAufAbschlagzusatzAttributeLink,
    RegionaltariftarifAufAbschlaegeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.com.energiemix import Energiemix
    from ibims.orm.models.com.preisgarantie import Preisgarantie
    from ibims.orm.models.com.regionale_preisstaffel import RegionalePreisstaffel
    from ibims.orm.models.com.tarifeinschraenkung import Tarifeinschraenkung
    from ibims.orm.models.com.vertragskonditionen import Vertragskonditionen
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class RegionalerAufAbschlag(SQLModel, table=True):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang mit regionalen Gültigkeiten
    abgebildet werden.
    Hier sind auch die Auswirkungen auf verschiedene Tarifparameter modelliert, die sich durch die Auswahl eines Auf-
    oder Abschlags ergeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalerAufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalerAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/RegionalerAufAbschlag.json>`_
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
    Beschreibung des Auf-/Abschlags
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung des Auf-/Abschlags
    """
    tarifnamensaenderungen: str | None = Field(default=None, title="Tarifnamensaenderungen")
    """
    Durch die Anwendung des Auf/Abschlags kann eine Änderung des Tarifnamens auftreten
    """
    website: str | None = Field(default=None, title="Website")
    """
    Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind
    """
    regionaleraufabschlag_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    regionaltarif_tarifaufabschlaege_link: List["Regionaltarif"] = Relationship(
        back_populates="tarifAufAbschlaege",
        link_model=RegionaltariftarifAufAbschlaegeLink,
    )
    aufAbschlagstyp: AufAbschlagstyp | None = Field(None)
    aufAbschlagsziel: AufAbschlagsziel | None = Field(None)
    einheit: Waehrungseinheit | None = Field(None)
    einschraenkungsaenderung_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifeinschraenkung.tarifeinschraenkung_sqlid", ondelete="SET NULL"),
        )
    )
    einschraenkungsaenderung: "Tarifeinschraenkung" = Relationship(
        back_populates="regionaleraufabschlag_einschraenkungsaenderung",
        sa_relationship_kwargs={"foreign_keys": "[RegionalerAufAbschlag.einschraenkungsaenderung_id]"},
    )
    energiemixaenderung_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("energiemix.energiemix_sqlid", ondelete="SET NULL"),
        )
    )
    energiemixaenderung: "Energiemix" = Relationship(
        back_populates="regionaleraufabschlag_energiemixaenderung",
        sa_relationship_kwargs={"foreign_keys": "[RegionalerAufAbschlag.energiemixaenderung_id]"},
    )
    garantieaenderung_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisgarantie.preisgarantie_sqlid", ondelete="SET NULL"),
        )
    )
    garantieaenderung: "Preisgarantie" = Relationship(
        back_populates="regionaleraufabschlag_garantieaenderung",
        sa_relationship_kwargs={"foreign_keys": "[RegionalerAufAbschlag.garantieaenderung_id]"},
    )
    gueltigkeitszeitraum_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    gueltigkeitszeitraum: "Zeitraum" = Relationship(
        back_populates="regionaleraufabschlag_gueltigkeitszeitraum",
        sa_relationship_kwargs={"foreign_keys": "[RegionalerAufAbschlag.gueltigkeitszeitraum_id]"},
    )
    staffeln: List["RegionalePreisstaffel"] = Relationship(
        back_populates="regionaleraufabschlag_staffeln_link",
        link_model=RegionalerAufAbschlagstaffelnLink,
    )
    vertagskonditionsaenderung_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertragskonditionen.vertragskonditionen_sqlid", ondelete="SET NULL"),
        )
    )
    vertagskonditionsaenderung: "Vertragskonditionen" = Relationship(
        back_populates="regionaleraufabschlag_vertagskonditionsaenderung",
        sa_relationship_kwargs={"foreign_keys": "[RegionalerAufAbschlag.vertagskonditionsaenderung_id]"},
    )
    voraussetzungen: List[str] | None = Field(None, title="voraussetzungen", sa_column=Column(ARRAY(String)))
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="regionaleraufabschlag_zusatzattribute_link",
        link_model=RegionalerAufAbschlagzusatzAttributeLink,
    )
    zusatzprodukte: List[str] | None = Field(None, title="zusatzprodukte", sa_column=Column(ARRAY(String)))
