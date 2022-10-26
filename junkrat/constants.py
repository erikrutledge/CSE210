from game.casting.color import Color

# _______General Game Constants________

# GAME
GAME_NAME = "JunkRat"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 672
SCREEN_HEIGHT = 896
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 0
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "junkrat/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "junkrat/assets/sounds/boing.wav"
WELCOME_SOUND = "junkrat/assets/sounds/start.wav"
OVER_SOUND = "junkrat/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "a"
RIGHT = "d"
UP = "w"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "junkrat/assets/data/level-{:03}.txt"
BASE_LEVELS = 5


# _______Scripting Constants________

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6


# _______Casting Constants________

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 5
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"

# RAT
RAT_GROUP = "rat"
RAT_IMAGE = "junkrat/assets/images/000.png"
RAT_WIDTH = 28
RAT_HEIGHT = 28
RAT_VELOCITY = 3
RAT_GRAVITY = 3.5
RAT_JUMP = -5

# PLATFORM
PLATFORM_GROUP = "platforms"
PLATFORM_IMAGE = "junkrat/assets/images/001.png"
PLATFORM_WIDTH = 28
PLATFORM_HEIGHT = 28

# FLAG
FLAG_GROUP = "flag"
FLAG_IMAGE = "junkrat/assets/images/002.png"
FLAG_WIDTH = 28
FLAG_HEIGHT = 28

# SAFE BLOCK
SAFE_BLOCK_GROUP = "safeblocks"
SAFE_BLOCK_IMAGE = "junkrat/assets/images/003.png"
SAFE_BLOCK_WIDTH = 28
SAFE_BLOCK_HEIGHT = 28

# DIALOG
DIALOG_GROUP = "dialogs"
WELCOME_IMAGE = "junkrat/assets/images/003.png"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_START = "READY SET GO!"
PREP_TO_RETRY = "TRY AGAIN"
WAS_GOOD_GAME = "GAME OVER"
