import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import LastgangwerteLink, LastgangzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.bo.messlokation import Messlokation
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.com.zeitreihenwert import Zeitreihenwert
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Lastgang(SQLModel, table=True):
    """
    Modell zur Abbildung eines Lastganges;
    In diesem Modell werden die Messwerte mit einem vollständigen Zeitintervall (zeit_intervall_laenge) angegeben und es bietet daher eine hohe Flexibilität in der Übertragung jeglicher zeitlich veränderlicher Messgrössen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Lastgang.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lastgang JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Lastgang.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    obis_kennzahl: str | None = Field(default=None, alias="obisKennzahl", title="Obiskennzahl")
    """
    Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    """
    version: str | None = Field(default=None, title="Version")
    """
    Versionsnummer des Lastgangs
    """
    lastgang_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ | None = Field(Typ.LASTGANG)
    marktlokation_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktlokation.marktlokation_sqlid", ondelete="SET NULL"),
        )
    )
    marktlokation: "Marktlokation" = Relationship(
        back_populates="lastgang_marktlokation",
        sa_relationship_kwargs={"foreign_keys": "[Lastgang.marktlokation_id]"},
    )
    messgroesse: Mengeneinheit | None = Field(None)
    messlokation_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("messlokation.messlokation_sqlid", ondelete="SET NULL"),
        )
    )
    messlokation: "Messlokation" = Relationship(
        back_populates="lastgang_messlokation",
        sa_relationship_kwargs={"foreign_keys": "[Lastgang.messlokation_id]"},
    )
    sparte: Sparte | None = Field(None)
    werte: List["Zeitreihenwert"] = Relationship(back_populates="lastgang_werte_link", link_model=LastgangwerteLink)
    zeitIntervallLaenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    zeitIntervallLaenge: "Menge" = Relationship(
        back_populates="lastgang_zeitIntervallLaenge",
        sa_relationship_kwargs={"foreign_keys": "[Lastgang.zeitIntervallLaenge_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="lastgang_zusatzattribute_link",
        link_model=LastgangzusatzAttributeLink,
    )
