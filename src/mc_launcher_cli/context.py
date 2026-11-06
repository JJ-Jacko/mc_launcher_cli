import os
from pathlib import Path

from mc_launcher_cli.other import load_config


__all__ = [
    # Config
    "CONFIG",

    # Path
    "PROJECT_DATA",
]

# Path
CONFIG_FILE = Path("config.toml")

# Initialization
CONFIG = load_config(CONFIG_FILE)

# Path
PROJECT_DATA: Path = Path(os.environ["LOCALAPPDATA"]) / CONFIG["project"]["organization"] / CONFIG["project"]["name"]
