from Deck import*
import pygame

class Game:
    def __init__(self, players):
        self.deck = Deck()  
        self.players = players 
        self.pot = 0  
        self.current_bet = 0  

    def start_new_round(self):
        self.deck.shuffle()
        self.current_bet = 0

    def handle_bets(self):
        pass

    def determine_winner(self):
        pass

    def distribute_pot(self):
        pass
    
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))  

