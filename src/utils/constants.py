import sys, os

PROJECT_DIR = os.path.join(os.path.dirname(sys.argv[0]),os.path.pardir)
DEBUG:int = 0

DATA_DIR = os.path.join(PROJECT_DIR,"dat")
NAME_FILE = os.path.join(DATA_DIR, "name.txt")
RULES_FILE = os.path.join(DATA_DIR, "rules.txt")
TABLE_FILE = os.path.join(DATA_DIR, "table.txt")
OUTPUT_DIR = os.path.join(DATA_DIR, "output.txt")
