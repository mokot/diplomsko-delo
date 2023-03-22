from enum import Enum, unique


# Enum for solar and lektor data
@unique
class FileType(Enum):
    COMPLETE = "COMPLETE"  # complete data (source + target + link)
    SOURCE = "SOURCE"
    TARGET = "TARGET"
    LINK = "LINK"
