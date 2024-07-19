from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..enum.abgabe_art import AbgabeArt
from ..enum.energierichtung import Energierichtung
from ..enum.mengeneinheit import Mengeneinheit
from ..enum.waermenutzung import Waermenutzung
from ..zusatz_attribut import ZusatzAttribut
from .konzessionsabgabe import Konzessionsabgabe
from .verwendungszweck_pro_marktrolle import VerwendungszweckProMarktrolle
from .zaehlzeitregister import Zaehlzeitregister


class Zaehlwerk(BaseModel):
    """
    Mit dieser Komponente werden Zählwerke modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlwerk.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlwerk JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Zaehlwerk.json>`_
    """

    model_config = ConfigDict(
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
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    anzahl_ablesungen: int | None = Field(default=None, alias="anzahlAblesungen", title="Anzahlablesungen")
    """
    Abrechnungsrelevant
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    einheit: Mengeneinheit | None = None
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
    konzessionsabgabe: Konzessionsabgabe | None = None
    """
    Wärmenutzung Marktlokation
    """
    nachkommastelle: int | None = Field(default=None, title="Nachkommastelle")
    """
    Anzahl der Vorkommastellen
    """
    obis_kennzahl: str = Field(..., alias="obisKennzahl", title="Obiskennzahl")
    richtung: Energierichtung | None = None
    verbrauchsart: str | None = Field(default=None, title="Verbrauchsart")
    verwendungszwecke: list[VerwendungszweckProMarktrolle] | None = Field(default=None, title="Verwendungszwecke")
    """
    Schwachlastfaehigkeit
    """
    vorkommastelle: int | None = Field(default=None, title="Vorkommastelle")
    """
    Steuerbefreiung
    """
    waermenutzung: Waermenutzung | None = None
    """
    Unterbrechbarkeit Marktlokation
    """
    wandlerfaktor: float | None = Field(default=None, title="Wandlerfaktor")
    zaehlwerk_id: str | None = Field(default=None, alias="zaehlwerkId", title="Zaehlwerkid")
    zaehlzeitregister: Zaehlzeitregister | None = None
    """
    Anzahl Ablesungen pro Jahr
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    vorkommastellen: int = Field(..., title="Vorkommastellen")
    nachkommastellen: int = Field(..., title="Nachkommastellen")
    schwachlastfaehig: bool = Field(..., title="Schwachlastfaehig")
    konzessionsabgaben_typ: AbgabeArt | None = Field(default=None, alias="konzessionsabgabenTyp")
    active_from: datetime = Field(..., alias="activeFrom", title="Activefrom")
    active_until: datetime | None = Field(default=None, alias="activeUntil", title="Activeuntil")
    description: str | None = Field(default=None, title="Description")
