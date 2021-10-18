import inversions, naive_inversions
from hypothesis import given, strategies as st


@given(st.lists(st.integers()))
def test_count(l):
    assert inversions.count(l)[0] == naive_inversions.count(l)
