import pandas as pd
import numpy as np
from DataStorageManager import DataStorageManager

class AdvancedDataProcessor:

    def __init__(self, data_storage_manager):
        self.data_storage_manager = data_storage_manager

    def apply_techniques(self, config, techniques, df):
        results = {}

        if 'moving_average' in techniques:
            window = config['moving_average']['window']
            results['moving_average'] = self.calculate_moving_average(df, window)

        if 'RSI' in techniques:
            window = config['RSI']['window']
            results['RSI'] = self.calculate_RSI(df, window)

        if 'MACD' in techniques:
            short_window = config['MACD']['short_window']
            long_window = config['MACD']['long_window']
            signal_window = config['MACD']['signal_window']
            results['MACD'] = self.calculate_MACD(df, short_window, long_window, signal_window)

        return results

    def calculate_moving_average(self, df, window):
        return df['Close'].rolling(window=window).mean()

    def calculate_RSI(self, df, window):
        delta = df['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_MACD(self, df, short_window, long_window, signal_window):
        short_ema = df['Close'].ewm(span=short_window, adjust=False).mean()
        long_ema = df['Close'].ewm(span=long_window, adjust=False).mean()
        macd_line = short_ema - long_ema
        signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()

        return {'macd_line': macd_line, 'signal_line': signal_line}
