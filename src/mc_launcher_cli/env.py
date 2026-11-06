"""Environment operations"""

import ctypes
from typing import List

from mc_launcher_cli.context import PROJECT_DATA
from mc_launcher_cli.context import JAVA_PROGRAM_DIRS
from mc_launcher_cli.context import MC_RESOURCE
from mc_launcher_cli.datas import Java
from mc_launcher_cli.datas import Minecraft
from mc_launcher_cli.dicts import VersionInfo
from mc_launcher_cli.other import load_config
from mc_launcher_cli.other import load_json_file


def run_in_administrator():
    
    match ctypes.windll.shell32.IsUserAnAdmin():
        case 0:
            return False
        case 1:
            return True
        case _:
            raise Exception


def init_project_data():
    PROJECT_DATA.DIR.mkdir(parents=True, exist_ok=True)
    PROJECT_DATA.LOGS.mkdir(parents=True, exist_ok=True)


def get_javas():
    javas: List[Java] = []
    
    for java_program_dir in JAVA_PROGRAM_DIRS:
        for java_home in java_program_dir.iterdir():
            release_file = java_home / "release"
            java_file = java_home / "bin/java.exe"

            if not release_file.exists():
                continue

            if not all([
                java_file.exists(),
                java_file.is_file()
            ]):
                continue

            release = load_config(release_file)
            implementor = release.get("IMPLEMENTOR")
            java_version = release.get("JAVA_VERSION")
            os_arch = release.get("OS_ARCH")
            
            javas.append(Java(
                HOME=java_home,
                IMPLEMENTOR=implementor,
                VERSION=java_version,
                OS_ARCH=os_arch
            ))

    return javas


def get_minecrafts():
    minecrafts: List[Minecraft] = []

    for sub in MC_RESOURCE.VERSIONS.iterdir():
        if not sub.is_dir():
            continue

        program_file = sub / f"{sub.name}.jar"
        version_file = sub / f"{sub.name}.json"

        if not all([
            program_file.exists(),
            program_file.is_file(),
            version_file.exists(),
            version_file.is_file()
        ]):
            continue

        version_info: VersionInfo = load_json_file(version_file)

        if sub.name != version_info["id"]:
            continue

        minecrafts.append(Minecraft(
            ID=version_info["id"],
            HOME=sub,
            VERSION=version_info["clientVersion"]
        ))

    return minecrafts