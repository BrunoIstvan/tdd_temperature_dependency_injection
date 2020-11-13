import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


class App:

    def __init__(self, data_source, plot):
        self.data_source = data_source
        self.plot = plot

    def read(self, **kwargs):
        return self.data_source.read(**kwargs)

    def draw(self, temperatures_by_hour):
        dates = []
        temperatures = []

        for date, temp in temperatures_by_hour.items():
            dates.append(datetime.datetime.fromisoformat(date))
            temperatures.append(temp)

        self.plot.draw(dates, temperatures)
