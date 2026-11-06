from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Java:
    HOME: Path
    IMPLEMENTOR: str
    VERSION: str
    OS_ARCH: str


@dataclass(frozen=True)
class Minecraft:
    ID: str
    HOME: Path
    VERSION: str
