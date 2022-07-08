from random import randint
from randomized_selection import select
from hypothesis import given, strategies as st


@given(st.lists(st.integers(), min_size=1))
def test_select(sequence):
    order = randint(1, len(sequence))
    assert select(sequence, order) == sorted(sequence)[order - 1]
