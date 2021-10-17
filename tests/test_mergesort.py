import mergesort


def test_merge():
    assert mergesort.merge([1, 2], [3, 4, 5]) == [1, 2, 3, 4, 5]


def test_sort():
    assert mergesort.sort([3, 2, 1]) == [1, 2, 3]
