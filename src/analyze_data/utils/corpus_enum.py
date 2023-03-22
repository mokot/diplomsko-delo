from enum import Enum, unique


# Enum for corpus selection
@unique
class Corpus(Enum):
    SOLAR = "SOLAR"
    LEKTOR = "LEKTOR"
