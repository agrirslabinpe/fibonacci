import pytest

from fibonacci import fibonacci


accepted_error = 1e6

testdata = [
    #(input value, expected value),
    (0, 0),
    (2, 1),
    (5, 5),
    (10, 55),
    (13, 233),
    (15, 610),
]

@pytest.mark.parametrize("input, expected", testdata)
def test_compute(input, expected):

    assert fibonacci.compute(input) == expected

# Using an accepted error for asserting the correctness
@pytest.mark.parametrize("input, expected", testdata)
def test_compute_direct(input, expected):

    assert fibonacci.compute_direct(input) == pytest.approx(expected, accepted_error)
