"""The Minecraft launcher based on CLI"""

import argparse
from importlib import metadata

from mc_launcher_cli.env import init_project_data
from mc_launcher_cli.env import get_javas
from mc_launcher_cli.env import get_minecrafts
from mc_launcher_cli.log import get_logger


def list_java(args: argparse.Namespace):
    print(get_javas())


def list_instance(args: argparse.Namespace):
    print(get_minecrafts())


def launch_instance(args: argparse.Namespace):
    print(f"Launch is not implemented: {args.instance_id}")


def remove_instance(args: argparse.Namespace):
    print(f"Remove is not implemented: {args.instance_id}")


def install_instance(args: argparse.Namespace):
    print(f"Install is not implemented: {args.version}")


def create_parser():
    # Root
    parser = argparse.ArgumentParser(prog="mcl", description=__doc__)
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {metadata.version('mc_launcher_cli')}",
    )
    parser.set_defaults(parser_help=parser)
    parser_commands = parser.add_subparsers(dest="command")

    # Java
    parser_java = parser_commands.add_parser("java", help="Manage Java runtime")
    parser_java.set_defaults(parser_help=parser_java)
    parser_java_actions = parser_java.add_subparsers(dest="action")

    parser_java_list = parser_java_actions.add_parser("list", help="List Java runtime")
    parser_java_list.set_defaults(handler=list_java)

    # Instance
    parser_instance = parser_commands.add_parser("instance", help="Manage Minecraft instances")
    parser_instance.set_defaults(parser_help=parser_instance)
    parser_instance_actions = parser_instance.add_subparsers(dest="action")

    parser_instance_list = parser_instance_actions.add_parser("list", help="List Minecraft instances")
    parser_instance_list.set_defaults(handler=list_instance)

    parser_instance_launch = parser_instance_actions.add_parser("launch", help="Launch a Minecraft instance")
    parser_instance_launch.add_argument("instance_id", help="Minecraft instance ID")
    parser_instance_launch.set_defaults(handler=launch_instance)

    parser_instance_remove = parser_instance_actions.add_parser("remove", help="Remove a Minecraft instance")
    parser_instance_remove.add_argument("instance_id", help="Minecraft instance ID")
    parser_instance_remove.set_defaults(handler=remove_instance)

    parser_instance_install = parser_instance_actions.add_parser("install", help="Install a Minecraft version")
    parser_instance_install.add_argument("version", help="Minecraft version")
    parser_instance_install.set_defaults(handler=install_instance)

    return parser


def main():
    init_project_data()
    logger = get_logger("mc_launcher_cli")
    parser = create_parser()
    args = parser.parse_args()

    if not hasattr(args, "handler"):
        args.parser_help.print_help()
        return

    args.handler(args)
    

if __name__ == "__main__":
    main()