from app import App

if __name__ == '__main__':

    import sys
    file_name = sys.argv[1]
    app = App()
    temperatures_by_hour = app.read(file_name=file_name)
    app.draw(temperatures_by_hour=temperatures_by_hour)
