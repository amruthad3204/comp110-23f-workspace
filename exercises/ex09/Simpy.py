"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730706009"


class Simpy:
    """Simpy class represents a simple array of float values."""
    values: list[float]

    def __init__(self, values: list[float]) -> None: 
        """Constructor for Simpy class."""
        self.values = values

    def __str__(self) -> str:
        """String representation of Simpy object. Returns a string in the format "Simpy([...])"."""
        return f"Simpy({self.values})"

    def fill(self, new_val: float, num_val: int) -> None:
        """Fill Simpy's values with a specific number of repeating values."""
        self.values = []
        while len(self.values) < num_val:
            self.values.append(new_val)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with a range of float values."""
        assert step != 0.0
        self.values = []
        current_val: float = start
        while current_val != stop:
            self.values.append(current_val)
            current_val += step

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        sum_val: float = sum(self.values)
        return sum_val

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the addition operator (+) for Simpy objects and floats. Returns a new Simpy object with values corresponding to the addition."""
        self.rhs = rhs
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            result_values = [self.values[i] + rhs.values[i] for i in range(len(self.values))]
        if type(rhs) is float:
            result_values = [self.values[i] + rhs for i in range(len(self.values))]
        return Simpy(result_values)
    
    def __pow__(self, exponent: Union[float, Simpy]) -> Simpy:
        """Overload the power operator (**) for Simpy objects and floats. Returns a new Simpy object with values corresponding to the exponentiation."""
        self.exponent = exponent
        if type(exponent) is Simpy:
            assert len(self.values) == len(exponent.values)
            result_values = [self.values[i] ** exponent.values[i] for i in range(len(self.values))]
        if type(exponent) is float:
            result_values = [self.values[i] ** exponent for i in range(len(self.values))]
        return Simpy(result_values)

    def __eq__(self, equal: Union[float, Simpy]) -> list[bool]:
        """Overload the equality operator (==) for Simpy objects and floats. Returns a list of boolean values indicating equality."""
        if type(equal) is Simpy:
            assert len(self.values) == len(equal.values)
            result_values = [self.values[i] == equal.values[i] for i in range(len(self.values))]
        if type(equal) is float:
            result_values = [self.values[i] == equal for i in range(len(self.values))]
        return result_values

    def __gt__(self, compare: Union[float, Simpy]) -> list[bool]:
        """Overload the greater than operator (>) for Simpy objects and floats. Returns a list of boolean values indicating greater than relationship."""
        if type(compare) is Simpy:
            assert len(self.values) == len(compare.values)
            result_values = [self.values[i] > compare.values[i] for i in range(len(self.values))]
        if type(compare) is float:
            result_values = [self.values[i] > compare for i in range(len(self.values))]
        return result_values

    def __getitem__(self, idx: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription operator ([]). Returns a specific item if rhs is an int, or a new Simpy object based on a mask if rhs is a list of bool."""
        if type(idx) is int:
            return self.values[idx]
        if type(idx) is list:
            return Simpy([self.values[i] for i in range(len(self.values)) if idx[i]])










# Test Part 0
# ones = Simpy([1., 1., 1., 1., 1.])
# print(ones.values)

# Test Part 1
# print(ones)

# Test Part 2
# twos = Simpy([])
# twos.fill(2.0, 3)
# print("Actual: ", twos, " - Expected: Simpy([2.0, 2.0, 2.0])")
# twos.fill(2.0, 5)
# print("Actual: ", twos, " - Expected: Simpy([2.0, 2.0, 2.0, 2.0, 2.0])")

# mixed = Simpy([])
# mixed.fill(3.0, 3)
# print("Actual: ", mixed, " - Expected: Simpy([3.0, 3.0, 3.0])")
# mixed.fill(2.0, 2)
# print("Actual: ", mixed, " - Expected: Simpy([2.0, 2.0])")

# Test Part 3
# positive = Simpy([])
# positive.arange(1.0, 5.0)
# print("Actual: ", positive, " - Expected: Simpy([1.0, 2.0, 3.0, 4.0])")

# ractional = Simpy([])
# fractional.arange(0.0, 1.0, 0.25)
# print("Actual: ", fractional, " - Expected: Simpy([0.0, 0.25, 0.5, 0.75])")

# negative = Simpy([])
# negative.arange(-1.0, -5.0, -1.0)
# print("Actual: ", negative, " - Expected: Simpy([-1.0, -2.0, -3.0, -4.0])")

# Test Part 4
# ones = Simpy([1.0, 1.0, 1.0])
# print("Actual: ", ones.sum(), " - Expected: 3.0")

# one_to_nine = Simpy([])
# one_to_nine.arange(1.0, 10.0)
# rint("Actual: ", one_to_nine.sum(), " - Expected: 45.0")

# Test Part 5
# a = Simpy([1.0, 1.0, 1.0])
# b = Simpy([2.0, 3.0, 4.0])
# c = a + b
# print("Actual: ", c, " - Expected: Simpy([3.0, 4.0, 5.0])")
# print("Actual: ", a + a, " - Expected: Simpy([2.0, 2.0, 2.0])")
# print("Actual: ", b + b, " - Expected: Simpy([4.0, 6.0, 8.0])")

# a = Simpy([1.0, 2.0, 3.0])
# b = a + 10.0
# print("Actual: ", b, " - Expected: Simpy([11.0, 12.0, 13.0])")
# print("Actual: ", a + 1.0, " - Expected: Simpy([2.0, 3.0, 4.0])")

# Test Part 6
# a = Simpy([2.0, 2.0, 2.0])
# b = Simpy([1.0, 2.0, 3.0])
# c = a ** b
# print("Actual: ", c, " - Expected: Simpy([2.0, 4.0, 8.0])")
# print("Actual: ", a ** a, " - Expected: Simpy([4.0, 4.0, 4.0])")
# print("Actual: ", b ** b, " - Expected: Simpy([1.0, 4.0, 27.0])")

# = Simpy([1.0, 2.0, 3.0])
# b = a ** 2.0
# print("Actual: ", b, " - Expected: Simpy([1.0, 4.0, 9.0])")
# Print("Actual: ", a ** 3.0, " - Expected: Simpy([1.0, 8.0, 27.0])")

# Test Check #1 for Understanding
# result = Simpy([]).arange(0.0, 16.0).pow(2.0)
# print("Actual: ", result, " - Expected: Simpy([1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0])")

# Test Part 7
# a = Simpy([1.0, 2.0, 3.0, 4.0])
# b = Simpy([1.0, 2.0, 1.0, 4.0])
# c = a == b
# print("Actual: ", c, " - Expected: [True, True, False, True]")
# print("Actual: ", a == a, " - Expected: [True, True, True, True]")

# a = Simpy([1.0, 2.0, 1.0, 4.0])
# b = a == 1.0
# print("Actual: ", b, " - Expected: [True, False, True, False]")
# print("Actual: ", a == 2.0, " - Expected: [False, True, False, False]")

# Test Part 8
# a = Simpy([1.0, 2.0, 3.0, 4.0])
# b = Simpy([2.0, 1.0, 1.0, 5.0])
# c = a > b
# print("Actual: ", c, " - Expected: [False, True, True, False]")
# print("Actual: ", b > a, " - Expected: [True, False, False, True]")

# a = Simpy([1.0, 2.0, 3.0, 4.0])
# b = a > 2.0
# print("Actual: ", b, " - Expected: [False, False, True, True]")
# print("Actual: ", a > 3.0, " - Expected: [False, False, False, True]")

# Test Part 9
# a = Simpy([10.0, 20.0, 30.0])
# print("Actual: ", a[0], " - Expected: 10.0")
# print("Actual: ", a[1], " - Expected: 20.0")
# print("Actual: ", a[2], " - Expected: 30.0")

# Test Part 10
# a = Simpy([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
# b = a[a > 2.0]
# print("Actual: ", b, " - Expected: Simpy([3.0, 4.0])")
# print("Actual: ", a[a + 1.0 == 2.0], " - Expected: Simpy([1.0, 1.0])")