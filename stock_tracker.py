# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}
total_value = 0

# Number of stocks user wants to add
n = int(input("Enter number of different stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print("Stock not available in price list")

# Calculate total investment
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_value += investment
    print(stock, "->", quantity, "shares x", price, "=", investment)

print("\nTotal Investment Value =", total_value)

# Save result to file
file = open("portfolio.txt", "w")
file.write("Stock Portfolio Summary\n")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    file.write(f"{stock} : {quantity} shares = {investment}\n")

file.write(f"\nTotal Investment = {total_value}")
file.close()

print("Portfolio saved to portfolio.txt")
