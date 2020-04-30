from enum import IntEnum


class Type(IntEnum):
    TIMESTAMP = 0,
    CONFIRMED = 1,
    DEATHS = 2,
    RECOVERED = 3,
    IN_THE_HOSPITAL = 4,
    IN_QUARANTINE = 5,
    UNDER_MEDICAL_SUPERVISION = 6,
    NUMBER_OF_TESTS = 7
