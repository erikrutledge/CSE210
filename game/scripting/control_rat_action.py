from constants import *
from game.scripting.action import Action
from game.scripting.collide_rat_action import CollideRatAction


class ControlRatAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        rat = cast.get_first_actor(RAT_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            rat.move_left()
            rat.gravity()
        elif self._keyboard_service.is_key_down(RIGHT): 
            rat.move_right()
            rat.gravity()
        else:
            rat.stop_moving()
            rat.gravity()

        if self._keyboard_service.is_key_down(UP):
            rat.jump()

