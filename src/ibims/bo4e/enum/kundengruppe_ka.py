from enum import Enum


class KundengruppeKA(str, Enum):
    """
    Eine AufzÃ¤hlung zur Einordnung fÃ¼r die HÃ¶he der Konzessionsabgabe.
    """

    S_SCHWACHLAST = "S_SCHWACHLAST"
    S_TARIF_25000 = "S_TARIF_25000"
    S_TARIF_100000 = "S_TARIF_100000"
    S_TARIF_500000 = "S_TARIF_500000"
    S_TARIF_G_500000 = "S_TARIF_G_500000"
    S_SONDERKUNDE = "S_SONDERKUNDE"
    G_KOWA_25000 = "G_KOWA_25000"
    G_KOWA_100000 = "G_KOWA_100000"
    G_KOWA_500000 = "G_KOWA_500000"
    G_KOWA_G_500000 = "G_KOWA_G_500000"
    G_TARIF_25000 = "G_TARIF_25000"
    G_TARIF_100000 = "G_TARIF_100000"
    G_TARIF_500000 = "G_TARIF_500000"
    G_TARIF_G_500000 = "G_TARIF_G_500000"
    G_SONDERKUNDE = "G_SONDERKUNDE"
    SONDER_KAS = "SONDER_KAS"
    SONDER_SAS = "SONDER_SAS"
    SONDER_TAS = "SONDER_TAS"
    SONDER_TKS = "SONDER_TKS"
    SONDER_TSS = "SONDER_TSS"
