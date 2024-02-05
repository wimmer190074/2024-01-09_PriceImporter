"""Testing the Converter."""

import pandas as pd
import pytest
from converter import StockDataProcessor

@pytest.fixture
def sample_csv_path(tmp_path):
    csv_data = "Lenzing, 170447112, 34.75, EUR, Vienna;\nAndritz, 170447131, 59.41, USD, New York;"
    csv_path = tmp_path / "data.txt"
    with open(csv_path, "w") as f:
        f.write(csv_data)
    return csv_path

def test_import_data_001(sample_csv_path):
    processor = StockDataProcessor(sample_csv_path)
    df = processor.import_data()
    assert isinstance(df, pd.DataFrame)

def test_import_data_002(sample_csv_path):
    processor = StockDataProcessor(sample_csv_path)
    df = processor.import_data()
    columns = ["Stock", "Price", "Currency", "Location", "DateTime"]
    data = [
    ["Lenzing", 34.75, "EUR", "Vienna", "1975-05-27 18:25:12"],
    ["Andritz", 59.41, "USD", "New York", "1975-05-27 18:25:31"]
    ]
    df_test = pd.DataFrame(data, columns=columns)
    df_test["DateTime"] = pd.to_datetime(df_test["DateTime"])  # Convert the "DateTime" column to datetime format
    assert df_test.equals(df)