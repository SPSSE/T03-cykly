from ukol_3 import faktorial


def test_faktorial_peti():
    assert faktorial(5) == 120


def test_faktorial_nuly():
    assert faktorial(0) == 1


def test_faktorial_jednicky():
    assert faktorial(1) == 1
