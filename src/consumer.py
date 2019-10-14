"""

"""

class OddsAndEvensCounter:
    """
    
    """
    def __init__(self):
        self.evens_count = 0
        self.odds_count = 0

    def count(self, num):
        self.odds_count = self.odds_count + (num)%2
        self.evens_count = self.evens_count + (num + 1)%2
        
    def __repr__(self):
        return f'odd: {self.odds_count} even: {self.evens_count}'