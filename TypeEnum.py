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

    def parse_to_title(self):
        if self.TIMESTAMP:
            return "Data"
        elif self.CONFIRMED:
            return "Liczba przypadków zachorowań na COVID-19"
        elif self.DEATHS:
            return "Liczba śmierci spowodowanych przez COVID-19"
        elif self.RECOVERED:
            return "Liczba wyzdrowień z COVID-19"
        elif self.IN_THE_HOSPITAL:
            return "Liczba osób hospitalizowanych"
        elif self.IN_QUARANTINE:
            return "Liczba osób poddanych kwarantannie"
        elif self.UNDER_MEDICAL_SUPERVISION:
            return "Liczba osób pod nadzorem medycznym"
        elif self.NUMBER_OF_TESTS:
            return "Liczba przeprowadzonych testów na COVID-19"
