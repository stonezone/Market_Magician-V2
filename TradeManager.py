class TradeManager:
    def __init__(self, starting_balance, alpaca_config, strategy_creator):
        self.alpaca_config = alpaca_config
        self.strategy_creator = strategy_creator
        self.equity = starting_balance
        self.open_positions = []
        self.closed_positions = []


    def execute_trades(self, strategy_signals):
        for signal in strategy_signals:
            if signal["action"] == "buy":
                self.buy(signal["symbol"], signal["quantity"], signal["price"])
                print(f"Buying {signal['quantity']} shares of {signal['symbol']} at {signal['price']}")
            elif signal["action"] == "sell":
                self.sell(signal["symbol"], signal["quantity"], signal["price"])
                print(f"Selling {signal['quantity']} shares of {signal['symbol']} at {signal['price']}")

        # Add a print statement to show the updated portfolio
        print("Updated portfolio:", self.open_positions)
        self.calculate_performance_metrics()

    def buy(self, symbol, quantity, price):
        # Implement your buy logic here
        pass

    def sell(self, symbol, quantity, price):
        # Implement your sell logic here
        pass

    def calculate_performance_metrics(self):
        total_profit_loss = sum([position["profit_loss"] for position in self.closed_positions])
        winning_trades = len([position for position in self.closed_positions if position["profit_loss"] > 0])
        losing_trades = len([position for position in self.closed_positions if position["profit_loss"] < 0])
        win_rate = winning_trades / (winning_trades + losing_trades) if (winning_trades + losing_trades) > 0 else 0
        max_drawdown = self.calculate_drawdown()

        print("Total Profit/Loss:", total_profit_loss)
        print("Winning Trades:", winning_trades)
        print("Losing Trades:", losing_trades)
        print("Win Rate:", win_rate)
        print("Max Drawdown:", max_drawdown)

    def calculate_drawdown(self):
        # Calculate the drawdown based on closed_positions
        pass
