# COMPLETE: The purpose of this file is to have a single document that references and runs all the files.
from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager

def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()
    pass

if __name__ == "__main__":
    main()