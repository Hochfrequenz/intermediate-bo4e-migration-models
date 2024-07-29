import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import ARRAY, Column, Enum, String
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.voraussetzungen import Voraussetzungen
from ibims.orm.models.many import (
    TarifeinschraenkungeinschraenkungleistungLink,
    TarifeinschraenkungeinschraenkungzaehlerLink,
    TarifeinschraenkungzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.geraet import Geraet
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.bo.tarif import Tarif
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.com.auf_abschlag_regional import AufAbschlagRegional
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.com.regionaler_auf_abschlag import RegionalerAufAbschlag
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Tarifeinschraenkung(SQLModel, table=True):
    """
    Mit dieser Komponente werden Einschränkungen für die Anwendung von Tarifen modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifeinschraenkung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifeinschraenkung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Tarifeinschraenkung.json>`_
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
    tarifeinschraenkung_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    regionaltarif_tarifeinschraenkung: List["Regionaltarif"] = Relationship(
        back_populates="tarifeinschraenkung",
        sa_relationship_kwargs={
            "primaryjoin": "Regionaltarif.tarifeinschraenkung_id==Tarifeinschraenkung.tarifeinschraenkung_sqlid",
            "lazy": "joined",
        },
    )
    tarif_tarifeinschraenkung: List["Tarif"] = Relationship(
        back_populates="tarifeinschraenkung",
        sa_relationship_kwargs={
            "primaryjoin": "Tarif.tarifeinschraenkung_id==Tarifeinschraenkung.tarifeinschraenkung_sqlid",
            "lazy": "joined",
        },
    )
    tarifpreisblatt_tarifeinschraenkung: List["Tarifpreisblatt"] = Relationship(
        back_populates="tarifeinschraenkung",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifpreisblatt.tarifeinschraenkung_id==Tarifeinschraenkung.tarifeinschraenkung_sqlid",
            "lazy": "joined",
        },
    )
    aufabschlagregional_einschraenkungsaenderung: List["AufAbschlagRegional"] = Relationship(
        back_populates="einschraenkungsaenderung",
        sa_relationship_kwargs={
            "primaryjoin": "AufAbschlagRegional.einschraenkungsaenderung_id==Tarifeinschraenkung.tarifeinschraenkung_sqlid",
            "lazy": "joined",
        },
    )
    regionaleraufabschlag_einschraenkungsaenderung: List["RegionalerAufAbschlag"] = Relationship(
        back_populates="einschraenkungsaenderung",
        sa_relationship_kwargs={
            "primaryjoin": "RegionalerAufAbschlag.einschraenkungsaenderung_id==Tarifeinschraenkung.tarifeinschraenkung_sqlid",
            "lazy": "joined",
        },
    )
    einschraenkungleistung: List["Menge"] = Relationship(
        back_populates="tarifeinschraenkung_einschraenkungleistung_link",
        link_model=TarifeinschraenkungeinschraenkungleistungLink,
    )
    einschraenkungzaehler: List["Geraet"] = Relationship(
        back_populates="tarifeinschraenkung_einschraenkungzaehler_link",
        link_model=TarifeinschraenkungeinschraenkungzaehlerLink,
    )
    voraussetzungen: List[Voraussetzungen] | None = Field(
        None, sa_column=Column(ARRAY(Enum(Voraussetzungen, name="voraussetzungen")))
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="tarifeinschraenkung_zusatzattribute_link",
        link_model=TarifeinschraenkungzusatzAttributeLink,
    )
    zusatzprodukte: List[str] | None = Field(None, title="zusatzprodukte", sa_column=Column(ARRAY(String)))
