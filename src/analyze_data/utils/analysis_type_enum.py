from enum import Enum, unique


# Enum for solar and lektor data analysis
@unique
class AnalysisType(Enum):
    CATEGORY = "CATEGORY"
    MSD = "MSD"
    ERROR_RATE = "ERROR_RATE"
    ERROR_TYPE = "ERROR_TYPE"
    ERROR_SUBTYPE = "ERROR_SUBTYPE"
