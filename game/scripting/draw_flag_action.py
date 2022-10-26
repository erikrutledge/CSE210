from constants import *
from game.scripting.action import Action
from game.casting.image import Image


class DrawFlagAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        flag = cast.get_first_actor(FLAG_GROUP)
        body = flag.get_body()
            
        image = Image(FLAG_IMAGE)
        position = body.get_position()
        self._video_service.draw_image(image, position)