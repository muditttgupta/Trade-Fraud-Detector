import pandas as pd
import numpy as np
import random
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Parameters
num_rows = 1000
products = ['Wheat', 'Rice', 'Sugar', 'Oil', 'Copper', 'Tea']
buyers = ['ABC Ltd', 'Global Corp', 'FastTrade', 'BuyNShip', 'ZoomEx']
sellers = ['Exporters Inc', 'Mega Traders', 'SellFast', 'TradeX', 'QuickExports']

# Generate synthetic data
data = {
    "Invoice ID": [f"INV{1000+i}" for i in range(num_rows)],
    "Buyer": [random.choice(buyers) for _ in range(num_rows)],
    "Seller": [random.choice(sellers) for _ in range(num_rows)],
    "Amount": np.random.randint(1000, 90000, size=num_rows),
    "Product": [random.choice(products) for _ in range(num_rows)],
    "Date": pd.date_range(start="2024-01-01", periods=num_rows, freq='D').strftime('%Y-%m-%d').tolist()
}

df = pd.DataFrame(data)

# Inject anomalies
for i in range(10):
    df.at[i, 'Invoice ID'] = df.at[0, 'Invoice ID']  # duplicate invoice
for i in range(20, 30):
    df.at[i, 'Amount'] = 200000  # unusually high amount

# Save to file
df.to_csv("data/sample_trade_data.csv", index=False)
print("✅ Dataset saved to data/sample_trade_data.csv")
