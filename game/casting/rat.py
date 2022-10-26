#The purpose of this class is to initialize and handl all interactions with the rat.
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Rat(Actor):

    def __init__(self, body):
        # Constructs a new rat.
        # Args: body: A new instance of Body.
        self._body = body

    def get_body(self):
        # Gets the rat's body.
        # Returns: and instance of Body.
        return self._body

    def move_next(self):
        # Moves the rat using its velocity.
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_left(self):
        # Steers the rat to the left.
        velocity = Point(-RAT_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def move_right(self):
        # Steers the rat to the right.
        velocity = Point(RAT_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def gravity(self):
        # Pulls the rat down at a contstant rate.
        velocity = self._body.get_velocity()
        vx = velocity.get_x()
        vy = velocity.get_y()
        vy += RAT_GRAVITY
        velocity = Point(vx,vy)
        self._body.set_velocity(velocity)

    def jump(self):
        # Makes the rat move upward for a moment.
        # if player is grounded
            velocity = self._body.get_velocity()
            vx = velocity.get_x()
            velocity = Point(vx,RAT_JUMP)
            self._body.set_velocity(velocity)
        
    def stop_moving(self):
        # Stops the rat from moving.
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)


