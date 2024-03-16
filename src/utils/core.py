import random
from typing import *
from utils import constants, io

def put_musnt(blacklist:Dict[str,str], table:List[List[List[str]]], status:Dict[str, bool]) \
                                            -> Tuple[List[List[List[str]]],Dict[str, bool]]:
    """Put all the blacklisted in the table

    Args:
        blacklist (Dict[str,str]): the rules given
        table (List[List[List[str]]]): the sitting tables
        status (Dict[str, bool]): Whether the student has been put

    Returns:
        List[List[List[str]]]: the result
        Dict[str, bool]: Whether the student has been put
    """
    for i, j in blacklist.items():
        if status[i] == False:
            column = -1
            row = -1
            pos = random.randint(0, 1)
            while (column == -1 and row == -1) or (table[column][row][0] != ""):
                column = random.randint(0, len(table) - 1) # choose a random group
                row = random.randint(0, len(table[column]) - 1) # choose a random row
            table[column][row][0] = i
        if status[j] == False:
            column = -1
            row = -1
            pos = random.randint(0, 1)
            while (column == -1 and row == -1) or (table[column][row][0] != "") \
                                            or table[column][row][pos^1] == i: # bumped into the blacklist
                column = random.randint(0, len(table) - 1) # choose a random group
                row = random.randint(0, len(table[column]) - 1) # choose a random row
            table[column][row][1] = j
            status[i] = status[j] = True
    return table, status

def put_must(whitelist:Dict[str,str], table:List[List[List[str]]], status:Dict[str, bool]) \
                                            -> Tuple[List[List[List[str]]],Dict[str, bool]]:
    """Put all the whitelisted in the table

    Args:
        whitelist (Dict[str,str]): The rules given
        table (List[List[str]]): The sitting tables
        status (Dict[str, bool]): Whether the student has been put

    Returns:
        List[List[List[str]]]: The result
        Dict[str, bool]: Whether the student has been put
    """
    for i, j in whitelist.items():
        if status[i] == True:
            if status[j] == True:
                continue
            else:
                raise ValueError("Invalid whitelist trying to put '%s' with two deskmates" %i)
        elif status[j] == True:
            if status[i] == True:
                continue
            else:
                raise ValueError("Invalid whitelist trying to put '%s' with two deskmates" %j)
        column = -1
        row = -1
        desk = [i, j]
        status[i] = status[j] = True
        random.shuffle(desk) # randomize the deskmates
        while (column == -1 and row == -1) or (table[column][row][0] != ""):
            column = random.randint(0, len(table) - 1) # choose a random group
            row = random.randint(0, len(table[column]) - 1) # choose a random row
        table[column][row] = desk
    return table, status

def rand_others(names:List[str], table:List[List[List[str]]], status:Dict[str, bool]) -> List[List[List[str]]]:
    """Put all the others in the given table

    Args:
        names (List[str]): the names given
        table (List[List[List[str]]]): the sitting table
        status (Dict[str, bool]): current status

    Returns:
        List[List[List[str]]]: the final sitting table
    """
    random.shuffle(names)
    start_column = 0
    current_name = 0
    for column in range(start_column, len(table)):
        for row in range(len(table[column])):
            for pos in (0, 1):
                while current_name < len(names) and status[names[current_name]] == True:
                    current_name += 1
                if current_name >= len(names):
                    return table
                if table[column][row][pos] == '':
                    table[column][row][pos] = names[current_name]
                    status[names[current_name]] = True
                    current_name += 1
    return table

def check():
    pass

def rdesk():
    table = io.read_table()
    if constants.DEBUG:
        print("Table", table)
    names = io.read_names()
    if constants.DEBUG:
        print("Names",names)
    rules = io.read_rules(names)
    if constants.DEBUG:
        print("Rules", rules)
    status = {}
    for name in names:
        status[name] = False
    table, status = put_must(rules[io.WHITELIST], table, status)
    if constants.DEBUG:
        print("Have put must", table)
    table, status = put_musnt(rules[io.BLACKLIST], table, status)
    if constants.DEBUG:
        print("Have put mustn't", table)
    table = rand_others(names, table, status)
    if constants.DEBUG:
        print("Have put others", table)
    if(constants.DEBUG):
        check()
    print("The table: ")
    io.output(table)