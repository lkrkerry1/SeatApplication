import random
from typing import *
from utils import constants, io

def put_musnt():
    pass

def put_must(whitelist:Dict[str,str], table:List[List[str]]) -> List[List[str]]:
    """Put all the whitelisted in the table

    Args:
        whitelist (Dict[str,str]): The rules given
        table (List[List[str]]): The sitting tables

    Returns:
        List[List[str]]: The result
    """

def rand_others():
    pass

def check():
    pass

def rdesk():
    table = io.read_table()
    if constants.DEBUG:
        print("Table", table)
    names = io.read_names()
    if constants.DEBUG:
        print("Names",names)
    rules = io.read_rules()
    if constants.DEBUG:
        print("Rules", rules)
    put_must(rules[io.WHITELIST], table)
    put_musnt()
    rand_others()
    if(constants.DEBUG):
        check()
    io.output()