from credit import calculate_risk


# ---------- Partie A : cas normaux ----------

def test_high_risk():
    result = calculate_risk(1000, 700, 30)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400, 30)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100, 30)
    assert result == "LOW"


# ---------- Partie B : cas limites et entrees invalides ----------

def test_zero_income():
    assert calculate_risk(0, 500, 30) == -1


def test_negative_income():
    assert calculate_risk(-1000, 500, 30) == -1


def test_zero_debt():
    assert calculate_risk(1000, 0, 30) == "LOW"


def test_ratio_exactly_0_3():
    # 300 / 1000 = 0.3 -> pas strictement > 0.3 -> LOW
    assert calculate_risk(1000, 300, 30) == "LOW"


def test_ratio_exactly_0_6():
    # 600 / 1000 = 0.6 -> pas strictement > 0.6 -> MEDIUM
    assert calculate_risk(1000, 600, 30) == "MEDIUM"


def test_invalid_age():
    assert calculate_risk(1000, 500, 0) == -1
