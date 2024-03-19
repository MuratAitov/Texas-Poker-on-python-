class Player:
    def __init__(self):
        self.open_cards = []
        self.bank = 0

    def add_card(self, card):
        self.open_cards.append(card)