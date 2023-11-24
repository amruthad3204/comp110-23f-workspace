"""File to define River class!"""

__author__ = "730706009"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River: 
    """Creating the class for river."""
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove animals from the River based on their age."""
        # Remove Fish older than 3
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        # Remove Bears older than 5
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int):
        """Remove the frontmost Fish from the River."""
        for _ in range(min(amount, len(self.fish))):
            self.fish.pop(0)

    def bears_eating(self):
        """Bears eat Fish. Adjust fish population accordingly."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # Bear eats 3 Fish
                bear.eat(3)  # Increase bear's hunger_score by 3
    
    def check_hunger(self):
        """Remove hungry Bears from the River."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        
    def repopulate_fish(self):
        """Repopulate Fish in the River."""
        n = len(self.fish) // 2 * 4
        for x in range(0, n): 
            self.fish.append(Bear())
        return None
    
    def repopulate_bears(self):
        """Repopulate Bears in the River."""
        new_bears = []
        for i in range(0, len(self.bears), 2):
            # Each pair of Bears produces 1 offspring
            new_bears.append(Bear())
        self.bears.extend(new_bears)
    
    def view_river(self):
        """Print the river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}\n")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        for _ in range(7):
            # Simulate one day for all Bears
            for bear in self.bears:
                bear.one_day()
            # Simulate one day for all Fish
            for fish in self.fish:
                fish.one_day()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.one_river_day()
        # Increase day by 1
        self.day += 1
        # Update day attribute to 7 at the end of the week
        self.day = 7
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()