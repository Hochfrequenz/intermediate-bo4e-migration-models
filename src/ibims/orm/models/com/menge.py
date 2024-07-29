import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.many import MengezusatzAttributeLink, TarifeinschraenkungeinschraenkungleistungLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.lastgang import Lastgang
    from ibims.orm.models.com.angebotsposition import Angebotsposition
    from ibims.orm.models.com.angebotsteil import Angebotsteil
    from ibims.orm.models.com.angebotsvariante import Angebotsvariante
    from ibims.orm.models.com.ausschreibungsdetail import Ausschreibungsdetail
    from ibims.orm.models.com.ausschreibungslos import Ausschreibungslos
    from ibims.orm.models.com.fremdkostenposition import Fremdkostenposition
    from ibims.orm.models.com.kostenposition import Kostenposition
    from ibims.orm.models.com.rechnungsposition import Rechnungsposition
    from ibims.orm.models.com.tarifeinschraenkung import Tarifeinschraenkung
    from ibims.orm.models.com.vertragsteil import Vertragsteil
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Menge(SQLModel, table=True):
    """
    Abbildung einer Menge mit Wert und Einheit.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Menge.svg" type="image/svg+xml"></object>

    .. HINT::
        `Menge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Menge.json>`_
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
    Gibt den absoluten Wert der Menge an
    """
    menge_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    lastgang_zeitIntervallLaenge: List["Lastgang"] = Relationship(
        back_populates="zeitIntervallLaenge",
        sa_relationship_kwargs={
            "primaryjoin": "Lastgang.zeitIntervallLaenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    angebotsposition_positionsmenge: List["Angebotsposition"] = Relationship(
        back_populates="positionsmenge",
        sa_relationship_kwargs={
            "primaryjoin": "Angebotsposition.positionsmenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    angebotsteil_gesamtmengeangebotsteil: List["Angebotsteil"] = Relationship(
        back_populates="gesamtmengeangebotsteil",
        sa_relationship_kwargs={
            "primaryjoin": "Angebotsteil.gesamtmengeangebotsteil_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    angebotsvariante_gesamtmenge: List["Angebotsvariante"] = Relationship(
        back_populates="gesamtmenge",
        sa_relationship_kwargs={
            "primaryjoin": "Angebotsvariante.gesamtmenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungsdetail_prognoseArbeitLieferzeitraum: List["Ausschreibungsdetail"] = Relationship(
        back_populates="prognoseArbeitLieferzeitraum",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungsdetail.prognoseArbeitLieferzeitraum_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungsdetail_prognoseJahresarbeit: List["Ausschreibungsdetail"] = Relationship(
        back_populates="prognoseJahresarbeit",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungsdetail.prognoseJahresarbeit_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungsdetail_prognoseLeistung: List["Ausschreibungsdetail"] = Relationship(
        back_populates="prognoseLeistung",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungsdetail.prognoseLeistung_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungslos_gesamtMenge: List["Ausschreibungslos"] = Relationship(
        back_populates="gesamtMenge",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungslos.gesamtMenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungslos_wunschMaximalmenge: List["Ausschreibungslos"] = Relationship(
        back_populates="wunschMaximalmenge",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungslos.wunschMaximalmenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungslos_wunschMindestmenge: List["Ausschreibungslos"] = Relationship(
        back_populates="wunschMindestmenge",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungslos.wunschMindestmenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    fremdkostenposition_menge: List["Fremdkostenposition"] = Relationship(
        back_populates="menge",
        sa_relationship_kwargs={
            "primaryjoin": "Fremdkostenposition.menge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    fremdkostenposition_zeitmenge: List["Fremdkostenposition"] = Relationship(
        back_populates="zeitmenge",
        sa_relationship_kwargs={
            "primaryjoin": "Fremdkostenposition.zeitmenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    kostenposition_menge: List["Kostenposition"] = Relationship(
        back_populates="menge",
        sa_relationship_kwargs={
            "primaryjoin": "Kostenposition.menge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    kostenposition_zeitmenge: List["Kostenposition"] = Relationship(
        back_populates="zeitmenge",
        sa_relationship_kwargs={
            "primaryjoin": "Kostenposition.zeitmenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    einheit: Mengeneinheit | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="menge_zusatzattribute_link", link_model=MengezusatzAttributeLink
    )
    rechnungsposition_positionsMenge: List["Rechnungsposition"] = Relationship(
        back_populates="positionsMenge",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnungsposition.positionsMenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    rechnungsposition_zeitbezogeneMenge: List["Rechnungsposition"] = Relationship(
        back_populates="zeitbezogeneMenge",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnungsposition.zeitbezogeneMenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    tarifeinschraenkung_einschraenkungleistung_link: List["Tarifeinschraenkung"] = Relationship(
        back_populates="einschraenkungleistung",
        link_model=TarifeinschraenkungeinschraenkungleistungLink,
    )
    vertragsteil_maximaleAbnahmemenge: List["Vertragsteil"] = Relationship(
        back_populates="maximaleAbnahmemenge",
        sa_relationship_kwargs={
            "primaryjoin": "Vertragsteil.maximaleAbnahmemenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    vertragsteil_minimaleAbnahmemenge: List["Vertragsteil"] = Relationship(
        back_populates="minimaleAbnahmemenge",
        sa_relationship_kwargs={
            "primaryjoin": "Vertragsteil.minimaleAbnahmemenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
    vertragsteil_vertraglichFixierteMenge: List["Vertragsteil"] = Relationship(
        back_populates="vertraglichFixierteMenge",
        sa_relationship_kwargs={
            "primaryjoin": "Vertragsteil.vertraglichFixierteMenge_id==Menge.menge_sqlid",
            "lazy": "joined",
        },
    )
