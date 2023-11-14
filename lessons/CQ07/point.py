"""Intro to Object Oriented Programming!"""

from __future__ import annotations

__author__ = "730706009"


class Point:
    """Creating a new class of Point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Defining the constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Function definition to scale the points."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Function scales the original point to create a new point."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Magic method to print out points in a readable way."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int | float) -> Point:
        """Overloading the multiplication * operator."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, factor: int | float) -> Point:
        """Overloading the addition + operator."""
        return Point(self.x + factor, self.y + factor)