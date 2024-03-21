
class PokerHandEvaluator: 
    def __init__(self): 
        
        self.hand_ranks = {
            "High Card": 0,
            "Pair": 1,
            "Two Pair": 2,
            "Three of a Kind": 3,
            "Straight": 4,
            "Flush": 5,
            "Full House": 6,
            "Four of a Kind": 7,
            "Straight Flush": 8,
            "Royal Flush": 9
        }

    def evaluate_hand(self,hand):
        


        
        # values = [card.value for card in hand]
        # value_counts = {value: values.count(value) for value in set(values)}
        # pairs = [value for value, count in value_counts.items() if count == 2]
        
        if combination == "Pair":
            return (self.hand_ranks["Pair"])
        
        if combination == "Two Pair":
            return (self.hand_ranks["Two Pair"])
        

        return (self.hand_ranks["High Card"], hand[0].value)
