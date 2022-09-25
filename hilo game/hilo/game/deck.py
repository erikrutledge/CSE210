import random

class Deck:
    """A complete deck of 52 face cards. Act as a physical deck that can be drawn from.
    draw gives a value of 1-13 and can only have 4 of each number.
    
    Attributes:
        value (int): the number on the drawn card. (face cards are just represented with numbers 11,12, and 13.)
        deck (list[int]): the complete list of values for 52 cards in a deck.
    """
    
    full_deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]


    def __init__(self):
        """Constructs a new instance of a deck with all 52 cards to draw from.
        
        Args:
            self (Director): an instance of Director.
        """  
        self.deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
        self.value = 0
        self.drawn_cards = []

        
    def draw_card(self):
        """Generates a random number and removes the selected card from the deck.

        Args:
            self (Deck): An instance of Deck.
        """
        self.drawn_cards.append(self.value)
        self.deck.remove(self.value)
        if len(self.deck) == 0:
            print(f"Oops, you ran out of cards! Your final score is {self.total_score}\n\n")
            exit()
        self.value = random.choice(self.deck)