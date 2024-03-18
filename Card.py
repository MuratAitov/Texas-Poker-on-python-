class Card:
    def __init__(self, suit, value):
        self.suit = suit  # Масть карты ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        self.value = value  # Значение карты ('2', '3', ..., '10', 'Jack', 'Queen', 'King', 'Ace')

    def __repr__(self): # Вывод карты как стринг 
        return f"{self.value} of {self.suit}"
