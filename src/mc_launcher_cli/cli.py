from mc_launcher_cli.env import init_project_data
from mc_launcher_cli.log import get_logger


def main():
    logger = get_logger("test", file=False)
    init_project_data()
    

if __name__ == "__main__":
    main()