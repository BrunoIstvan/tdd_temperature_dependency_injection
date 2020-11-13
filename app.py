import datetime
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


class App:

    @classmethod
    def configure(cls, filename):

        with open(filename) as file:
            config = json.load(file)

        data_source = __import__(config['data_source']['name']).DataSource()
        plot = __import__(config['plot']['name']).Plot()

        return cls(data_source, plot)

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
