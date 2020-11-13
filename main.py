import os

from app import App

if __name__ == '__main__':
    import sys

    config_file = sys.argv[1]
    file_name = sys.argv[2]
    app = App.configure(config_file)
    temperatures_by_hour = app.read(file_name=file_name)
    app.draw(temperatures_by_hour)
