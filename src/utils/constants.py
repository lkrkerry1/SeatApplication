import sys, os, time

PROJECT_DIR = os.path.join(os.path.dirname(sys.argv[0]), os.path.pardir)
DEBUG: int = 0

# [DEP] DATA_DIR = os.path.join(PROJECT_DIR, "dat")
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
SETTINGS_DIR = os.path.join(ASSETS_DIR, "settings")

NAME_FILE = os.path.join(SETTINGS_DIR, "name.txt")
RULES_FILE = os.path.join(SETTINGS_DIR, "rules.txt")
TABLE_FILE = os.path.join(SETTINGS_DIR, "table.txt")
OUTPUT_DIR = os.path.join(ASSETS_DIR, "history")
OUTPUT_DIR = os.path.join(OUTPUT_DIR, str(time.time()) + ".txt")

START_PROBABILITY = 100
DELTA_PROBABILITY = [20, 15, 10, 5, 0]
