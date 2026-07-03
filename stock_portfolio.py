stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 320,
    "AMZN": 140
}

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

total_value = 0

while True:
    stock = input("\nEnter Stock Name (AAPL, TSLA, GOOG, MSFT, AMZN): ").upper()

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity
    total_value += investment

    print(f"Investment in {stock}: ${investment}")

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n===================================")
print(f"Total Investment Value = ${total_value}")
print("===================================")

with open("portfolio_result.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write(f"Total Investment Value = ${total_value}")

print("\nResult saved in portfolio_result.txt")
print("Thank you!")