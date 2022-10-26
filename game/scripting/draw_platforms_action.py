from constants import *
from game.scripting.action import Action
from game.casting.image import Image


class DrawPlatformsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        platforms = cast.get_actors(PLATFORM_GROUP)
        
        for platform in platforms:
            body = platform.get_body()
                
            image = Image(PLATFORM_IMAGE)
            position = body.get_position()
            self._video_service.draw_image(image, position)