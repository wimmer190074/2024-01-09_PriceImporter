"""Sample Use of the Converter Class"""
from converter import StockDataProcessor

x = StockDataProcessor("./data.txt")
y = x.import_data()
x.visualize_data(y)