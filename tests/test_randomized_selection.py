from random import randint
from randomized_selection import select
from hypothesis import given, strategies as st


@given(st.lists(st.integers(), min_size=1))
def test_select(l):
    o = randint(1, len(l))
    assert select(l, o) == sorted(l)[o - 1]
