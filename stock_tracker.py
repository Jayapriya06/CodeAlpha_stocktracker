
import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol}.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
            print(f"Removed {quantity} shares of {symbol}.")
        else:
            print("Stock not found or insufficient quantity.")

    def view_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nYour Portfolio:")
        for symbol, quantity in self.portfolio.items():
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d")["Close"].iloc[-1]  # Get last closing price
            print(f"{symbol}: {quantity} shares @ ${price:.2f} each")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)

        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)

        elif choice == "3":
            portfolio.view_portfolio()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")
