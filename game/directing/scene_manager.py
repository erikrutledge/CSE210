import csv
from constants import *
from game.casting.rat import Rat
from game.casting.body import Body
from game.casting.platform import Platform
from game.casting.safe import Safe
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.flag import Flag
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_rat_action import CollideRatAction
from game.scripting.control_rat_action import ControlRatAction
from game.scripting.draw_rat_action import DrawRatAction
from game.scripting.draw_platforms_action import DrawPlatformsAction
from game.scripting.draw_safe_block_action import DrawSafeBlockAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_flag_action import DrawFlagAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_rat_action import MoveRatAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService

class SceneManager:
    # The person in charge of setting up the cast and script for each scene.

    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Initialize each action as a variable here.
    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_RAT_ACTION = CollideRatAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_RAT_ACTION = ControlRatAction(KEYBOARD_SERVICE)
    DRAW_RAT_ACTION = DrawRatAction(VIDEO_SERVICE)
    DRAW_PLATFORMS_ACTION = DrawPlatformsAction(VIDEO_SERVICE)
    DRAW_SAFE_BLOCKS_ACTION = DrawSafeBlockAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_FLAG_ACTION = DrawFlagAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_RAT_ACTION = MoveRatAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    
    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)

    # ________Scene Methods________
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_platforms(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_rat(cast)
        self._add_flag(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_next_level(self, cast, script):
        self._add_rat(cast)
        self._add_platforms(cast)
        self._add_flag(cast)
        self._add_dialog(cast, PREP_TO_START)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))

    def _prepare_try_again(self, cast, script):
        self._add_rat(cast)
        self._add_flag(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)
        self._add_dialog(cast, PREP_TO_RETRY)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_RAT_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_rat(cast)
        self._add_flag(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)


    # ________Casting Methods________
    def _add_rat(self, cast):
        cast.clear_actors(RAT_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level()
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace = True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                    if column[0] == "M":
                        x = FIELD_LEFT + c * PLATFORM_WIDTH
                        y = FIELD_TOP + r * PLATFORM_HEIGHT
                        position = Point(x, y)
                        size = Point(RAT_WIDTH, RAT_HEIGHT)
                        velocity = Point(0, 0)

                        body = Body(position, size, velocity)
                        rat = Rat(body)
                        cast.add_actor(RAT_GROUP, rat)
                    else:
                        pass

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_platforms(self, cast):
        cast.clear_actors(PLATFORM_GROUP)
        cast.clear_actors(SAFE_BLOCK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level()
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace = True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                    if  column[0] == "X":
                        x = FIELD_LEFT + c * PLATFORM_WIDTH
                        y = FIELD_TOP + r * PLATFORM_HEIGHT
                        position = Point(x, y)
                        size = Point(PLATFORM_WIDTH, PLATFORM_HEIGHT)
                        velocity = Point(0, 0)

                        body = Body(position, size, velocity)
                        platform = Platform(body)
                        cast.add_actor(PLATFORM_GROUP, platform)

                    elif column[0] == "S":
                        x = FIELD_LEFT + c * PLATFORM_WIDTH
                        y = FIELD_TOP + r * PLATFORM_HEIGHT
                        position = Point(x, y)
                        size = Point(SAFE_BLOCK_WIDTH, SAFE_BLOCK_HEIGHT)
                        velocity = Point(0, 0)

                        body = Body(position, size, velocity)
                        safe_block = Safe(body)
                        cast.add_actor(SAFE_BLOCK_GROUP, safe_block)
                    else:
                        pass
                        
    def _add_flag(self, cast):
        cast.clear_actors(FLAG_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level()
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace = True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                    if column[0] == "F":
                        x = FIELD_LEFT + c * PLATFORM_WIDTH
                        y = FIELD_TOP + r * PLATFORM_HEIGHT
                        position = Point(x, y)
                        size = Point(FLAG_WIDTH, FLAG_HEIGHT)
                        velocity = Point(0, 0)

                        body = Body(position, size, velocity)
                        flag = Flag(body)
                        cast.add_actor(FLAG_GROUP, flag)
                    else:
                        pass

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

# ________Scripting Methods________

    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_RAT_ACTION)
        script.add_action(OUTPUT, self.DRAW_PLATFORMS_ACTION)
        script.add_action(OUTPUT, self.DRAW_SAFE_BLOCKS_ACTION)
        script.add_action(OUTPUT, self.DRAW_FLAG_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_RAT_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_RAT_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)