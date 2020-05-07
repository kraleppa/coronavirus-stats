
import csv
from TypeEnum import Type
import requests
from bs4 import BeautifulSoup

URL = 'https://raw.githubusercontent.com/dtandev/coronavirus/master/data/CoronavirusPL%20-%20General.csv'


def refresh_data():
    source = requests.get(URL)
    if source.ok:
        soup = BeautifulSoup(source.text, 'html.parser')
        f = open("data.csv", "w")
        f.write(soup.prettify())
        f.close()


def get_data(data_type: Type):
    dates_list = []
    data_list = []
    try:
        file = open("data.csv")
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
