# app.py - Streamlit UI for Trade Fraud Detector

import streamlit as st
import pandas as pd
import os
import sys

# Add src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from trade_fraud_detector import (
    preprocess_data,
    rule_based_detection,
    detect_anomalies_isolation_forest,
    plot_amount_outliers,
    plot_invoice_trend
)

st.set_page_config(page_title="Trade Fraud Detector", layout="wide")
st.title("🚨 Trade Fraud Detection System")

uploaded_file = st.file_uploader("Upload a Trade CSV file", type="csv")

if uploaded_file:
    st.subheader("📄 Uploaded Data Preview")
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    # Run pipeline
    df = preprocess_data(df)
    df = rule_based_detection(df)
    df = detect_anomalies_isolation_forest(df)
    df['final_anomaly'] = df['duplicate_invoice'] | df['high_amount'] | df['is_anomaly_iforest']

    # Show anomalies
    st.subheader("🚩 Flagged Anomalies")
    st.dataframe(df[df['final_anomaly']])

    # Save for external use
    os.makedirs("data", exist_ok=True)
    df[df['final_anomaly']].to_csv("data/flagged_anomalies.csv", index=False)

    # Generate plots
    os.makedirs("output", exist_ok=True)
    plot_amount_outliers(df)
    plot_invoice_trend(df)

    st.subheader("📊 Visualizations")
    st.image("output/amount_outliers.png", caption="Anomalies in Transaction Amounts")
    st.image("output/invoice_trend.png", caption="Invoice Amount Trend Over Time")

    st.success("✅ Analysis complete. Results saved to data/ and output/ folders.")

else:
    st.info("👆 Upload a CSV file to get started.")
