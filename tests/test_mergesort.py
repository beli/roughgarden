import mergesort
from hypothesis import given, strategies as st


@given(st.lists(st.integers()))
def test_sort(l):
    assert mergesort.sort(l) == sorted(l)
