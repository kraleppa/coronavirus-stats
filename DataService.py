import csv
from TypeEnum import Type


def get_data(data_type):
    dates_list = []
    data_list = []
    try:
        file = open("CoronavirusPL - General.csv")
        csv_reader = csv.reader(file, delimiter=",")

        for row in csv_reader:
            if row[0] == "Timestamp":
                continue
            dates_list.append(row[Type.TIMESTAMP])
            data_list.append(int(row[data_type]))
    except FileNotFoundError:
        exit(1)
    return dates_list, data_list
