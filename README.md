
# Custom Indicators for Jesse Trading Bots

This repository contains custom indicators to be used with the Jesse trading framework. These indicators enhance the capabilities of Jesse by providing additional metrics and tools for creating and backtesting trading strategies.

**🤖 GET JESSE TRADING [HERE](https://jesse.trade?ref=201221)** 📈

### Indicators
- **Highest:** Gets the highest value of a candle for a period
- **Lowest:** Gets the lowest value of a candle for a period
## Installation

To use these custom indicators in your Jesse environment, follow the steps below:

### Step 1: Clone the Repository

Go to the main folder of your jesse environment and clone this repository to your local machine:

```bash
git clone https://github.com/asuras-ai/jesse-custom-indicators.git custom_indicators
```
Or just copy the folder into the main directory of your Jesse environment

### Step 2: Import and Use the Indicators in Your Strategy

Once the indicators are added to your Jesse project, you can import and use them in your trading strategies. Below is an example of how to do this:

1. Open or create a strategy file in your Jesse project, for example, `~/jesse-project/strategies/my_strategy.py`.

2. Import the custom indicator:

   ```python
   import custom_indicators as cta
   ```

3. Use the indicator in your strategy:

   ```python
   class MyStrategy(Strategy):
       @property
       def my_custom_indicator(self):
           return cta.custom_indicator(self.candles)
       
       def should_long(self) -> bool:
           return self.my_custom_indicator > some_value
       
       def go_long(self):
           entry_price = self.price
           qty = utils.size_to_qty(self.balance * 0.5, entry_price)
           self.buy = qty, entry_price  # MARKET order
       
       def update_position(self) -> None:
           if self.my_custom_indicator < some_value:
               self.liquidate()
       
       def on_open_position(self, order) -> None:
           self.stop_loss = self.position.qty, self.price - self.current_range * 2
           self.take_profit = self.position.qty / 2, self.price + self.current_range * 2
       
       @property
       def current_range(self):
           return self.high - self.low
   ```

### Example Custom Indicator

Here's an example of what a custom indicator might look like. Place this file in your `indicators` directory:

```python
# ~/jesse-project/indicators/my_custom_indicator.py

def my_custom_indicator(candles, period=14):
    # Example calculation
    return ta.sma(candles, period)
```

### Documentation

For more detailed information on how to create and use custom indicators in Jesse, refer to the official Jesse documentation: [Jesse Docs](https://docs.jesse-ai.com/).

## Contributing

If you would like to contribute to this repository, please fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Happy trading with Jesse!
