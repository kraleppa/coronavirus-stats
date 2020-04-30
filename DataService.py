import csv
from TypeEnum import Type


class DataService:
    def __init__(self):
        try:
            file = open("CoronavirusPL - General.csv")
            self.csv_reader = csv.reader(file, delimiter=",")
        except FileNotFoundError:
            exit(1)

    def get_data(self, data_type):
        csv_iterator = iter(self.csv_reader)
        next(csv_iterator)
        result_lit = []
        for row in csv_iterator:
            result_lit.append((row[Type.TIMESTAMP], row[data_type]))
        return result_lit


if __name__ == "__main__":
    service = DataService()
    print(service.get_data(Type.CONFIRMED))
