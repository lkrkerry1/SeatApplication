import random
from typing import *
from utils import constants, io

def put_musnt(seating:io.SeatingTable) -> io.SeatingTable:
    """Put all the blacklisted in the table
    """
    for i, j in seating.rules[io.BLACKLIST].items():
        if seating.status[i] == False:
            column = -1
            row = -1
            pos = random.randint(0, 1)
            while (column == -1 and row == -1) or (seating.table[column][row][0] != ""):
                column = random.randint(0, len(seating.table) - 1) # choose a random group
                row = random.randint(0, len(seating.table[column]) - 1) # choose a random row
            seating.table[column][row][0] = i
        if seating.status[j] == False:
            column = -1
            row = -1
            pos = random.randint(0, 1)
            while (column == -1 and row == -1) or (seating.table[column][row][0] != "") \
                                            or seating.table[column][row][pos^1] == i: # bumped into the blacklist
                column = random.randint(0, len(seating.table) - 1) # choose a random group
                row = random.randint(0, len(seating.table[column]) - 1) # choose a random row
            seating.table[column][row][1] = j
            seating.status[i] = seating.status[j] = True
    return seating

def put_must(seating:io.SeatingTable)-> io.SeatingTable:
    """Put all the whitelisted in the table
    """
    for i, j in seating.rules[io.WHITELIST].items():
        if seating.status[i] == True:
            if seating.status[j] == True:
                continue
            else:
                raise ValueError("Invalid whitelist trying to put '%s' with two deskmates" %i)
        elif seating.status[j] == True:
            if seating.status[i] == True:
                continue
            else:
                raise ValueError("Invalid whitelist trying to put '%s' with two deskmates" %j)
        column = -1
        row = -1
        desk = [i, j]
        seating.status[i] = seating.status[j] = True
        random.shuffle(desk) # randomize the deskmates
        while (column == -1 and row == -1) or (seating.table[column][row][0] != ""):
            column = random.randint(0, len(seating.table) - 1) # choose a random group
            row = random.randint(0, len(seating.table[column]) - 1) # choose a random row
        seating.table[column][row] = desk
    return seating

def rand_others(names:List[str], table:List[List[List[str]]], status:Dict[str, bool]) -> List[List[List[str]]]:
    """Put all the others in the given table

    Args:
        names (List[str]): the names given
        table (List[List[List[str]]]): the sitting table
        status (Dict[str, bool]): current status

    Returns:
        List[List[List[str]]]: the final sitting table
    """ # Todo: use class to rewrite
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
    seating = io.SeatingTable()
    if(constants.DEBUG):
        check()
    # Todo: rewrite generate
    print(seating)
    seating.save()