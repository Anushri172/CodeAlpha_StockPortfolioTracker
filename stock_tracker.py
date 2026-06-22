stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

stock_name = input("Enter stock name (AAPL/TSLA/GOOG): ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    total = stock_prices[stock_name] * quantity
    print("Total Investment Value: $", total)
else:
    print("Stock not found!")