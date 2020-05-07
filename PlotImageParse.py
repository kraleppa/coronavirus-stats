import matplotlib.pyplot as plt
from DataService import get_data
from TypeEnum import Type, parse_to_title

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (20, 12),
          'axes.labelsize': 'x-large',
          'axes.titlesize': 'x-large',
          'xtick.labelsize': 'x-large',
          'ytick.labelsize': 'x-large'}

plots = [Type.CONFIRMED, Type.IN_QUARANTINE, Type.NUMBER_OF_TESTS, Type.DAILY_NUMBER_OF_TESTS]


def create_plot(data_type: Type):
    dates, data = get_data(data_type)
    plt.close()
    plt.rcParams.update(params)
    plt.bar(dates, data)
    plt.grid(True, which='both')
    plt.title(parse_to_title(data_type), fontsize=20)
    plt.xticks(rotation=90)
    plt.savefig(f"static/images/{parse_to_title(data_type)}")


def refresh_plots():
    for enum in plots:
        create_plot(enum)
