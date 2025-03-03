# Stock Portfolio Tracker 📈  

## Overview  
The **Stock Portfolio Tracker** is a simple Python-based application that allows users to manage their stock investments. Users can **add, remove, and view stocks** along with their real-time prices using the **yfinance** API.  

## Features  
✅ Add stocks with quantity to your portfolio  
✅ Remove stocks from your portfolio  
✅ View current stock prices (requires `yfinance`)  
✅ Simple text-based interface  

## Requirements  
- Python 3.x  
- **yfinance** library (for real-time stock data)  

## Installation  
Before running the script, install the required library:  
```sh
pip install yfinance

How to Run

1. Open a terminal or command prompt.


2. Navigate to the folder containing stock_tracker.py.


3. Run the script using:

python stock_tracker.py



Usage

1️⃣ Add Stock – Enter the stock symbol (e.g., AAPL, TSLA) and quantity.
2️⃣ Remove Stock – Remove a specific number of shares from the portfolio.
3️⃣ View Portfolio – Display all stocks with their real-time prices.
4️⃣ Exit – Close the application.

Example Usage

1. Add Stock  
2. Remove Stock  
3. View Portfolio  
4. Exit  
Choose an option: 1  
Enter stock symbol: AAPL  
Enter quantity: 5  
Added 5 shares of AAPL.  

Choose an option: 3  
Your Portfolio:  
AAPL: 5 shares @ $178.25 each

Notes

If yfinance is not installed, remove the stock price fetching part.

Stock prices are based on the latest market close.


Author

Developed by Jayapriya

License

This project is open-source and available under the MIT License.
