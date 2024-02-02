import pandas as pd
import matplotlib.pyplot as plt

class StockDataProcessor:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def import_data(self):
        try:
            df = pd.read_csv(self.csv_path)
            return df
        except FileNotFoundError:
            print(f"Error: File not found at path {self.csv_path}")
            return None

    def visualize_data(self, df):
        pass
