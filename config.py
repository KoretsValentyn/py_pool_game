"""configuration"""


import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read('pool.ini')


def get_ticks():
    """return tickets"""
    return int(CONFIG['App']['Ticks'])
