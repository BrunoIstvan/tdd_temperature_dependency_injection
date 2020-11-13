import datetime
from pathlib import Path

from urban_climate_csv import DataSource

BASE_DIR = Path(__file__).resolve(strict=True).parent


def test_read():
    reader = DataSource()
    file_name = 'london.csv'
    for key, value in reader.read(file_name=file_name).items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value

