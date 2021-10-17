import inversions

def test_merge():
    assert inversions.merge([1,2,3,4,5], [1,6,7]) == (4, [1,1,2,3,4,5,6,7])

def test_count():
    assert inversions.count([1,2,3,4,5,1,6,7]) == (4, [1,1,2,3,4,5,6,7])