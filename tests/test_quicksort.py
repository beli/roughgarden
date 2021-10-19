from quicksort import qsort
from hypothesis import given, strategies as st


@given(st.lists(st.integers()))
def test_qsort(l):
    l1 = sorted(l)
    qsort(l)
    l2 = l
    assert l1 == l2
