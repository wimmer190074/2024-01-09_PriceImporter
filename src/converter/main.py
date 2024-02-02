from converter import StockDataProcessor

x = StockDataProcessor("./data.txt")
y = x.import_data()
print(y)