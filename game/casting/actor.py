from game.casting.text import Text


class Actor:
    """A thing that participates in the game."""
    
    def __init__(self):
        """Constructs a new Actor using the given group and id.
        
        Args:
            group: A string containing the actor's group name.
            id: A number that uniquely identifies the actor within the group.
        """
        
