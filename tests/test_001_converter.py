# tests/test_converter.py
import pandas as pd
import pytest
from converter import StockDataProcessor

@pytest.fixture
def sample_csv_path(tmp_path):
    csv_data = "Stock, Timestamp, Price, Currency, Location\nLenzing, 170447112, 34.75, EUR, Vienna"
    csv_path = tmp_path / "data.txt"
    with open(csv_path, "w") as f:
        f.write(csv_data)
    return csv_path

def test_import_data(sample_csv_path):
    processor = StockDataProcessor(sample_csv_path)
    df = processor.import_data()
    assert isinstance(df, pd.DataFrame)

def test_visualize_data(sample_csv_path):
    processor = StockDataProcessor(sample_csv_path)
    df = processor.import_data()
    plot = processor.visualize_data(df)
    assert plot is not None  
