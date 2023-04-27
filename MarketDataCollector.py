# MarketDataCollector.py
# This script contains the MarketDataCollector class responsible for fetching market data from various
# data sources (e.g., Alpha Vantage, Yahoo Finance). It interacts with the DataStorageManager class to
# provide the collected data for storage. It is used in main.py to fetch market data for the specified symbols.

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import yfinance as yf

class MarketDataCollector:

    def __init__(self, config):
        self.config = config

    def get_data(self, symbol, start_date, end_date, source="yahoo"):
        if source == "alpha_vantage":
            return self._get_data_alpha_vantage(symbol)
        elif source == "yahoo":
            return self._get_data_yahoo(symbol, start_date, end_date)
        else:
            raise ValueError(f"Unsupported data source: {source}")

    def _get_data_alpha_vantage(self, symbol):
        api_key = self.config["data_sources"]["alpha_vantage"]["api_key"]
        ts = TimeSeries(key=api_key, output_format="pandas")
        data, _ = ts.get_daily(symbol, outputsize="full")
        return data

    def _get_data_yahoo(self, symbol, start_date, end_date):
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
