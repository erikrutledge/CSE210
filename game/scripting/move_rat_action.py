from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRatAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        rat = cast.get_first_actor(RAT_GROUP)
        body = rat.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        x = position.get_x()

        position = position.add(velocity)
        body.set_position(position)


# ADD WALLS TO PREVENT LEAVING THE SCREEN
        # if x < 0:
        #     position = Point(0, position.get_y())
        # elif x > (SCREEN_WIDTH - RAT_WIDTH):
        #     position = Point(SCREEN_WIDTH - RAT_WIDTH, position.get_y())
            
        # body.set_position(position)