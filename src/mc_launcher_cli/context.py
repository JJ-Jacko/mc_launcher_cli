import os
from pathlib import Path

from mc_launcher_cli.other import load_config


__all__ = [
    # Config
    "CONFIG",

    "PROJECT_DATA",
]

# Path
CONFIG_FILE = Path("config.toml")
JAVA_PROGRAM_DIRS = frozenset({
    Path("C:\Program Files\Java"),
})

class MC_RESOURCE:
    DIR = Path(os.environ["APPDATA"]) / ".minecraft"

    VERSIONS = DIR / "versions"


# Initialization
CONFIG = load_config(CONFIG_FILE)

class PROJECT_DATA:
    DIR: Path = Path(os.environ["LOCALAPPDATA"]) / CONFIG["project"]["organization"] / CONFIG["project"]["name"]

    LOGS = DIR / "logs"
