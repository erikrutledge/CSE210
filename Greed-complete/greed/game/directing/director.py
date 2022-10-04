import random
from game.casting.artifact import Artifact
from game.shared.point import Point
from game.shared.color import Color

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.running_total = []

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        margin = Point(0,15)
        neg_margin = Point(0,-15)

        for artifact in artifacts:
            location = artifact.get_position()
            depth = location.get_y()
            if robot.get_position().equals(artifact.get_position()) or robot.get_position().equals(artifact.get_position().add(margin)) or robot.get_position().equals(artifact.get_position().add(neg_margin)):
                self.running_total.append(artifact.get_value())
                banner.set_text(f"Score: {sum(self.running_total)}")
                cast.remove_actor("artifacts", artifact)
            elif depth >= 600:
                cast.remove_actor("artifacts", artifact)
            position = artifact.get_position()
            velocity = Point(0,+5)
            new_position = position.add(velocity)
            artifact.set_position(new_position)

        if len(artifacts) < 50:
            artifact = Artifact()
            artifact.set_font_size(15)
            x = random.randint(1, 60 - 1)
            y = 1
            position = Point(x,y)
            position = position.scale(15)
            artifact.set_position(position)
            n = random.randint(1,2)
            if n == 1:
                artifact.set_text("*")
                artifact.set_color(Color(0,179,234))
                artifact.set_value(1)
            elif n == 2:
                artifact.set_text("O")
                artifact.set_color(Color(96,43,30))
                artifact.set_value(-1)
            cast.add_actor("artifacts", artifact)
 
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
