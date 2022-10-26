from game.casting.actor import Actor


class Flag(Actor):
    # The goal, a flag to be reached.

    def __init__(self, body):
        #Constructs a new Flag.
        #Args: body: A new instance of Body. 
        self._body = body

    def get_body(self):
        #Gets the flag's body.
        #Returns: An instance of Body.
        return self._body