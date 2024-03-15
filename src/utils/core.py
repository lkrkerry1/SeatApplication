import random
import .utils.constants,.utils.io

def put_musnt():
    pass

def put_must():
    pass

def rand_others():
    pass

def check():
    pass

def rdesk():
    io.read_names()
    io.read_rules()
    put_must()
    put_musnt()
    rand_others()
    if(constants.DEBUG):
        check()
    io.output()