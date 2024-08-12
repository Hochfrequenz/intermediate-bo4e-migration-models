from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enum.voraussetzungen import Voraussetzungen

if TYPE_CHECKING:
    from ..bo.geraet import Geraet
    from ..zusatz_attribut import ZusatzAttribut
    from .menge import Menge


class Tarifeinschraenkung(BaseModel):
    """
    Mit dieser Komponente werden EinschrÃ¤nkungen fÃ¼r die Anwendung von Tarifen modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifeinschraenkung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifeinschraenkung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/Tarifeinschraenkung.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: Optional[str] = Field(default=None, alias="_id", title=" Id")
    """
    Eine generische ID, die fÃ¼r eigene Zwecke genutzt werden kann.
    Z.B. kÃ¶nnten hier UUIDs aus einer Datenbank stehen oder URLs zu einem Backend-System.
    """
    version: str = Field(default="v202401.4.0", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    einschraenkungleistung: Optional[list["Menge"]] = Field(default=None, title="Einschraenkungleistung")
    """
    Die vereinbarte Leistung, die (nÃ¤herungsweise) abgenommen wird.
    Insbesondere Gastarife kÃ¶nnen daran gebunden sein, dass die Leistung einer vereinbarten HÃ¶he entspricht.
    """
    einschraenkungzaehler: Optional[list["Geraet"]] = Field(default=None, title="Einschraenkungzaehler")
    """
    Liste der ZÃ¤hler/GerÃ¤te, die erforderlich sind, damit dieser Tarif zur Anwendung gelangen kann.
    (Falls keine ZÃ¤hler angegeben sind, ist der Tarif nicht an das Vorhandensein bestimmter ZÃ¤hler gebunden.)
    """
    voraussetzungen: Optional[list[Voraussetzungen]] = Field(default=None, title="Voraussetzungen")
    """
    Voraussetzungen, die erfÃ¼llt sein mÃ¼ssen, damit dieser Tarif zur Anwendung kommen kann
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    zusatzprodukte: Optional[list[str]] = Field(default=None, title="Zusatzprodukte")
    """
    Weitere Produkte, die gemeinsam mit diesem Tarif bestellt werden kÃ¶nnen
    """
