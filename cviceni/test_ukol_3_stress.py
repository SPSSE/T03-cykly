import math

import pytest
from hypothesis import given, settings, strategies as st

from ukol_3 import faktorial


@settings(max_examples=10000, deadline=None)
@given(st.integers(min_value=0, max_value=500))
def test_faktorial_nezaporna_cisla(n):
    assert faktorial(n) == math.factorial(n)


@settings(max_examples=10000, deadline=None)
@given(st.integers(min_value=-100_000, max_value=-1))
def test_faktorial_zaporna_cisla_vyhodi_valueerror(n):
    with pytest.raises(ValueError):
        faktorial(n)
