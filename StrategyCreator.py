from AdvancedDataProcessor import AdvancedDataProcessor

class StrategyCreator:
    def __init__(self, advanced_data_processor):
        self.advanced_data_processor = advanced_data_processor

    # Add the 'df' parameter to the create_strategy method
    def create_strategy(self, config, df):
        techniques = config
        analysis_results = self.advanced_data_processor.apply_techniques(config, techniques, df)
        
        strategy_signals = []

        for technique, analysis_result in analysis_results.items():
            strategy_signals.extend(self.generate_signal(technique, analysis_result))

        return strategy_signals

    # The rest of the class remains the same...


    def apply_techniques(self, config, techniques, df):
        results = {}

        if 'moving_average' in techniques:
            window = config['moving_average']['window']
            results['moving_average'] = self.calculate_moving_average(df, window)
        
        # Add other techniques here as needed

        return results

    # Other methods as before ...


    def generate_signal(self, technique, analysis_result):
        if technique == 'moving_average':
            return self.generate_moving_average_signal(analysis_result)
        elif technique == 'RSI':
            return self.generate_rsi_signal(analysis_result)
        elif technique == 'MACD':
            return self.generate_macd_signal(analysis_result)
        else:
            raise ValueError(f"Unknown technique: {technique}")

    def generate_moving_average_signal(self, moving_average):
        signals = []
        position = 0

        for i in range(1, len(moving_average)):
            if moving_average[i] > moving_average[i - 1] and position == 0:
                signals.append({"action": "buy", "symbol": "AAPL", "quantity": 10, "price": moving_average.index[i]})
                position = 1
            elif moving_average[i] < moving_average[i - 1] and position == 1:
                signals.append({"action": "sell", "symbol": "AAPL", "quantity": 10, "price": moving_average.index[i]})
                position = 0

        return signals

    def generate_rsi_signal(self, rsi):
     # Modify this function similar to generate_moving_average_signal
        return []

    def generate_macd_signal(self, macd):
    # Modify this function similar to generate_moving_average_signal
        return []
