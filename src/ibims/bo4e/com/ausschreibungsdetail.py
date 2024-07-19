from pydantic import BaseModel, ConfigDict, Field

from ..enum.zaehlertyp import Zaehlertyp
from ..zusatz_attribut import ZusatzAttribut
from .adresse import Adresse
from .menge import Menge
from .zeitraum import Zeitraum


class Ausschreibungsdetail(BaseModel):
    """
    Die Komponente Ausschreibungsdetail wird verwendet um die Informationen zu einer Abnahmestelle innerhalb eines
    Ausschreibungsloses abzubilden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Ausschreibungsdetail.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibungsdetail JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Ausschreibungsdetail.json>`_
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
    ist_lastgang_vorhanden: bool | None = Field(
        default=None, alias="istLastgangVorhanden", title="Istlastgangvorhanden"
    )
    """
    Prognosewert für die Jahresarbeit der ausgeschriebenen Lokation
    """
    kunde: str | None = Field(default=None, title="Kunde")
    """
    Bezeichnung des Kunden, der die Marktlokation nutzt
    """
    lieferzeitraum: Zeitraum | None = None
    """
    Angefragter Zeitraum für die ausgeschriebene Belieferung
    """
    marktlokations_id: str | None = Field(default=None, alias="marktlokationsId", title="Marktlokationsid")
    """
    Identifikation einer ausgeschriebenen Marktlokation
    """
    marktlokationsadresse: Adresse | None = None
    """
    Die Adresse an der die Marktlokation sich befindet
    """
    marktlokationsbezeichnung: str | None = Field(default=None, title="Marktlokationsbezeichnung")
    """
    Bezeichnung für die Lokation, z.B. 'Zentraler Einkauf, Hamburg'
    """
    netzbetreiber: str | None = Field(default=None, title="Netzbetreiber")
    """
    Bezeichnung des zuständigen Netzbetreibers, z.B. 'Stromnetz Hamburg GmbH'
    """
    netzebene_lieferung: str | None = Field(default=None, alias="netzebeneLieferung", title="Netzebenelieferung")
    """
    In der angegebenen Netzebene wird die Marktlokation versorgt, z.B. MSP für Mittelspannung
    """
    netzebene_messung: str | None = Field(default=None, alias="netzebeneMessung", title="Netzebenemessung")
    """
    In der angegebenen Netzebene wird die Lokation gemessen, z.B. NSP für Niederspannung
    """
    prognose_arbeit_lieferzeitraum: Menge | None = Field(default=None, alias="prognoseArbeitLieferzeitraum")
    """
    Ein Prognosewert für die Arbeit innerhalb des angefragten Lieferzeitraums der ausgeschriebenen Lokation
    """
    prognose_jahresarbeit: Menge | None = Field(default=None, alias="prognoseJahresarbeit")
    """
    Prognosewert für die Jahresarbeit der ausgeschriebenen Lokation
    """
    prognose_leistung: Menge | None = Field(default=None, alias="prognoseLeistung")
    """
    Prognosewert für die abgenommene maximale Leistung der ausgeschriebenen Lokation
    """
    rechnungsadresse: Adresse | None = None
    """
    Die (evtl. abweichende) Rechnungsadresse
    """
    zaehlernummer: str | None = Field(default=None, title="Zaehlernummer")
    """
    Die Bezeichnung des Zählers an der Marktlokation
    """
    zaehlertechnik: Zaehlertyp | None = None
    """
    Spezifikation, um welche Zählertechnik es sich im vorliegenden Fall handelt, z.B. Leistungsmessung
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
