import game.parachute, game.words

class Director:
    """ A person who directs the game.
    The responsability of a director is to control the sequence of play.

    Attributes:
        word (Words): a single instance of a random word.
        wordlist (list[str]): the word variable separated out into a list of letters.
        strikes (int): a running value of mistakes that starts at 0 and ends the game at 5.
        guesses (list[str]): a list of all the past guesses.
        correct_guesses (list[str]): the display shown to the user that is updated with correct letters as they are guessed.
        is_playing (boolean): Whether or not the game is being played.
    """
    def __init__(self):
        """ Constructs a new Director
        Args: self (Director): an instance of Director
        """
        self.word = game.words.Words.random_word()
        self.wordlist = list(self.word)
        self.strikes = 0
        self.guesses = []
        self.correct_guesses = ["_","_","_","_","_"]
        self.is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.compare_inputs()
            self.update_display()
            self.display_parachute()


    def get_inputs(self):
        """Asks the user to guess any letter a-z.
        Args: self (Director): An instance of Director.
        """
        print(f"Previous guesses: {self.guesses}")
        self.guess = input("Guess a letter [a-z]: ")
        self.guesses.append(self.guess)


    def compare_inputs(self):
        """Compares the guessed letter to the randomly generated word and updated the variables accordingly
        Args: self (Director): An instance of Director
        """
        if self.guess in self.wordlist:
            indices = [i for i,x in enumerate(self.wordlist) if x==self.guess]
            for i in indices:
                self.correct_guesses[i] = self.guess
        else:
            print("\nSorry that letter is not in the word!")
            self.strikes += 1
            if self.strikes == 5:
                game.parachute.Parachute.display_parachute(5)
                print(f"The word was '{self.word}'")
                exit()
        if self.correct_guesses == self.wordlist:
            print(f"\n{self.wordlist}")
            print(f"Well done, you win! The word was '{self.word}'")
            exit()

    def update_display(self):
        """Updates and shows the new display to the user.
        Args: self (Director): An instance of Director
        """
        print(f"\n{self.correct_guesses}")


    def display_parachute(self):
        """Displays the new parachute depending on the result of the previous guess.
        Args: self (Director): An instance of Director.
        """
        game.parachute.Parachute.display_parachute(self.strikes)