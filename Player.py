from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 1000

    def add_card(self, card):
        self.hand.append(card)

    def bet(self, amount):
        if amount <= self.chips:
            self.chips -= amount
            return amount
        else:
            return 0
        
    def fold(self):
        pass 

    @abstractmethod
    def decide_action(self):
        pass

class RandomPlayer(Player):
    def decide_action(self):
        return random.choice(['fold', 'call', 'raise']), random.randint(1, self.chips)

