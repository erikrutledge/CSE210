from game.casting.actor import Actor


class Artifact(Actor):
    
    def __init__(self):
        super().__init__()

    def set_value(self, value):
        """Updates the value.

        Args: value(int): The given value of each object
        """
        self.value = value

    def get_value(self):
        """Gets the actor's value
        
        Returns:
            value(int): The object's value.
        """
        return self.value
    