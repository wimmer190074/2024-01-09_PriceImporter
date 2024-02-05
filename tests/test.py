import pandas as pd
from converter import StockDataProcessor

csv_data = "Lenzing, 170447112, 34.75, EUR, Vienna;\nAndritz, 170447131, 59.41, USD, New York;"
csv_path = "data.txt"
with open(csv_path, "w") as f:
        f.write(csv_data)

processor = StockDataProcessor(csv_path)
df = processor.import_data()

columns = ["Stock", "Price", "Currency", "Location", "DateTime"]
data = [
["Lenzing", 34.75, "EUR", "Vienna", "1975-05-27 18:25:12"],
["Andritz", 59.41, "USD", "New York", "1975-05-27 18:25:31"]
]
df_test = pd.DataFrame(data, columns=columns)
df_test["DateTime"] = pd.to_datetime(df_test["DateTime"]) 

comparison = df_test.compare(df)
print(comparison)

