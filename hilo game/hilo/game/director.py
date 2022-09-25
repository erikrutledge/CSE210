from game.deck import Deck
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deck (Deck): A single instance of the Deck object.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The number of points 
        total_score (int): The running total score for the game.
        value (int): The value on each card, 1-13.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.deck = Deck.full_deck
        self.value = random.randint(1,13)
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.drawn_cards = []
        self.selection = "starting value"


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            Deck.draw_card(self)
            self.display_card()
            self.calculate_score()
            self.update_score()
            self.check_exit_conditions()
            self.retry()
    
    def get_inputs(self):
        """Ask the user if the next card will be higher or lower.

        Args:
            self (Director): An instance of Director.
        """ 
        print(f"\nThe current card is: {self.value}")
        self.selection = input("Is the next card going to be higher or lower? [h,l] ").lower()

    def display_card(self):
        print(f"The new card is: {self.value}")

    def calculate_score(self):
        if self.selection == 'h':
            if self.value > self.drawn_cards[-1]:
                self.score = 100
                print("Well done! You gain 100 points.")
            elif self.value < self.drawn_cards[-1]:
                self.score = -75
                print("Bad luck... You lose 75 points.")
            elif self.value == self.drawn_cards[-1]:
                self.score = -75
                print("What are the odds of that!? You lose 75 points.")
        elif self.selection == 'l':
            if self.value < self.drawn_cards[-1]:
                self.score = 100
                print("Well done! You gain 100 points.")
            elif self.value > self.drawn_cards[-1]:
                self.score = -75
                print("Bad luck... You lose 75 points.")
            elif self.value == self.drawn_cards[-1]:
                self.score = -75
                print("What are the odds of that!? You lose 75 points.")
        else:
            print("Sorry, I didn't understand that, please try again.")
        
    def update_score(self):
        self.total_score += self.score

    def check_exit_conditions(self):
        """Checks all the end conditions to see when the game ends.

        Args:
            self (Director): An instance of Director.
        """        
        if self.is_playing == False:
            print("Thanks for playing!\n\n")
            exit()
        else:
            return
    
    def retry(self):
        print(f"Your score is now: {self.total_score}")
        retry = input("Would you like to keep playing? [y/n] ")
        if retry == "n":
            print("\nThanks for playing, please try again soon!\n\n")
            exit()
        else:
            return
