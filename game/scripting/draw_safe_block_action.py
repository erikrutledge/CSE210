from constants import *
from game.scripting.action import Action
from game.casting.image import Image


class DrawSafeBlockAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        safe_blocks = cast.get_actors(SAFE_BLOCK_GROUP)
        
        for safe_block in safe_blocks:
            body = safe_block.get_body()
                
            image = Image(SAFE_BLOCK_IMAGE)
            position = body.get_position()
            self._video_service.draw_image(image, position)