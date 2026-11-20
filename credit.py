"""Calcul du niveau de risque de credit d'un client."""

HIGH_RISK_THRESHOLD = 0.6
MEDIUM_RISK_THRESHOLD = 0.3
INVALID_INPUT = -1


def calculate_risk(income, debt, age):
    """Retourne "HIGH", "MEDIUM" ou "LOW" selon le ratio dette / revenu.

    Retourne INVALID_INPUT (-1) si le revenu ou l'age n'est pas valide.
    """
    if income <= 0 or age <= 0:
        return INVALID_INPUT

    ratio = debt / income

    if ratio > HIGH_RISK_THRESHOLD:
        return "HIGH"
    if ratio > MEDIUM_RISK_THRESHOLD:
        return "MEDIUM"
    return "LOW"
