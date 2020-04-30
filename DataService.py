import csv
from TypeEnum import Type


def get_data(data_type: Type):
    dates_list = []
    data_list = []
    try:
        file = open("CoronavirusPL - General.csv")
        csv_reader = csv.reader(file, delimiter=",")

        if data_type == Type.DAILY_NUMBER_OF_TESTS:
            it = 0
            prev = None
            for row in csv_reader:
                if it == 0:
                    it += 1
                elif it == 1:
                    prev = int(row[Type.NUMBER_OF_TESTS])
                    data_list.append(prev)
                    dates_list.append(row[Type.TIMESTAMP])
                    it += 1
                else:
                    cur = int(row[Type.NUMBER_OF_TESTS])
                    data_list.append(cur - prev)
                    dates_list.append(row[Type.TIMESTAMP])
                    prev = cur
        else:
            for row in csv_reader:
                if row[0] == "Timestamp":
                    continue
                dates_list.append(row[Type.TIMESTAMP])
                data_list.append(int(row[data_type]))
    except FileNotFoundError:
        exit(1)
    return dates_list, data_list
