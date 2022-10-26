from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point

class CollideRatAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

        
    def execute(self, cast, script, callback):

        self.safe_collisions(cast)
        self.danger_collisions(cast, callback)
        self.flag_collision(cast, callback)



    def flag_collision(self, cast, callback):
        rat = cast.get_first_actor(RAT_GROUP)
        flag = cast.get_first_actor(FLAG_GROUP)
        rat_body = rat.get_body()
        flag_body = flag.get_body()

        if self._physics_service.has_collided(rat_body, flag_body):
            sound = Sound(WELCOME_SOUND)
            self._audio_service.play_sound(sound)
            stats = cast.get_first_actor(STATS_GROUP)
            stats.next_level()
            callback.on_next(NEXT_LEVEL)

    
    def safe_collisions(self, cast):
        rat = cast.get_first_actor(RAT_GROUP)
        safe_blocks = cast.get_actors(SAFE_BLOCK_GROUP)

        for safe_block in safe_blocks:
            safe_blocks_body = safe_block.get_body()
            rat_body = rat.get_body()
            safe_blocks_surface = safe_blocks_body.get_position()
            rat_surface = rat_body.get_position()

            if self._physics_service.has_collided(rat_body, safe_blocks_body):
                if self._physics_service.is_above(rat_body, safe_blocks_body):
                    x = rat_surface.get_x()
                    y = safe_blocks_surface.get_y() - PLATFORM_HEIGHT
                    position = Point(x,y)
                    rat_body.set_position(position)

                elif self._physics_service.is_below(rat_body, safe_blocks_body):
                    x = rat_surface.get_x()
                    y = safe_blocks_surface.get_y() + PLATFORM_HEIGHT
                    position = Point(x,y)
                    rat_body.set_position(position)

    
    def danger_collisions(self, cast, callback):
        rat = cast.get_first_actor(RAT_GROUP)
        platforms = cast.get_actors(PLATFORM_GROUP)
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)

        for platform in platforms:
            platform_body = platform.get_body()
            rat_body = rat.get_body()

            if self._physics_service.has_collided(rat_body, platform_body):
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
                self._audio_service.play_sound(bounce_sound)
                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN) 
                else:

                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(over_sound)

