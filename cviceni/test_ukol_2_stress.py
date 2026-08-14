import pytest
from hypothesis import given, settings, strategies as st

from ukol_2 import pocet_sudych


@settings(max_examples=10000, deadline=None)
@given(st.integers(min_value=1, max_value=100_000))
def test_pocet_sudych_kladna_cisla(n):
    assert pocet_sudych(n) == n // 2


@settings(max_examples=10000, deadline=None)
@given(st.integers(min_value=-100_000, max_value=0))
def test_pocet_sudych_nekladna_cisla_vraci_nulu(n):
    assert pocet_sudych(n) == 0


@settings(max_examples=10000, deadline=None)
@given(st.one_of(st.text(), st.floats(), st.none(), st.lists(st.integers())))
def test_pocet_sudych_spatny_typ_vyhodi_typeerror(n):
    with pytest.raises(TypeError):
        pocet_sudych(n)
