from enum import Enum, unique


# Enum for multiple error keys and labels
@unique
class Error(Enum):
    ERROR_KEY = "JE NAPAKA"  # label = 0
    NO_ERROR_KEY = "NI NAPAKE"  # label = 1
    ERROR_LABEL = 0
    NO_ERROR_LABEL = 1
