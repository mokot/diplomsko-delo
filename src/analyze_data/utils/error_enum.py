from enum import Enum, unique


# Enum for solar and lektor error data
@unique
class ErrorType(Enum):
    SINGLE = "SINGLE"
    MULTIPLE = "MULTIPLE"
