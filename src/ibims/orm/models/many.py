"""
File containing all linking classes for many-many relations in the BO4E version
"""

import uuid as uuid_pkg
from typing import Optional

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, SQLModel


class AngebotvariantenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Angebot and Angebotsvariante for field varianten.
    """

    angebot_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebot.angebot_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    angebotsvariante_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebotsvariante.angebotsvariante_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AngebotzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Angebot and ZusatzAttribut for field zusatzAttribute.
    """

    angebot_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebot.angebot_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AusschreibungloseLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Ausschreibung and Ausschreibungslos for field lose.
    """

    ausschreibung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("ausschreibung.ausschreibung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    ausschreibungslos_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("ausschreibungslos.ausschreibungslos_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AusschreibungzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Ausschreibung and ZusatzAttribut for field zusatzAttribute.
    """

    ausschreibung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("ausschreibung.ausschreibung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class BilanzierungzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Bilanzierung and ZusatzAttribut for field zusatzAttribute.
    """

    bilanzierung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("bilanzierung.bilanzierung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class BilanzierunglastprofileLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Bilanzierung and Lastprofil for field lastprofile.
    """

    bilanzierung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("bilanzierung.bilanzierung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    lastprofil_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("lastprofil.lastprofil_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class BuendelvertrageinzelvertraegeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Buendelvertrag and Vertrag for field einzelvertraege.
    """

    buendelvertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("buendelvertrag.buendelvertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    vertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertrag.vertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class Buendelvertragunterzeichnervp1Link(SQLModel, table=True):
    """
    class linking m-n relation of tables Buendelvertrag and Unterschrift for field unterzeichnervp1.
    """

    buendelvertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("buendelvertrag.buendelvertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    unterschrift_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("unterschrift.unterschrift_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class Buendelvertragunterzeichnervp2Link(SQLModel, table=True):
    """
    class linking m-n relation of tables Buendelvertrag and Unterschrift for field unterzeichnervp2.
    """

    buendelvertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("buendelvertrag.buendelvertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    unterschrift_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("unterschrift.unterschrift_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class BuendelvertragvertragskonditionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Buendelvertrag and Vertragskonditionen for field vertragskonditionen.
    """

    buendelvertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("buendelvertrag.buendelvertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    vertragskonditionen_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertragskonditionen.vertragskonditionen_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class BuendelvertragzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Buendelvertrag and ZusatzAttribut for field zusatzAttribute.
    """

    buendelvertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("buendelvertrag.buendelvertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class DokumentzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Dokument and ZusatzAttribut for field zusatzAttribute.
    """

    dokument_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("dokument.dokument_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class EnergiemengeenergieverbrauchLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Energiemenge and Verbrauch for field energieverbrauch.
    """

    energiemenge_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("energiemenge.energiemenge_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    verbrauch_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("verbrauch.verbrauch_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class EnergiemengezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Energiemenge and ZusatzAttribut for field zusatzAttribute.
    """

    energiemenge_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("energiemenge.energiemenge_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class FremdkostenkostenbloeckeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Fremdkosten and Fremdkostenblock for field kostenbloecke.
    """

    fremdkosten_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("fremdkosten.fremdkosten_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    fremdkostenblock_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("fremdkostenblock.fremdkostenblock_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class FremdkostenzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Fremdkosten and ZusatzAttribut for field zusatzAttribute.
    """

    fremdkosten_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("fremdkosten.fremdkosten_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class GeraetzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Geraet and ZusatzAttribut for field zusatzAttribute.
    """

    geraet_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geraet.geraet_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class GeschaeftspartneransprechpartnerLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Geschaeftspartner and Person for field ansprechpartner.
    """

    geschaeftspartner_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    person_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("person.person_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class GeschaeftspartnerkontaktwegeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Geschaeftspartner and Kontaktweg for field kontaktwege.
    """

    geschaeftspartner_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    kontaktweg_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kontaktweg.kontaktweg_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class GeschaeftspartnerzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Geschaeftspartner and ZusatzAttribut for field zusatzAttribute.
    """

    geschaeftspartner_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class HinweiszusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Hinweis and ZusatzAttribut for field zusatzAttribute.
    """

    hinweis_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("hinweis.hinweis_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KampagnezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Kampagne and ZusatzAttribut for field zusatzAttribute.
    """

    kampagne_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kampagne.kampagne_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KostenkostenbloeckeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Kosten and Kostenblock for field kostenbloecke.
    """

    kosten_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kosten.kosten_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    kostenblock_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kostenblock.kostenblock_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KostensummeKostenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Kosten and Betrag for field summeKosten.
    """

    kosten_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kosten.kosten_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    betrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("betrag.betrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KostenzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Kosten and ZusatzAttribut for field zusatzAttribute.
    """

    kosten_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kosten.kosten_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class LastgangwerteLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Lastgang and Zeitreihenwert for field werte.
    """

    lastgang_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("lastgang.lastgang_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zeitreihenwert_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitreihenwert.zeitreihenwert_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class LastgangzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Lastgang and ZusatzAttribut for field zusatzAttribute.
    """

    lastgang_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("lastgang.lastgang_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MarktlokationverbrauchsmengenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Marktlokation and Verbrauch for field verbrauchsmengen.
    """

    marktlokation_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktlokation.marktlokation_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    verbrauch_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("verbrauch.verbrauch_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MarktlokationzaehlwerkeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Marktlokation and Zaehlwerk for field zaehlwerke.
    """

    marktlokation_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktlokation.marktlokation_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zaehlwerk_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlwerk.zaehlwerk_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MarktlokationzaehlwerkeDerBeteiligtenMarktrolleLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Marktlokation and Zaehlwerk for field zaehlwerkeDerBeteiligtenMarktrolle.
    """

    marktlokation_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktlokation.marktlokation_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zaehlwerk_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlwerk.zaehlwerk_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MarktlokationzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Marktlokation and ZusatzAttribut for field zusatzAttribute.
    """

    marktlokation_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktlokation.marktlokation_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MarktteilnehmerzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Marktteilnehmer and ZusatzAttribut for field zusatzAttribute.
    """

    marktteilnehmer_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktteilnehmer.marktteilnehmer_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MesslokationgeraeteLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Messlokation and Geraet for field geraete.
    """

    messlokation_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("messlokation.messlokation_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    geraet_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geraet.geraet_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MesslokationmessdienstleistungLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Messlokation and Dienstleistung for field messdienstleistung.
    """

    messlokation_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("messlokation.messlokation_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    dienstleistung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("dienstleistung.dienstleistung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MesslokationmesslokationszaehlerLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Messlokation and Zaehler for field messlokationszaehler.
    """

    messlokation_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("messlokation.messlokation_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zaehler_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehler.zaehler_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MesslokationzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Messlokation and ZusatzAttribut for field zusatzAttribute.
    """

    messlokation_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("messlokation.messlokation_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PersonkontaktwegeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Person and Kontaktweg for field kontaktwege.
    """

    person_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("person.person_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    kontaktweg_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kontaktweg.kontaktweg_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PersonzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Person and ZusatzAttribut for field zusatzAttribute.
    """

    person_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("person.person_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PersonzustaendigkeitenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Person and Zustaendigkeit for field zustaendigkeiten.
    """

    person_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("person.person_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zustaendigkeit_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zustaendigkeit.zustaendigkeit_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattpreispositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Preisblatt and Preisposition for field preispositionen.
    """

    preisblatt_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblatt.preisblatt_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    preisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisposition.preisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Preisblatt and ZusatzAttribut for field zusatzAttribute.
    """

    preisblatt_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblatt.preisblatt_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattDienstleistungpreispositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattDienstleistung and Preisposition for field preispositionen.
    """

    preisblattdienstleistung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "preisblattdienstleistung.preisblattdienstleistung_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    preisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisposition.preisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattDienstleistungzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattDienstleistung and ZusatzAttribut for field zusatzAttribute.
    """

    preisblattdienstleistung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "preisblattdienstleistung.preisblattdienstleistung_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattHardwareinklusiveGeraeteLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattHardware and Geraet for field inklusiveGeraete.
    """

    preisblatthardware_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblatthardware.preisblatthardware_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    geraet_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geraet.geraet_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattHardwarepreispositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattHardware and Preisposition for field preispositionen.
    """

    preisblatthardware_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblatthardware.preisblatthardware_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    preisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisposition.preisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattHardwarezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattHardware and ZusatzAttribut for field zusatzAttribute.
    """

    preisblatthardware_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblatthardware.preisblatthardware_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattKonzessionsabgabepreispositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattKonzessionsabgabe and Preisposition for field preispositionen.
    """

    preisblattkonzessionsabgabe_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "preisblattkonzessionsabgabe.preisblattkonzessionsabgabe_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    preisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisposition.preisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattKonzessionsabgabezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattKonzessionsabgabe and ZusatzAttribut for field zusatzAttribute.
    """

    preisblattkonzessionsabgabe_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "preisblattkonzessionsabgabe.preisblattkonzessionsabgabe_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattMessunginklusiveGeraeteLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattMessung and Geraet for field inklusiveGeraete.
    """

    preisblattmessung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblattmessung.preisblattmessung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    geraet_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geraet.geraet_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattMessungpreispositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattMessung and Preisposition for field preispositionen.
    """

    preisblattmessung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblattmessung.preisblattmessung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    preisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisposition.preisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattMessungzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattMessung and ZusatzAttribut for field zusatzAttribute.
    """

    preisblattmessung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblattmessung.preisblattmessung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattNetznutzungpreispositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattNetznutzung and Preisposition for field preispositionen.
    """

    preisblattnetznutzung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblattnetznutzung.preisblattnetznutzung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    preisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisposition.preisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisblattNetznutzungzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PreisblattNetznutzung and ZusatzAttribut for field zusatzAttribute.
    """

    preisblattnetznutzung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisblattnetznutzung.preisblattnetznutzung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RechnungrechnungspositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Rechnung and Rechnungsposition for field rechnungspositionen.
    """

    rechnung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("rechnung.rechnung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    rechnungsposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("rechnungsposition.rechnungsposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RechnungsteuerbetraegeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Rechnung and Steuerbetrag for field steuerbetraege.
    """

    rechnung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("rechnung.rechnung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    steuerbetrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("steuerbetrag.steuerbetrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RechnungzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Rechnung and ZusatzAttribut for field zusatzAttribute.
    """

    rechnung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("rechnung.rechnung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionnegativListeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Region and Regionskriterium for field negativListe.
    """

    region_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("region.region_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    regionskriterium_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionskriterium.regionskriterium_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionpositivListeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Region and Regionskriterium for field positivListe.
    """

    region_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("region.region_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    regionskriterium_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionskriterium.regionskriterium_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Region and ZusatzAttribut for field zusatzAttribute.
    """

    region_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("region.region_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionaltarifpreisgarantienLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Regionaltarif and RegionalePreisgarantie for field preisgarantien.
    """

    regionaltarif_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionaltarif.regionaltarif_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    regionalepreisgarantie_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "regionalepreisgarantie.regionalepreisgarantie_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )


class RegionaltariftarifAufAbschlaegeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Regionaltarif and RegionalerAufAbschlag for field tarifAufAbschlaege.
    """

    regionaltarif_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionaltarif.regionaltarif_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    regionaleraufabschlag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionaleraufabschlag.regionaleraufabschlag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionaltariftarifpreiseLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Regionaltarif and RegionaleTarifpreisposition for field tarifpreise.
    """

    regionaltarif_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionaltarif.regionaltarif_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    regionaletarifpreisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "regionaletarifpreisposition.regionaletarifpreisposition_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )


class RegionaltarifzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Regionaltarif and ZusatzAttribut for field zusatzAttribute.
    """

    regionaltarif_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionaltarif.regionaltarif_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class StandorteigenschafteneigenschaftenStromLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Standorteigenschaften and StandorteigenschaftenStrom for field eigenschaftenStrom.
    """

    standorteigenschaften_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("standorteigenschaften.standorteigenschaften_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    standorteigenschaftenstrom_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "standorteigenschaftenstrom.standorteigenschaftenstrom_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )


class StandorteigenschaftenzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Standorteigenschaften and ZusatzAttribut for field zusatzAttribute.
    """

    standorteigenschaften_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("standorteigenschaften.standorteigenschaften_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TariftarifAufAbschlaegeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarif and AufAbschlagRegional for field tarifAufAbschlaege.
    """

    tarif_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarif.tarif_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    aufabschlagregional_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("aufabschlagregional.aufabschlagregional_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TariftarifpreiseLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarif and TarifpreispositionProOrt for field tarifpreise.
    """

    tarif_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarif.tarif_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    tarifpreispositionproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "tarifpreispositionproort.tarifpreispositionproort_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )


class TarifzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarif and ZusatzAttribut for field zusatzAttribute.
    """

    tarif_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarif.tarif_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifinfozusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifinfo and ZusatzAttribut for field zusatzAttribute.
    """

    tarifinfo_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifinfo.tarifinfo_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifkostenzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifkosten and ZusatzAttribut for field zusatzAttribute.
    """

    tarifkosten_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifkosten.tarifkosten_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifpreisblatttarifAufAbschlaegeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifpreisblatt and AufAbschlag for field tarifAufAbschlaege.
    """

    tarifpreisblatt_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifpreisblatt.tarifpreisblatt_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    aufabschlag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("aufabschlag.aufabschlag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifpreisblatttarifpreiseLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifpreisblatt and Tarifpreisposition for field tarifpreise.
    """

    tarifpreisblatt_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifpreisblatt.tarifpreisblatt_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    tarifpreisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifpreisposition.tarifpreisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifpreisblattzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifpreisblatt and ZusatzAttribut for field zusatzAttribute.
    """

    tarifpreisblatt_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifpreisblatt.tarifpreisblatt_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class Vertragunterzeichnervp1Link(SQLModel, table=True):
    """
    class linking m-n relation of tables Vertrag and Unterschrift for field unterzeichnervp1.
    """

    vertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertrag.vertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    unterschrift_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("unterschrift.unterschrift_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class Vertragunterzeichnervp2Link(SQLModel, table=True):
    """
    class linking m-n relation of tables Vertrag and Unterschrift for field unterzeichnervp2.
    """

    vertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertrag.vertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    unterschrift_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("unterschrift.unterschrift_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class VertragvertragsteileLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Vertrag and Vertragsteil for field vertragsteile.
    """

    vertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertrag.vertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    vertragsteil_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertragsteil.vertragsteil_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class VertragzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Vertrag and ZusatzAttribut for field zusatzAttribute.
    """

    vertrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertrag.vertrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZaehlergeraeteLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zaehler and Geraet for field geraete.
    """

    zaehler_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehler.zaehler_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    geraet_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geraet.geraet_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZaehlerzaehlwerkeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zaehler and Zaehlwerk for field zaehlwerke.
    """

    zaehler_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehler.zaehler_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zaehlwerk_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlwerk.zaehlwerk_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZaehlerzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zaehler and ZusatzAttribut for field zusatzAttribute.
    """

    zaehler_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehler.zaehler_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZaehlerGaszusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables ZaehlerGas and ZusatzAttribut for field zusatzAttribute.
    """

    zaehlergas_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlergas.zaehlergas_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZaehlerGaszaehlwerkeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables ZaehlerGas and Zaehlwerk for field zaehlwerke.
    """

    zaehlergas_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlergas.zaehlergas_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zaehlwerk_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlwerk.zaehlwerk_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZeitreihewerteLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zeitreihe and Zeitreihenwert for field werte.
    """

    zeitreihe_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitreihe.zeitreihe_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zeitreihenwert_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitreihenwert.zeitreihenwert_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZeitreihezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zeitreihe and ZusatzAttribut for field zusatzAttribute.
    """

    zeitreihe_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitreihe.zeitreihe_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AdressezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Adresse and ZusatzAttribut for field zusatzAttribute.
    """

    adresse_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("adresse.adresse_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AngebotspositionzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Angebotsposition and ZusatzAttribut for field zusatzAttribute.
    """

    angebotsposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebotsposition.angebotsposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AngebotsteillieferstellenangebotsteilLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Angebotsteil and Marktlokation for field lieferstellenangebotsteil.
    """

    angebotsteil_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebotsteil.angebotsteil_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    marktlokation_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktlokation.marktlokation_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AngebotsteilpositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Angebotsteil and Angebotsposition for field positionen.
    """

    angebotsteil_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebotsteil.angebotsteil_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    angebotsposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebotsposition.angebotsposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AngebotsteilzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Angebotsteil and ZusatzAttribut for field zusatzAttribute.
    """

    angebotsteil_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebotsteil.angebotsteil_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AngebotsvarianteteileLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Angebotsvariante and Angebotsteil for field teile.
    """

    angebotsvariante_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebotsvariante.angebotsvariante_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    angebotsteil_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebotsteil.angebotsteil_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AngebotsvariantezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Angebotsvariante and ZusatzAttribut for field zusatzAttribute.
    """

    angebotsvariante_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("angebotsvariante.angebotsvariante_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AufAbschlagstaffelnLink(SQLModel, table=True):
    """
    class linking m-n relation of tables AufAbschlag and Preisstaffel for field staffeln.
    """

    aufabschlag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("aufabschlag.aufabschlag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    preisstaffel_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisstaffel.preisstaffel_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AufAbschlagzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables AufAbschlag and ZusatzAttribut for field zusatzAttribute.
    """

    aufabschlag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("aufabschlag.aufabschlag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AufAbschlagProOrtstaffelnLink(SQLModel, table=True):
    """
    class linking m-n relation of tables AufAbschlagProOrt and AufAbschlagstaffelProOrt for field staffeln.
    """

    aufabschlagproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("aufabschlagproort.aufabschlagproort_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    aufabschlagstaffelproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "aufabschlagstaffelproort.aufabschlagstaffelproort_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )


class AufAbschlagProOrtzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables AufAbschlagProOrt and ZusatzAttribut for field zusatzAttribute.
    """

    aufabschlagproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("aufabschlagproort.aufabschlagproort_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AufAbschlagRegionalbetraegeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables AufAbschlagRegional and AufAbschlagProOrt for field betraege.
    """

    aufabschlagregional_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("aufabschlagregional.aufabschlagregional_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    aufabschlagproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("aufabschlagproort.aufabschlagproort_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AufAbschlagRegionalzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables AufAbschlagRegional and ZusatzAttribut for field zusatzAttribute.
    """

    aufabschlagregional_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("aufabschlagregional.aufabschlagregional_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AufAbschlagstaffelProOrtzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables AufAbschlagstaffelProOrt and ZusatzAttribut for field zusatzAttribute.
    """

    aufabschlagstaffelproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "aufabschlagstaffelproort.aufabschlagstaffelproort_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AusschreibungsdetailzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Ausschreibungsdetail and ZusatzAttribut for field zusatzAttribute.
    """

    ausschreibungsdetail_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("ausschreibungsdetail.ausschreibungsdetail_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AusschreibungsloslieferstellenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Ausschreibungslos and Ausschreibungsdetail for field lieferstellen.
    """

    ausschreibungslos_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("ausschreibungslos.ausschreibungslos_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    ausschreibungsdetail_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("ausschreibungsdetail.ausschreibungsdetail_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class AusschreibungsloszusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Ausschreibungslos and ZusatzAttribut for field zusatzAttribute.
    """

    ausschreibungslos_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("ausschreibungslos.ausschreibungslos_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class BetragzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Betrag and ZusatzAttribut for field zusatzAttribute.
    """

    betrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("betrag.betrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class DienstleistungzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Dienstleistung and ZusatzAttribut for field zusatzAttribute.
    """

    dienstleistung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("dienstleistung.dienstleistung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class EnergieherkunftzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Energieherkunft and ZusatzAttribut for field zusatzAttribute.
    """

    energieherkunft_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("energieherkunft.energieherkunft_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class EnergiemixanteilLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Energiemix and Energieherkunft for field anteil.
    """

    energiemix_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("energiemix.energiemix_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    energieherkunft_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("energieherkunft.energieherkunft_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class EnergiemixzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Energiemix and ZusatzAttribut for field zusatzAttribute.
    """

    energiemix_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("energiemix.energiemix_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class FremdkostenblockkostenpositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Fremdkostenblock and Fremdkostenposition for field kostenpositionen.
    """

    fremdkostenblock_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("fremdkostenblock.fremdkostenblock_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    fremdkostenposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("fremdkostenposition.fremdkostenposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class FremdkostenblockzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Fremdkostenblock and ZusatzAttribut for field zusatzAttribute.
    """

    fremdkostenblock_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("fremdkostenblock.fremdkostenblock_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class FremdkostenpositionzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Fremdkostenposition and ZusatzAttribut for field zusatzAttribute.
    """

    fremdkostenposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("fremdkostenposition.fremdkostenposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class GeokoordinatenzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Geokoordinaten and ZusatzAttribut for field zusatzAttribute.
    """

    geokoordinaten_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geokoordinaten.geokoordinaten_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KatasteradressezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Katasteradresse and ZusatzAttribut for field zusatzAttribute.
    """

    katasteradresse_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("katasteradresse.katasteradresse_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KontaktwegzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Kontaktweg and ZusatzAttribut for field zusatzAttribute.
    """

    kontaktweg_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kontaktweg.kontaktweg_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KonzessionsabgabezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Konzessionsabgabe and ZusatzAttribut for field zusatzAttribute.
    """

    konzessionsabgabe_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("konzessionsabgabe.konzessionsabgabe_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KostenblockkostenpositionenLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Kostenblock and Kostenposition for field kostenpositionen.
    """

    kostenblock_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kostenblock.kostenblock_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    kostenposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kostenposition.kostenposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KostenblockzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Kostenblock and ZusatzAttribut for field zusatzAttribute.
    """

    kostenblock_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kostenblock.kostenblock_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KostenpositionzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Kostenposition and ZusatzAttribut for field zusatzAttribute.
    """

    kostenposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kostenposition.kostenposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class KriteriumWertzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables KriteriumWert and ZusatzAttribut for field zusatzAttribute.
    """

    kriteriumwert_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kriteriumwert.kriteriumwert_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MarktgebietInfozusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables MarktgebietInfo and ZusatzAttribut for field zusatzAttribute.
    """

    marktgebietinfo_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktgebietinfo.marktgebietinfo_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MengezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Menge and ZusatzAttribut for field zusatzAttribute.
    """

    menge_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("menge.menge_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class MesslokationszuordnungzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Messlokationszuordnung and ZusatzAttribut for field zusatzAttribute.
    """

    messlokationszuordnung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "messlokationszuordnung.messlokationszuordnung_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PositionsAufAbschlagzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables PositionsAufAbschlag and ZusatzAttribut for field zusatzAttribute.
    """

    positionsaufabschlag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("positionsaufabschlag.positionsaufabschlag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreiszusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Preis and ZusatzAttribut for field zusatzAttribute.
    """

    preis_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preis.preis_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisgarantiezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Preisgarantie and ZusatzAttribut for field zusatzAttribute.
    """

    preisgarantie_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisgarantie.preisgarantie_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreispositionpreisstaffelnLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Preisposition and Preisstaffel for field preisstaffeln.
    """

    preisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisposition.preisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    preisstaffel_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisstaffel.preisstaffel_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreispositionzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Preisposition and ZusatzAttribut for field zusatzAttribute.
    """

    preisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisposition.preisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class PreisstaffelzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Preisstaffel and ZusatzAttribut for field zusatzAttribute.
    """

    preisstaffel_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisstaffel.preisstaffel_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RechnungspositionzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Rechnungsposition and ZusatzAttribut for field zusatzAttribute.
    """

    rechnungsposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("rechnungsposition.rechnungsposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionaleGueltigkeitkriteriumsWerteLink(SQLModel, table=True):
    """
    class linking m-n relation of tables RegionaleGueltigkeit and KriteriumWert for field kriteriumsWerte.
    """

    regionalegueltigkeit_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionalegueltigkeit.regionalegueltigkeit_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    kriteriumwert_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("kriteriumwert.kriteriumwert_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionaleGueltigkeitzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables RegionaleGueltigkeit and ZusatzAttribut for field zusatzAttribute.
    """

    regionalegueltigkeit_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionalegueltigkeit.regionalegueltigkeit_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionalePreisgarantiezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables RegionalePreisgarantie and ZusatzAttribut for field zusatzAttribute.
    """

    regionalepreisgarantie_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "regionalepreisgarantie.regionalepreisgarantie_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionalePreisstaffelzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables RegionalePreisstaffel and ZusatzAttribut for field zusatzAttribute.
    """

    regionalepreisstaffel_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionalepreisstaffel.regionalepreisstaffel_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionalerAufAbschlagstaffelnLink(SQLModel, table=True):
    """
    class linking m-n relation of tables RegionalerAufAbschlag and RegionalePreisstaffel for field staffeln.
    """

    regionaleraufabschlag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionaleraufabschlag.regionaleraufabschlag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    regionalepreisstaffel_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionalepreisstaffel.regionalepreisstaffel_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionalerAufAbschlagzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables RegionalerAufAbschlag and ZusatzAttribut for field zusatzAttribute.
    """

    regionaleraufabschlag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionaleraufabschlag.regionaleraufabschlag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionaleTarifpreispositionpreisstaffelnLink(SQLModel, table=True):
    """
    class linking m-n relation of tables RegionaleTarifpreisposition and RegionalePreisstaffel for field preisstaffeln.
    """

    regionaletarifpreisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "regionaletarifpreisposition.regionaletarifpreisposition_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    regionalepreisstaffel_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionalepreisstaffel.regionalepreisstaffel_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionaleTarifpreispositionzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables RegionaleTarifpreisposition and ZusatzAttribut for field zusatzAttribute.
    """

    regionaletarifpreisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "regionaletarifpreisposition.regionaletarifpreisposition_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class RegionskriteriumzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Regionskriterium and ZusatzAttribut for field zusatzAttribute.
    """

    regionskriterium_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionskriterium.regionskriterium_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class SigmoidparameterzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Sigmoidparameter and ZusatzAttribut for field zusatzAttribute.
    """

    sigmoidparameter_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("sigmoidparameter.sigmoidparameter_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class StandorteigenschaftenGasmarktgebieteLink(SQLModel, table=True):
    """
    class linking m-n relation of tables StandorteigenschaftenGas and MarktgebietInfo for field marktgebiete.
    """

    standorteigenschaftengas_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "standorteigenschaftengas.standorteigenschaftengas_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    marktgebietinfo_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktgebietinfo.marktgebietinfo_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class StandorteigenschaftenGaszusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables StandorteigenschaftenGas and ZusatzAttribut for field zusatzAttribute.
    """

    standorteigenschaftengas_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "standorteigenschaftengas.standorteigenschaftengas_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class StandorteigenschaftenStromzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables StandorteigenschaftenStrom and ZusatzAttribut for field zusatzAttribute.
    """

    standorteigenschaftenstrom_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "standorteigenschaftenstrom.standorteigenschaftenstrom_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class SteuerbetragzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Steuerbetrag and ZusatzAttribut for field zusatzAttribute.
    """

    steuerbetrag_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("steuerbetrag.steuerbetrag_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifberechnungsparameterzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifberechnungsparameter and ZusatzAttribut for field zusatzAttribute.
    """

    tarifberechnungsparameter_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "tarifberechnungsparameter.tarifberechnungsparameter_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifberechnungsparameterzusatzpreiseLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifberechnungsparameter and Tarifpreis for field zusatzpreise.
    """

    tarifberechnungsparameter_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "tarifberechnungsparameter.tarifberechnungsparameter_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    tarifpreis_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifpreis.tarifpreis_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifeinschraenkungeinschraenkungleistungLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifeinschraenkung and Menge for field einschraenkungleistung.
    """

    tarifeinschraenkung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifeinschraenkung.tarifeinschraenkung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    menge_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("menge.menge_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifeinschraenkungeinschraenkungzaehlerLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifeinschraenkung and Geraet for field einschraenkungzaehler.
    """

    tarifeinschraenkung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifeinschraenkung.tarifeinschraenkung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    geraet_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geraet.geraet_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifeinschraenkungzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifeinschraenkung and ZusatzAttribut for field zusatzAttribute.
    """

    tarifeinschraenkung_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifeinschraenkung.tarifeinschraenkung_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifpreiszusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifpreis and ZusatzAttribut for field zusatzAttribute.
    """

    tarifpreis_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifpreis.tarifpreis_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifpreispositionpreisstaffelnLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifpreisposition and Preisstaffel for field preisstaffeln.
    """

    tarifpreisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifpreisposition.tarifpreisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    preisstaffel_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisstaffel.preisstaffel_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifpreispositionzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Tarifpreisposition and ZusatzAttribut for field zusatzAttribute.
    """

    tarifpreisposition_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifpreisposition.tarifpreisposition_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifpreispositionProOrtpreisstaffelnLink(SQLModel, table=True):
    """
    class linking m-n relation of tables TarifpreispositionProOrt and TarifpreisstaffelProOrt for field preisstaffeln.
    """

    tarifpreispositionproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "tarifpreispositionproort.tarifpreispositionproort_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    tarifpreisstaffelproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "tarifpreisstaffelproort.tarifpreisstaffelproort_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )


class TarifpreispositionProOrtzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables TarifpreispositionProOrt and ZusatzAttribut for field zusatzAttribute.
    """

    tarifpreispositionproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "tarifpreispositionproort.tarifpreispositionproort_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class TarifpreisstaffelProOrtzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables TarifpreisstaffelProOrt and ZusatzAttribut for field zusatzAttribute.
    """

    tarifpreisstaffelproort_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "tarifpreisstaffelproort.tarifpreisstaffelproort_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class UnterschriftzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Unterschrift and ZusatzAttribut for field zusatzAttribute.
    """

    unterschrift_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("unterschrift.unterschrift_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class VerbrauchzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Verbrauch and ZusatzAttribut for field zusatzAttribute.
    """

    verbrauch_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("verbrauch.verbrauch_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class VertragskonditionenzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Vertragskonditionen and ZusatzAttribut for field zusatzAttribute.
    """

    vertragskonditionen_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertragskonditionen.vertragskonditionen_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class VertragsteilzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Vertragsteil and ZusatzAttribut for field zusatzAttribute.
    """

    vertragsteil_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertragsteil.vertragsteil_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class VerwendungszweckProMarktrollezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables VerwendungszweckProMarktrolle and ZusatzAttribut for field zusatzAttribute.
    """

    verwendungszweckpromarktrolle_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "verwendungszweckpromarktrolle.verwendungszweckpromarktrolle_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZaehlwerkverwendungszweckeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zaehlwerk and VerwendungszweckProMarktrolle for field verwendungszwecke.
    """

    zaehlwerk_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlwerk.zaehlwerk_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    verwendungszweckpromarktrolle_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "verwendungszweckpromarktrolle.verwendungszweckpromarktrolle_sqlid",
                ondelete="CASCADE",
            ),
            primary_key=True,
        )
    )


class ZaehlwerkzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zaehlwerk and ZusatzAttribut for field zusatzAttribute.
    """

    zaehlwerk_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlwerk.zaehlwerk_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZaehlzeitregisterzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zaehlzeitregister and ZusatzAttribut for field zusatzAttribute.
    """

    zaehlzeitregister_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zaehlzeitregister.zaehlzeitregister_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZeitraumzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zeitraum and ZusatzAttribut for field zusatzAttribute.
    """

    zeitraum_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZeitreihenwertzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zeitreihenwert and ZusatzAttribut for field zusatzAttribute.
    """

    zeitreihenwert_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitreihenwert.zeitreihenwert_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZeitspannezusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zeitspanne and ZusatzAttribut for field zusatzAttribute.
    """

    zeitspanne_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitspanne.zeitspanne_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )


class ZustaendigkeitzusatzAttributeLink(SQLModel, table=True):
    """
    class linking m-n relation of tables Zustaendigkeit and ZusatzAttribut for field zusatzAttribute.
    """

    zustaendigkeit_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zustaendigkeit.zustaendigkeit_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
    zusatzattribut_id: Optional[uuid_pkg.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zusatzattribut.zusatzattribut_sqlid", ondelete="CASCADE"),
            primary_key=True,
        )
    )
