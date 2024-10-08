import sys, os, time


PROJECT_DIR = os.path.join(
    os.path.dirname(sys.argv[0]), os.path.pardir
)
DEBUG: int = 1
DISPLAY_MODE = 0

# [DEP] DATA_DIR = os.path.join(PROJECT_DIR, "dat")
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
SETTINGS_DIR = os.path.join(ASSETS_DIR, "settings")
LOGGING_DIR = os.path.join(PROJECT_DIR, "log")

NAME_FILE = os.path.join(SETTINGS_DIR, "name.yaml")
RULES_FILE = os.path.join(SETTINGS_DIR, "rule.yaml")
TABLE_FILE = os.path.join(SETTINGS_DIR, "table.yaml")
LOGGING_SETTINGS = os.path.join(SETTINGS_DIR, "logging.yaml")

OUTPUT_DIR = os.path.join(ASSETS_DIR, "history")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, str(time.time()) + ".txt")

AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
RANDOMIZE_VEDIO = os.path.join(AUDIO_DIR, "randomize.avi")
BACKGROUND_PICTURE = os.path.join(AUDIO_DIR, "bg.png")
BACK_BUTTON = os.path.join(AUDIO_DIR, "back.png")
OPEN_BUTTON = os.path.join(AUDIO_DIR, "open.png")
DEL_BUTTON = os.path.join(AUDIO_DIR, "del.png")

DEFAULT_GROUP_NUM = 3
DEFAULT_ROW_OF_GROUP = [6, 6, 7]
DEFAULT_COLUMN_OF_DESK = 2

START_PROBABILITY = 100
DELTA_PROBABILITY = [20, 15, 10, 5, 0]

BUFFER_SIZE = 10
BUTTON_SIZE = (50, 50)

# raise NotImplementedError


import yaml
