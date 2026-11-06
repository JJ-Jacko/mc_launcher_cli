from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Java:
    HOME: Path
    IMPLEMENTOR: str
    VERSION: str
    OS_ARCH: str
