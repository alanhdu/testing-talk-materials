from ..unit import mean


def test_merge_sort():
    assert mean([1, 2, 3]) == 2.0
    assert mean([-1.5, 0, 1.5]) == 0
