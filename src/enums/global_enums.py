from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not to expected"
    WRONG_ELEMENT_COUNT = "Numbers of item is not equal to expected"
