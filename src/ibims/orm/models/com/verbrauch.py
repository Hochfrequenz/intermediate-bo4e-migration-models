import uuid as uuid_pkg
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.ablesende_rolle import AblesendeRolle
from ibims.orm.models.enum.ablesungsstatus import Ablesungsstatus
from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.enum.messwertstatus import Messwertstatus
from ibims.orm.models.enum.wertermittlungsverfahren import Wertermittlungsverfahren
from ibims.orm.models.many import (
    EnergiemengeenergieverbrauchLink,
    MarktlokationverbrauchsmengenLink,
    VerbrauchzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.energiemenge import Energiemenge
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Verbrauch(SQLModel, table=True):
    """
    Abbildung eines zeitlich abgegrenzten Verbrauchs

    .. raw:: html

        <object data="../_static/images/bo4e/com/Verbrauch.svg" type="image/svg+xml"></object>

    .. HINT::
        `Verbrauch JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Verbrauch.json>`_
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
    enddatum: datetime | None = Field(default=None, title="Enddatum")
    """
    Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird
    """
    obis_kennzahl: str | None = Field(default=None, alias="obisKennzahl", title="Obiskennzahl")
    """
    Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:
    """
    startdatum: datetime | None = Field(default=None, title="Startdatum")
    """
    Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird
    """
    wert: float | None = Field(default=None, title="Wert")
    """
    Gibt den absoluten Wert der Menge an
    """
    ablesegrund: str | None = Field(default=None, title="Ablesegrund")
    ablesebeschreibung: str | None = Field(default=None, title="Ablesebeschreibung")
    periodenverbrauch: Decimal | None = Field(default=None, title="Periodenverbrauch")
    periodenverbrauch_ursprung: str | None = Field(
        default=None,
        alias="periodenverbrauchUrsprung",
        title="Periodenverbrauchursprung",
    )
    energiegehalt_gas: Decimal | None = Field(default=None, alias="energiegehaltGas", title="Energiegehaltgas")
    energiegehalt_gas_gueltig_von: datetime | None = Field(
        default=None,
        alias="energiegehaltGasGueltigVon",
        title="Energiegehaltgasgueltigvon",
    )
    energiegehalt_gas_gueltig_bis: datetime | None = Field(
        default=None,
        alias="energiegehaltGasGueltigBis",
        title="Energiegehaltgasgueltigbis",
    )
    umwandlungsfaktor_gas: Decimal | None = Field(
        default=None, alias="umwandlungsfaktorGas", title="Umwandlungsfaktorgas"
    )
    umwandlungsfaktor_gas_gueltig_von: datetime | None = Field(
        default=None,
        alias="umwandlungsfaktorGasGueltigVon",
        title="Umwandlungsfaktorgasgueltigvon",
    )
    umwandlungsfaktor_gas_gueltig_bis: datetime | None = Field(
        default=None,
        alias="umwandlungsfaktorGasGueltigBis",
        title="Umwandlungsfaktorgasgueltigbis",
    )
    verbrauch_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    energiemenge_energieverbrauch_link: List["Energiemenge"] = Relationship(
        back_populates="energieverbrauch", link_model=EnergiemengeenergieverbrauchLink
    )
    marktlokation_verbrauchsmengen_link: List["Marktlokation"] = Relationship(
        back_populates="verbrauchsmengen", link_model=MarktlokationverbrauchsmengenLink
    )
    einheit: Mengeneinheit | None = Field(None)
    messwertstatus: Messwertstatus | None = Field(None)
    wertermittlungsverfahren: Wertermittlungsverfahren | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="verbrauch_zusatzattribute_link",
        link_model=VerbrauchzusatzAttributeLink,
    )
    ableser: AblesendeRolle | None = Field(None)
    status: Ablesungsstatus | None = Field(None)
