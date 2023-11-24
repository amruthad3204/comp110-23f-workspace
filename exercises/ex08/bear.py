"""File to define Bear class."""

__author__ = "730706009"


class Bear:
    """Defining the functions to create the class for bear."""
    def __init__(self):
        """Setting base age and hunger score."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Simulate one day in the life of a Bear."""
        self.hunger_score -= 1
        self.age += 1

    def eat(self, num_fish: int):
        """Bear eats num_fish, updating hunger score."""
        self.hunger_score += num_fish