import matplotlib.pyplot as plt
from DataService import get_data
from TypeEnum import Type, parse_to_title

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (20, 12),
          'axes.labelsize': 'x-large',
          'axes.titlesize': 'x-large',
          'xtick.labelsize': 'x-large',
          'ytick.labelsize': 'x-large'}


def create_plot(data_type: Type):
    print(data_type)
    dates, data = get_data(data_type)
    print(data)
    plt.close()
    plt.rcParams.update(params)
    plt.bar(dates, data)
    plt.grid(True, which='both')
    plt.title(parse_to_title(data_type), fontsize=20)
    plt.xticks(rotation=90)
    print(parse_to_title(data_type))
    plt.savefig(f"static/images/{parse_to_title(data_type)}")
