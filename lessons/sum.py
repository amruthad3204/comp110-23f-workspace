"""Summing the elements of a list using different loop."""

__author__ = "730706009"


def w_sum(vals: list[float]) -> float: 
    """Using a while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len[vals]:
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float: 
    """Using a for loop."""
    sum: float = 0.0 
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list([float])) -> float: 
    """Using for loop + range."""
    sum: float = 0.0
    for idx in range(0, len(vals)): 
        sum += vals[idx]
    return sum