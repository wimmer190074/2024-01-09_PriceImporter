"""Imports the Stock Prices and Visualizes them."""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.dates as mdates

class StockDataProcessor:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def import_data(self):
        try:
            df = pd.read_csv(self.csv_path, header=None, names=['Stock', 'Timestamp', 'Price', 'Currency', 'Location'])

            df = df.applymap(lambda x: x.strip().replace(';', '') if isinstance(x, str) else x)

            df['DateTime'] = pd.to_datetime(df['Timestamp'], unit='s')
            df.drop('Timestamp', axis=1, inplace=True)

            return df
        except FileNotFoundError:
            print(f"Error: File not found at path {self.csv_path}")
            return None

    def visualize_data(self, df):
        grouped = df.groupby(['Location', 'Stock'])

        fig, axes = plt.subplots(nrows=len(df['Location'].unique()), figsize=(10, 8 * len(df['Location'].unique())), 
                                sharex=True, sharey=True, gridspec_kw={'hspace': 0.4})

        cmap = ListedColormap(['b', 'g', 'r', 'c', 'm', 'y', 'k'])

        for i, ((location, stock), group) in enumerate(grouped):
            color = cmap(i % cmap.N)
            ax = axes[df['Location'].unique().tolist().index(location)]
            group.plot(x='DateTime', y='Price', kind='scatter', ax=ax, label=stock, color=color)

            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

            currency_label = f'Price in {group["Currency"].iloc[0]}'
            ax.set_ylabel(currency_label)

        for i, ax in enumerate(axes):
            ax.set_title(df['Location'].unique()[i])
            ax.set_xlabel('Date')
            ax.legend(title='Stock')

        plt.tight_layout()
        plt.show()