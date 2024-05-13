import sys, os

PROJECT_DIR = os.path.join(os.path.dirname(sys.argv[0]), os.path.pardir)
DEBUG: int = 1

DATA_DIR = os.path.join(PROJECT_DIR, "dat")
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
SETTINGS_DIR = os.path.join(ASSETS_DIR, "settings")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")

NAME_FILE = os.path.join(SETTINGS_DIR, "name.txt")
RULES_FILE = os.path.join(SETTINGS_DIR, "rules.txt")
TABLE_FILE = os.path.join(SETTINGS_DIR, "table.txt")
OUTPUT_DIR = os.path.join(ASSETS_DIR, "history")
MAIN_FILE = os.path.join(AUDIO_DIR, "bg.png")
RANDOM_VEDIO = os.path.join(AUDIO_DIR, "randomize.avi")
