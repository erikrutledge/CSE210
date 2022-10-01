class Parachute:
    """A drawing of a man parachuting with 6 stages of destruction. Phases 0-4 show varying degrees of strings being
    cut, with the final stage depicting him on the ground.
    
    Attributes:
        count (int): the number determining the what phase the parachute is in."""

    def __init__(self):
        """Constructs a new instance of a parachute complete with all 5 strings.
        Args: self (Director): an instance of Director
        """
        print("  ___________\n /___________\ \n \  \  |  /  /\n  \_ \ | / _/\n    \ \|/ /\n      \|/\n       O")


    def display_parachute(count):
        """displays a parachute with varying degrees of wear determined by count.
        Args: count (int): A number from 0-5 representing the different phases of the parachute.
        """
        if count == 0:
            print("  ___________\n /___________\ \n \  \  |  /  /\n  \_ \ | / _/\n    \ \|/ /\n      \|/\n       O\n")
        elif count == 1:
            print("  ___________\n /___________\ \n    \  |  /  /\n     \ | / _/\n      \|/ /\n      \|/\n       O\n")
        elif count == 2:
            print("  ___________\n /___________\ \n       |  /  /\n       | / _/\n       |/ /\n       |/\n       O\n")
        elif count == 3:
            print("  ___________\n /___________\ \n       |  /\n       | /\n       |/\n       |\n       O\n")
        elif count == 4:
            print("  ___________\n /___________\ \n       |\n       |\n       |\n       |\n       O\n")
        elif count == 5:
            print("\n\n   GAME OVER.\nPlease try again.\n\n_______X_______\n")
        else:
            print("something went wrong displaying your parachute, please try again.")

