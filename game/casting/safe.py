from game.casting.actor import Actor


class Safe(Actor):
    #A solid, rectangular object that can be walked on.

    def __init__(self, body):
        #Constructs a new Platform.
        #Args: body: A new instance of Body.
        self._body = body

    def get_body(self):
        #Gets the platform's body.
        #Returns: An instance of Body.
        return self._body