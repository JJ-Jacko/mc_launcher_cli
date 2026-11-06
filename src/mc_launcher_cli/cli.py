from mc_launcher_cli.env import init_project_data
from mc_launcher_cli.log import get_logger


def main():
    init_project_data()
    logger = get_logger("mc_launcher_cli")

if __name__ == "__main__":
    main()