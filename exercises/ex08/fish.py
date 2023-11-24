"""File to define Fish class."""

__author__ = "730706009"


class Fish:
    """Writing functions to define class for fish."""
    def __init__(self):
        """Starting aage of fish is 0."""
        self.age = 0
    
    def one_day(self):
        """Increase the age of the fish by 1."""
        self.age += 1