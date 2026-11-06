from typing import TypedDict


class VersionInfo(TypedDict):
    id: str
    type: str
    clientVersion: str
    mainClass: str