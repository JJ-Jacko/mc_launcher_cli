"""Environment operations"""

import ctypes

from mc_launcher_cli.context import PROJECT_DATA


def run_in_administrator():
    
    match ctypes.windll.shell32.IsUserAnAdmin():
        case 0:
            return False
        case 1:
            return True
        case _:
            raise Exception


def init_project_data():
    PROJECT_DATA.mkdir(parents=True, exist_ok=True)
    