# 🚨 Trade Fraud Detector

A lightweight fraud detection system built with **Python** and **Streamlit** to identify suspicious transactions in trade datasets using both **rule-based logic** and **machine learning**.

---

## 📦 Features

- 🔍 **Anomaly Detection**
  - Duplicate Invoice ID detection
  - High-amount transaction flagging
  - Isolation Forest for unsupervised anomaly detection

- 📊 **Visualizations**
  - Outlier scatterplot of transaction amounts
  - Invoice amount trends over time

- 📂 **CSV Upload Support**
  - Upload any properly structured trade data file
  - View flagged anomalies instantly

- 🖥️ **Streamlit UI**
  - Clean, intuitive interface for uploading, visualizing, and reviewing data

---

## 🗂️ Dataset Format

CSV file with the following headers:

```csv
Invoice ID, Buyer, Seller, Amount, Product, Date
```

**Example:**

| Invoice ID | Buyer       | Seller        | Amount | Product | Date       |
|------------|-------------|---------------|--------|---------|------------|
| INV1001    | ABC Ltd     | Exporters Inc | 35000  | Tea     | 2024-01-01 |
| INV1002    | FastTrade   | Mega Traders  | 200000 | Copper  | 2024-01-02 |

---

## 🚀 How to Run

### 📌 1. Clone this Repo
```bash
git clone https://github.com/your-username/Trade-Fraud-Detector.git
cd Trade-Fraud-Detector
```

### 📌 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 📌 3. Run the App
```bash
streamlit run app.py
```

---

## 💡 Technology Stack

- **Python 3.8+**
- **Pandas** — data processing
- **Matplotlib / Seaborn** — data visualization
- **Scikit-learn** — Isolation Forest anomaly detection
- **Streamlit** — frontend dashboard

---

## 📁 Project Structure

```
TradeFraudDetector/
├── app.py                  # Streamlit UI
├── src/
│   ├── trade_fraud_detector.py
│   └── generate_trade_data.py
├── data/
│   ├── sample_trade_data.csv
│   └── flagged_anomalies.csv (generated)
├── output/
│   ├── amount_outliers.png
│   └── invoice_trend.png
├── requirements.txt
├── README.md
```

---

## 🛠️ Future Improvements
- Streamlit Cloud deployment
- Download flagged results directly from UI
- Allow user-defined thresholds in interface
- Additional unsupervised techniques (e.g., DBSCAN)

---

## 👨‍💻 Author

Built with 💻 by [Mudit Gupta](https://github.com/muditttgupta)
