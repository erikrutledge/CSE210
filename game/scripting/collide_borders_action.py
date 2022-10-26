from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.rat import Rat


class CollideBordersAction(Action, Rat):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        rat = cast.get_first_actor(RAT_GROUP)
        body = rat.get_body()
        position = body.get_position()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)

        if y >= (FIELD_BOTTOM + RAT_WIDTH):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life()
            self._audio_service.play_sound(bounce_sound)
            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:

                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)