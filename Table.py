from Deck import* 
from Player import* 

class Table:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.community_cards = []
        self.pot = 0
        self.current_bets = 0

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def deal_hole_cards(self):
        for player in self.players:
            player.add_card(self.deck.deal_card())
            player.add_card(self.deck.deal_card())

    def flop(self):
        # Сжигаем одну карту
        self.deck.deal_card()
        # Раздаём флоп
        for _ in range(3):
            self.community_cards.append(self.deck.deal_card())

    def turn_or_river(self):
        # Сжигаем одну карту
        self.deck.deal_card()
        # Раздаём терн или ривер
        self.community_cards.append(self.deck.deal_card())

    def collect_bets(self, amount):
        for player in self.players:
            bet = player.bet(amount)
            self.pot += bet
            self.current_bets += bet

    def distribute_pot(self, winner):
        winner.chips += self.pot
        self.pot = 0
        self.current_bets = 0

    def show_down(self):
        pass

    def reset_round(self):
        self.community_cards.clear()
        self.pot = 0
        self.current_bets = 0
        for player in self.players:
            player.hand.clear()
        self.deck = Deck()  
