from abc import ABC, abstractmethod

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

    @abstractmethod
    def decide_action(self):
        pass
