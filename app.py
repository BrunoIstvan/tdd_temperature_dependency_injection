import csv
from datetime import datetime
from pathlib import Path

import matplotlib.dates
import matplotlib.pyplot

BASE_DIR = Path(__file__).resolve(strict=True).parent


class App:

    def read(self, file_name):

        temperatures_by_hour = {}
        file_name = Path(BASE_DIR).joinpath(file_name)

        with open(file=file_name, mode='r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                hour = datetime.strptime(row[0], '%d/%m/%Y %H:%M').isoformat()
                temperature = float(row[2])
                temperatures_by_hour[hour] = temperature

        return temperatures_by_hour

    def draw(self, temperatures_by_hour):

        dates = []
        temperatures = []

        for date, temp in temperatures_by_hour.items():
            dates.append(date)
            temperatures.append(temp)

        dates = matplotlib.dates.date2num(dates)
        matplotlib.pyplot.plot_date(dates, temperatures, linestyle='-')
        matplotlib.pyplot.show()
