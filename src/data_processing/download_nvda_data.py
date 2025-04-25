import yfinance as yf

# Download Nvidia (NVDA) data from Jan 1, 2024 to today
nvda = yf.download('NVDA', start='2024-04-25', end='2025-04-25')

# Show the first few rows
print(nvda.head())

# Save it as a CSV to your data folder
nvda.to_csv('/Users/adam/Desktop/financial_data_visualization/data/nvda_stock_data.csv')

print("✅ NVDA data saved to data/example_stock_data.csv")
