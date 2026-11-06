"""Environment operations"""

import ctypes


def run_in_administrator():
    
    match ctypes.windll.shell32.IsUserAnAdmin():
        case 0:
            return False
        case 1:
            return True
        case _:
            raise Exception
