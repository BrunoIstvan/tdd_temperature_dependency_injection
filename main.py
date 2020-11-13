import os

from app import App

if __name__ == '__main__':

    import sys
    # from matplotlib_plot import Plot
    from plotly_plot import Plot
    from open_weather_json import DataSource as DSJson
    from urban_climate_csv import DataSource as DSCsv

    origin_name = sys.argv[1]
    file_name = sys.argv[2]
    app = None

    if not os.path.exists(file_name):
        raise Exception('O arquivo de dados informado não existe')

    print('Origin:', origin_name.lower())
    print('File Name:', file_name)

    if origin_name.lower() == 'json':
        app = App(data_source=DSJson(), plot=Plot())
    if origin_name.lower() == 'csv':
        app = App(data_source=DSCsv(), plot=Plot())

    print(app)

    temperatures_by_hour = app.read(file_name=file_name)
    app.draw(temperatures_by_hour)
