from constants import *
from game.scripting.action import Action
from game.casting.image import Image


class DrawRatAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        rat = cast.get_first_actor(RAT_GROUP)
        body = rat.get_body()

        image = Image(RAT_IMAGE)
        position = body.get_position()
        self._video_service.draw_image(image, position)