from quicksort import qsort
from hypothesis import given, strategies as st


@given(st.lists(st.integers()))
def test_qsort(l):
    sorted_l = sorted(l)
    qsort(l)
    assert l == sorted_l
