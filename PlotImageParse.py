import matplotlib.pyplot as plt
from DataService import DataService
from TypeEnum import Type

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (20, 12),
          'axes.labelsize': 'x-large',
          'axes.titlesize': 'x-large',
          'xtick.labelsize': 'x-large',
          'ytick.labelsize': 'x-large'}


class PlotParser:
    def __init__(self):
        self.data_service = DataService()

    def create_plot(self, data_type: Type):
        dates, data = self.data_service.get_data(data_type)
        plt.rcParams.update(params)
        plt.bar(dates, data)
        plt.grid(True, which='both')
        plt.title(data_type.parse_to_title(), fontsize=20)
        plt.xticks(rotation=90)
        plt.savefig(f"img/{data_type.parse_to_title()}")

