import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.enum.preisstatus import Preisstatus
from ibims.orm.models.enum.waehrungseinheit import Waehrungseinheit
from ibims.orm.models.many import PreiszusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.angebotsposition import Angebotsposition
    from ibims.orm.models.com.fremdkostenposition import Fremdkostenposition
    from ibims.orm.models.com.kostenposition import Kostenposition
    from ibims.orm.models.com.rechnungsposition import Rechnungsposition
    from ibims.orm.models.com.tarifberechnungsparameter import Tarifberechnungsparameter
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Preis(SQLModel, table=True):
    """
    Abbildung eines Preises mit Wert, Einheit, Bezugswert und Status.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Preis.json>`_
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
    wert: float | None = Field(default=None, title="Wert")
    """
    Gibt die nominale Höhe des Preises an.
    """
    preis_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    angebotsposition_positionspreis: List["Angebotsposition"] = Relationship(
        back_populates="positionspreis",
        sa_relationship_kwargs={
            "primaryjoin": "Angebotsposition.positionspreis_id==Preis.preis_sqlid",
            "lazy": "joined",
        },
    )
    fremdkostenposition_einzelpreis: List["Fremdkostenposition"] = Relationship(
        back_populates="einzelpreis",
        sa_relationship_kwargs={
            "primaryjoin": "Fremdkostenposition.einzelpreis_id==Preis.preis_sqlid",
            "lazy": "joined",
        },
    )
    kostenposition_einzelpreis: List["Kostenposition"] = Relationship(
        back_populates="einzelpreis",
        sa_relationship_kwargs={
            "primaryjoin": "Kostenposition.einzelpreis_id==Preis.preis_sqlid",
            "lazy": "joined",
        },
    )
    bezugswert: Mengeneinheit | None = Field(None)
    einheit: Waehrungseinheit | None = Field(None)
    status: Preisstatus | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="preis_zusatzattribute_link", link_model=PreiszusatzAttributeLink
    )
    rechnungsposition_einzelpreis: List["Rechnungsposition"] = Relationship(
        back_populates="einzelpreis",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnungsposition.einzelpreis_id==Preis.preis_sqlid",
            "lazy": "joined",
        },
    )
    tarifberechnungsparameter_hoechstpreisHT: List["Tarifberechnungsparameter"] = Relationship(
        back_populates="hoechstpreisHT",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifberechnungsparameter.hoechstpreisHT_id==Preis.preis_sqlid",
            "lazy": "joined",
        },
    )
    tarifberechnungsparameter_hoechstpreisNT: List["Tarifberechnungsparameter"] = Relationship(
        back_populates="hoechstpreisNT",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifberechnungsparameter.hoechstpreisNT_id==Preis.preis_sqlid",
            "lazy": "joined",
        },
    )
    tarifberechnungsparameter_mindestpreis: List["Tarifberechnungsparameter"] = Relationship(
        back_populates="mindestpreis",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifberechnungsparameter.mindestpreis_id==Preis.preis_sqlid",
            "lazy": "joined",
        },
    )
