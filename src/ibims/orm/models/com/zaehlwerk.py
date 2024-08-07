import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.abgabe_art import AbgabeArt
from ibims.orm.models.enum.energierichtung import Energierichtung
from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.enum.waermenutzung import Waermenutzung
from ibims.orm.models.many import (
    MarktlokationzaehlwerkeDerBeteiligtenMarktrolleLink,
    MarktlokationzaehlwerkeLink,
    ZaehlerGaszaehlwerkeLink,
    ZaehlerzaehlwerkeLink,
    ZaehlwerkverwendungszweckeLink,
    ZaehlwerkzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.bo.zaehler import Zaehler
    from ibims.orm.models.bo.zaehler_gas import ZaehlerGas
    from ibims.orm.models.com.konzessionsabgabe import Konzessionsabgabe
    from ibims.orm.models.com.verwendungszweck_pro_marktrolle import VerwendungszweckProMarktrolle
    from ibims.orm.models.com.zaehlzeitregister import Zaehlzeitregister
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Zaehlwerk(SQLModel, table=True):
    """
    Mit dieser Komponente werden Zählwerke modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlwerk.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlwerk JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Zaehlwerk.json>`_
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
    anzahl_ablesungen: int | None = Field(default=None, alias="anzahlAblesungen", title="Anzahlablesungen")
    """
    Abrechnungsrelevant
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    ist_abrechnungsrelevant: bool | None = Field(
        default=None, alias="istAbrechnungsrelevant", title="Istabrechnungsrelevant"
    )
    """
    Anzahl der Nachkommastellen
    """
    ist_schwachlastfaehig: bool | None = Field(default=None, alias="istSchwachlastfaehig", title="Istschwachlastfaehig")
    """
    Schwachlastfaehigkeit
    """
    ist_steuerbefreit: bool | None = Field(default=None, alias="istSteuerbefreit", title="Iststeuerbefreit")
    """
    Konzessionsabgabe
    """
    ist_unterbrechbar: bool | None = Field(default=None, alias="istUnterbrechbar", title="Istunterbrechbar")
    """
    Stromverbrauchsart/Verbrauchsart Marktlokation
    """
    nachkommastelle: int | None = Field(default=None, title="Nachkommastelle")
    """
    Anzahl der Vorkommastellen
    """
    obis_kennzahl: str | None = Field(default=None, alias="obisKennzahl", title="Obiskennzahl")
    verbrauchsart: str | None = Field(default=None, title="Verbrauchsart")
    vorkommastelle: int | None = Field(default=None, title="Vorkommastelle")
    """
    Steuerbefreiung
    """
    wandlerfaktor: float | None = Field(default=None, title="Wandlerfaktor")
    zaehlwerk_id: str | None = Field(default=None, alias="zaehlwerkId", title="Zaehlwerkid")
    vorkommastellen: int = Field(..., title="Vorkommastellen")
    nachkommastellen: int = Field(..., title="Nachkommastellen")
    schwachlastfaehig: bool = Field(..., title="Schwachlastfaehig")
    active_from: datetime = Field(..., alias="activeFrom", title="Activefrom")
    active_until: datetime | None = Field(default=None, alias="activeUntil", title="Activeuntil")
    description: str | None = Field(default=None, title="Description")
    zaehlwerk_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    marktlokation_zaehlwerke_link: List["Marktlokation"] = Relationship(
        back_populates="zaehlwerke", link_model=MarktlokationzaehlwerkeLink
    )
    marktlokation_zaehlwerkederbeteiligtenmarktrolle_link: List["Marktlokation"] = Relationship(
        back_populates="zaehlwerkeDerBeteiligtenMarktrolle",
        link_model=MarktlokationzaehlwerkeDerBeteiligtenMarktrolleLink,
    )
    zaehler_zaehlwerke_link: List["Zaehler"] = Relationship(
        back_populates="zaehlwerke", link_model=ZaehlerzaehlwerkeLink
    )
    zaehlergas_zaehlwerke_link: List["ZaehlerGas"] = Relationship(
        back_populates="zaehlwerke", link_model=ZaehlerGaszaehlwerkeLink
    )
    einheit: Mengeneinheit | None = Field(None)
    konzessionsabgabe_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("konzessionsabgabe.konzessionsabgabe_sqlid", ondelete="SET NULL"),
        )
    )
    konzessionsabgabe: "Konzessionsabgabe" = Relationship(
        back_populates="zaehlwerk_konzessionsabgabe",
        sa_relationship_kwargs={"foreign_keys": "[Zaehlwerk.konzessionsabgabe_id]"},
    )
    richtung: Energierichtung | None = Field(None)
    verwendungszwecke: List["VerwendungszweckProMarktrolle"] = Relationship(
        back_populates="zaehlwerk_verwendungszwecke_link",
        link_model=ZaehlwerkverwendungszweckeLink,
    )
    waermenutzung: Waermenutzung | None = Field(None)
    zaehlzeitregister_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlzeitregister.zaehlzeitregister_sqlid", ondelete="SET NULL"),
        )
    )
    zaehlzeitregister: "Zaehlzeitregister" = Relationship(
        back_populates="zaehlwerk_zaehlzeitregister",
        sa_relationship_kwargs={"foreign_keys": "[Zaehlwerk.zaehlzeitregister_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="zaehlwerk_zusatzattribute_link",
        link_model=ZaehlwerkzusatzAttributeLink,
    )
    konzessionsabgabenTyp: AbgabeArt | None = Field(None)
