## SUPERCEDED BY COLLIDE_RAT_ACTION

from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point


class CollidePlatformsAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        rat = cast.get_first_actor(RAT_GROUP)
        platforms = cast.get_actors(PLATFORM_GROUP)

        for platform in platforms:
            platform_body = platform.get_body()
            rat_body = rat.get_body()
            surface = platform_body.get_position()
            hand = rat_body.get_position()

            if self._physics_service.has_collided(rat_body, platform_body):

                if self._physics_service.is_above(rat_body, platform_body):
                    y = surface.get_y() - PLATFORM_HEIGHT
                    x = hand.get_x()
                    position = Point(x,y)
                    rat_body.set_position(position)

                if self._physics_service.is_below(rat_body, platform_body):
                    y = surface.get_y() + PLATFORM_HEIGHT
                    x = hand.get_x()
                    position = Point(x,y)
                    rat_body.set_position(position)

