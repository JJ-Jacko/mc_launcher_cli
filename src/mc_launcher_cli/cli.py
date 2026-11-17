"""The Minecraft launcher based on CLI"""

import argparse

from mc_launcher_cli.env import init_project_data
from mc_launcher_cli.env import get_javas
from mc_launcher_cli.env import get_minecrafts
from mc_launcher_cli.log import get_logger


def main():
    init_project_data()
    logger = get_logger("mc_launcher_cli")
    parser = argparse.ArgumentParser(prog="mcl", description=__doc__)
    subparser = parser.add_subparsers(dest="command")
    parser_java = subparser.add_parser("java", help="Manage Java runtime")
    parser_java.add_argument("-l", "--list", action="store_true", help="List Java runtime")
    parser_instance = subparser.add_parser("instance", help="Manage Minecraft instances")
    parser_instance.add_argument("-l", "--list", action="store_true", help="List Minecraft instances")

    args = parser.parse_args()

    if not (command_name := args.command):
        parser.print_help()
        return

    if command_name == "java":
        if not args.list:
            parser_java.print_help()
            return
        
        print(get_javas())
        
    elif command_name == "instance":
        if not args.list:
            parser_instance.print_help()
            return
        
        print(get_minecrafts())
    

if __name__ == "__main__":
    main()