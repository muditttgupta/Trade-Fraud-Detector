# trade_fraud_detector.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import os

# Preprocess the uploaded dataset
def preprocess_data(df):
    df = df[['Invoice ID', 'Buyer', 'Seller', 'Amount', 'Product', 'Date']]
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df.dropna(subset=['Invoice ID', 'Amount'], inplace=True)
    return df

# Rule-based anomaly detection
def rule_based_detection(df):
    df['duplicate_invoice'] = df.duplicated(subset=['Invoice ID'], keep=False)
    df['high_amount'] = df['Amount'] > 100000  # customizable threshold
    return df

# Optional ML-based anomaly detection using Isolation Forest
def detect_anomalies_isolation_forest(df):
    X = df[['Amount']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    df['anomaly_iforest'] = model.fit_predict(X_scaled)
    df['is_anomaly_iforest'] = df['anomaly_iforest'] == -1
    return df

# Plot outliers

def plot_amount_outliers(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=df.index, y='Amount', hue='final_anomaly', palette={True: 'red', False: 'blue'})
    plt.title("Transaction Amount Anomalies")
    plt.xlabel("Transaction Index")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("output/amount_outliers.png")
    plt.close()

# Plot invoice trends
def plot_invoice_trend(df):
    plt.figure(figsize=(10, 6))
    df_sorted = df.sort_values('Date')
    sns.lineplot(data=df_sorted, x='Date', y='Amount')
    plt.title("Invoice Amount Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("output/invoice_trend.png")
    plt.close()

# Main function
def main(csv_path):
    if not os.path.exists(csv_path):
        print(f"File {csv_path} not found.")
        return

    df = pd.read_csv(csv_path)
    df = preprocess_data(df)
    df = rule_based_detection(df)
    df = detect_anomalies_isolation_forest(df)

    df['final_anomaly'] = df['duplicate_invoice'] | df['high_amount'] | df['is_anomaly_iforest']

    flagged = df[df['final_anomaly']]
    os.makedirs("data", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    flagged.to_csv("data/flagged_anomalies.csv", index=False)

    print("Flagged anomalies saved to 'data/flagged_anomalies.csv'")
    plot_amount_outliers(df)
    plot_invoice_trend(df)
    print("Plots saved to 'output/' folder")

if __name__ == "__main__":
    main("data/sample_trade_data.csv")

