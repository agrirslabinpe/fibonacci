"""Module with functions for computing the Nth Fibonacci number.

In all cases it is expected that N >= 0.
"""

import numpy as np


def compute(n: int) -> int:
    xi = 0
    xj = 1
    xn = xi + xj

    if n <= 1:
        if n == 0:
            xn = xi
        else:
            xn = xj
    else:
        for i in range(2, n):
            xi = xj
            xj = xn
            xn = xi + xj


    return xn


def compute_direct(n: int) -> int:
    """
    Notes
    -----
    This is an exact formula for computing fibonacci numbers, but due to
    representation limitations for irrational numbers it might return numbers 
    with small numerical flutuations. We could avoid this behavior easily by
    rounding the result, i.e. np.round(result, 0)
    """


    golden_number = (1 + np.sqrt(5)) / 2

    return (golden_number ** n - (1 - golden_number) ** n) / np.sqrt(5)
