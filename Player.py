class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 0

    def add_card(self, card):
        self.hand.append(card)

    def bet(self, amount):
        if amount <= self.chips:
            self.chips -= amount
            return amount
        else:
            return 0  
