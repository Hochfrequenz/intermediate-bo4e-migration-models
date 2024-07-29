import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.waehrungscode import Waehrungscode
from ibims.orm.models.many import BetragzusatzAttributeLink, KostensummeKostenLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.fremdkosten import Fremdkosten
    from ibims.orm.models.bo.kosten import Kosten
    from ibims.orm.models.bo.rechnung import Rechnung
    from ibims.orm.models.com.angebotsposition import Angebotsposition
    from ibims.orm.models.com.angebotsteil import Angebotsteil
    from ibims.orm.models.com.angebotsvariante import Angebotsvariante
    from ibims.orm.models.com.fremdkostenblock import Fremdkostenblock
    from ibims.orm.models.com.fremdkostenposition import Fremdkostenposition
    from ibims.orm.models.com.kostenblock import Kostenblock
    from ibims.orm.models.com.kostenposition import Kostenposition
    from ibims.orm.models.com.rechnungsposition import Rechnungsposition
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Betrag(SQLModel, table=True):
    """
    Die Komponente wird dazu verwendet, Summenbeträge (beispielsweise in Angeboten und Rechnungen) als Geldbeträge
    abzubilden. Die Einheit ist dabei immer die Hauptwährung also Euro, Dollar etc…

    .. raw:: html

        <object data="../_static/images/bo4e/com/Betrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Betrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Betrag.json>`_
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
    Gibt den Betrag des Preises an.
    """
    betrag_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    fremdkosten_summeKosten: List["Fremdkosten"] = Relationship(
        back_populates="summeKosten",
        sa_relationship_kwargs={
            "primaryjoin": "Fremdkosten.summeKosten_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    kosten_summekosten_link: List["Kosten"] = Relationship(
        back_populates="summeKosten", link_model=KostensummeKostenLink
    )
    rechnung_gesamtbrutto: List["Rechnung"] = Relationship(
        back_populates="gesamtbrutto",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.gesamtbrutto_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    rechnung_gesamtnetto: List["Rechnung"] = Relationship(
        back_populates="gesamtnetto",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.gesamtnetto_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    rechnung_gesamtsteuer: List["Rechnung"] = Relationship(
        back_populates="gesamtsteuer",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.gesamtsteuer_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    rechnung_rabattBrutto: List["Rechnung"] = Relationship(
        back_populates="rabattBrutto",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.rabattBrutto_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    rechnung_vorausgezahlt: List["Rechnung"] = Relationship(
        back_populates="vorausgezahlt",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.vorausgezahlt_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    rechnung_zuZahlen: List["Rechnung"] = Relationship(
        back_populates="zuZahlen",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.zuZahlen_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    angebotsposition_positionskosten: List["Angebotsposition"] = Relationship(
        back_populates="positionskosten",
        sa_relationship_kwargs={
            "primaryjoin": "Angebotsposition.positionskosten_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    angebotsteil_gesamtkostenangebotsteil: List["Angebotsteil"] = Relationship(
        back_populates="gesamtkostenangebotsteil",
        sa_relationship_kwargs={
            "primaryjoin": "Angebotsteil.gesamtkostenangebotsteil_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    angebotsvariante_gesamtkosten: List["Angebotsvariante"] = Relationship(
        back_populates="gesamtkosten",
        sa_relationship_kwargs={
            "primaryjoin": "Angebotsvariante.gesamtkosten_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    waehrung: Waehrungscode | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="betrag_zusatzattribute_link",
        link_model=BetragzusatzAttributeLink,
    )
    fremdkostenblock_summeKostenblock: List["Fremdkostenblock"] = Relationship(
        back_populates="summeKostenblock",
        sa_relationship_kwargs={
            "primaryjoin": "Fremdkostenblock.summeKostenblock_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    fremdkostenposition_betragKostenposition: List["Fremdkostenposition"] = Relationship(
        back_populates="betragKostenposition",
        sa_relationship_kwargs={
            "primaryjoin": "Fremdkostenposition.betragKostenposition_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    kostenblock_summeKostenblock: List["Kostenblock"] = Relationship(
        back_populates="summeKostenblock",
        sa_relationship_kwargs={
            "primaryjoin": "Kostenblock.summeKostenblock_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    kostenposition_betragKostenposition: List["Kostenposition"] = Relationship(
        back_populates="betragKostenposition",
        sa_relationship_kwargs={
            "primaryjoin": "Kostenposition.betragKostenposition_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    rechnungsposition_teilrabattNetto: List["Rechnungsposition"] = Relationship(
        back_populates="teilrabattNetto",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnungsposition.teilrabattNetto_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
    rechnungsposition_teilsummeNetto: List["Rechnungsposition"] = Relationship(
        back_populates="teilsummeNetto",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnungsposition.teilsummeNetto_id==Betrag.betrag_sqlid",
            "lazy": "joined",
        },
    )
