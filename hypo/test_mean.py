from hypothesis import given
from hypothesis.strategies import floats, lists


@given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean(xs):
    mean = sum(xs) / len(xs)
    assert min(xs) <= mean <= max(xs)
