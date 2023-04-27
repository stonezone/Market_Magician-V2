import json
from MarketDataCollector import MarketDataCollector
from DataStorageManager import DataStorageManager
from AdvancedDataProcessor import AdvancedDataProcessor
from StrategyCreator import StrategyCreator
from TradeManager import TradeManager

def main():
    with open("config.json") as config_file:
        config = json.load(config_file)

    data_collector = MarketDataCollector(config)
    data_storage_manager = DataStorageManager(config)

    start_date = "2020-01-01"
    end_date = "2023-04-25"
    symbol = "AAPL"

    # Fetch and store the data
    stock_data = data_collector.get_data(symbol, start_date, end_date)
    data_storage_manager.store_data(symbol, stock_data)

    # Load the data from storage
    loaded_data = data_storage_manager.get_data(symbol, start_date, end_date)

    advanced_data_processor = AdvancedDataProcessor(data_storage_manager)
    strategy_creator = StrategyCreator(advanced_data_processor)
    trade_manager = TradeManager(config["starting_balance"], config["alpaca"], strategy_creator)

    # Add the line below to read 'techniques' from the config file
    strategy_config = config["techniques"]

    strategy_signals = strategy_creator.create_strategy(strategy_config, loaded_data)
    trade_manager.execute_trades(strategy_signals)

if __name__ == "__main__":
    main()
