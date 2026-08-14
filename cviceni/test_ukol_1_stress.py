import pytest
from hypothesis import given, settings, strategies as st

from ukol_1 import soucet_do_n


@settings(max_examples=10000, deadline=None)
@given(st.integers(min_value=1, max_value=100_000))
def test_soucet_do_n_kladna_cisla(n):
    assert soucet_do_n(n) == n * (n + 1) // 2


@settings(max_examples=10000, deadline=None)
@given(st.integers(min_value=-100_000, max_value=0))
def test_soucet_do_n_nekladna_cisla_vraci_nulu(n):
    assert soucet_do_n(n) == 0


@settings(max_examples=10000, deadline=None)
@given(st.one_of(st.text(), st.floats(), st.none(), st.lists(st.integers())))
def test_soucet_do_n_spatny_typ_vyhodi_typeerror(n):
    with pytest.raises(TypeError):
        soucet_do_n(n)
