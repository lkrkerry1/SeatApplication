from typing import *
from utils import constants

WHITELIST = 0
BLACKLIST = 1

def read_table() -> List[List[List[str]]]:
    """Reads the table given

    Returns:
        List[str]: a list of the empty table
    """
    table = []
    table_num = {}
    with open(constants.TABLE_FILE) as f:
        for line in f.read().splitlines():
            key, value = line.split('=', 1)
            if key == "ColumnOfGroup":
                table_num["ColumnOfGroup"] = [int(i) for i in value.split(",")]
                continue
            table_num[key] = int(value)
    for i in range(table_num["GroupNum"]):
        table.append([])
        for j in range(table_num["ColumnOfGroup"][i]):
            table[i].append([])
            for _ in range(table_num["LineOfGroup"]):
                table[i][j].append("")
    return table



def read_names() -> List[str]:
    """Reads the names of the specified properties

    Returns:
        List[str]: a list of the names
    """
    with open(constants.NAME_FILE) as f:
        return f.read().splitlines()

def read_rules(names: List[str]) -> Tuple[Dict[str, str]]:
    """Reads the rules of the specified properties

    Args:
        names (List[str]): The names given

    Returns:
        Dict[str, str]: a dict of the rules
    """
    rules = ({},{})
    with open(constants.RULES_FILE) as f:
        for line in f.read().splitlines():
            if "[WhiteList]" in line:
                idx = 0
                continue
            if "[BlackList]" in line:
                idx = 1
                continue
            key, value = line.split(':')
            if idx == WHITELIST and key in rules[idx]:
                raise ValueError("Invalid whitesList rule with key '%s' and value '%s'"% key %value)
            if idx == BLACKLIST and key in rules[idx] and rules[idx][key] == value:
                raise ValueError("Invalid blackList rule being multiple: key '%s' and value '%s'"% key %value)
            if key not in names:
                raise ValueError("Invalid rule with '%s' which is not in names"%key)
            if value not in names:
                raise ValueError("Invalid rule with '%s' which is not in names"%value)
            rules[idx][key] = value
    return rules

def output():
    pass