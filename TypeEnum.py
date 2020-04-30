from enum import IntEnum


def parse_to_title(data_type):
    if data_type == Type.TIMESTAMP:
        return "Data"
    elif data_type == Type.CONFIRMED:
        return "Liczba przypadków zachorowań na COVID-19"
    elif data_type == Type.DEATHS:
        return "Liczba śmierci spowodowanych przez COVID-19"
    elif data_type == Type.RECOVERED:
        return "Liczba wyzdrowień z COVID-19"
    elif data_type == Type.IN_THE_HOSPITAL:
        return "Liczba osób hospitalizowanych"
    elif data_type == Type.IN_QUARANTINE:
        return "Liczba osób poddanych kwarantannie"
    elif data_type == Type.UNDER_MEDICAL_SUPERVISION:
        return "Liczba osób pod nadzorem medycznym"
    elif data_type == Type.NUMBER_OF_TESTS:
        return "Liczba przeprowadzonych testów na COVID-19"
    elif data_type == Type.DAILY_NUMBER_OF_TESTS:
        return "Dzienna liczba przeprowadzonych testów na COVID-19"


class Type(IntEnum):
    TIMESTAMP = 0,
    CONFIRMED = 1,
    DEATHS = 2,
    RECOVERED = 3,
    IN_THE_HOSPITAL = 4,
    IN_QUARANTINE = 5,
    UNDER_MEDICAL_SUPERVISION = 6,
    NUMBER_OF_TESTS = 7,
    DAILY_NUMBER_OF_TESTS = 8


