import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.messpreistyp import Messpreistyp
from ibims.orm.models.enum.tarifkalkulationsmethode import Tarifkalkulationsmethode
from ibims.orm.models.many import (
    TarifberechnungsparameterzusatzAttributeLink,
    TarifberechnungsparameterzusatzpreiseLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.bo.tarif import Tarif
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.com.preis import Preis
    from ibims.orm.models.com.tarifpreis import Tarifpreis
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Tarifberechnungsparameter(SQLModel, table=True):
    """
    In dieser Komponente sind die Berechnungsparameter für die Ermittlung der Tarifkosten zusammengefasst.
    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifberechnungsparameter.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifberechnungsparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Tarifberechnungsparameter.json>`_
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
    ist_messpreis_in_grundpreis_enthalten: bool | None = Field(
        default=None,
        alias="istMesspreisInGrundpreisEnthalten",
        title="Istmesspreisingrundpreisenthalten",
    )
    """
    True, falls der Messpreis im Grundpreis (GP) enthalten ist
    """
    ist_messpreis_zu_beruecksichtigen: bool | None = Field(
        default=None,
        alias="istMesspreisZuBeruecksichtigen",
        title="Istmesspreiszuberuecksichtigen",
    )
    """
    Typ des Messpreises
    """
    kw_inklusive: float | None = Field(default=None, alias="kwInklusive", title="Kwinklusive")
    """
    Im Preis bereits eingeschlossene Leistung (für Gas)
    """
    kw_weitere_mengen: float | None = Field(default=None, alias="kwWeitereMengen", title="Kwweiteremengen")
    """
    Intervall, indem die über "kwInklusive" hinaus abgenommene Leistung kostenpflichtig wird (z.B. je 5 kW 20 EURO)
    """
    tarifberechnungsparameter_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    regionaltarif_berechnungsparameter: List["Regionaltarif"] = Relationship(
        back_populates="berechnungsparameter",
        sa_relationship_kwargs={
            "primaryjoin": "Regionaltarif.berechnungsparameter_id==Tarifberechnungsparameter.tarifberechnungsparameter_sqlid",
            "lazy": "joined",
        },
    )
    tarif_berechnungsparameter: List["Tarif"] = Relationship(
        back_populates="berechnungsparameter",
        sa_relationship_kwargs={
            "primaryjoin": "Tarif.berechnungsparameter_id==Tarifberechnungsparameter.tarifberechnungsparameter_sqlid",
            "lazy": "joined",
        },
    )
    tarifpreisblatt_berechnungsparameter: List["Tarifpreisblatt"] = Relationship(
        back_populates="berechnungsparameter",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifpreisblatt.berechnungsparameter_id==Tarifberechnungsparameter.tarifberechnungsparameter_sqlid",
            "lazy": "joined",
        },
    )
    berechnungsmethode: Tarifkalkulationsmethode | None = Field(None)
    hoechstpreisHT_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("preis.preis_sqlid", ondelete="SET NULL"))
    )
    hoechstpreisHT: "Preis" = Relationship(
        back_populates="tarifberechnungsparameter_hoechstpreisHT",
        sa_relationship_kwargs={"foreign_keys": "[Tarifberechnungsparameter.hoechstpreisHT_id]"},
    )
    hoechstpreisNT_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("preis.preis_sqlid", ondelete="SET NULL"))
    )
    hoechstpreisNT: "Preis" = Relationship(
        back_populates="tarifberechnungsparameter_hoechstpreisNT",
        sa_relationship_kwargs={"foreign_keys": "[Tarifberechnungsparameter.hoechstpreisNT_id]"},
    )
    messpreistyp: Messpreistyp | None = Field(None)
    mindestpreis_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("preis.preis_sqlid", ondelete="SET NULL"))
    )
    mindestpreis: "Preis" = Relationship(
        back_populates="tarifberechnungsparameter_mindestpreis",
        sa_relationship_kwargs={"foreign_keys": "[Tarifberechnungsparameter.mindestpreis_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="tarifberechnungsparameter_zusatzattribute_link",
        link_model=TarifberechnungsparameterzusatzAttributeLink,
    )
    zusatzpreise: List["Tarifpreis"] = Relationship(
        back_populates="tarifberechnungsparameter_zusatzpreise_link",
        link_model=TarifberechnungsparameterzusatzpreiseLink,
    )
