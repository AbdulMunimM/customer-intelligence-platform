# 📊 Customer Intelligence Platform

An end-to-end Machine Learning project that performs customer segmentation using **RFM Analysis** and **K-Means Clustering**, providing actionable business insights through an interactive Streamlit dashboard.

---

## Overview

Customer Intelligence Platform helps businesses understand customer purchasing behavior by grouping customers into meaningful segments based on:

- Recency
- Frequency
- Monetary Value (RFM)

The application includes a complete machine learning pipeline, customer prediction, business recommendations, and an interactive dashboard for data exploration.

---

## Features

- Customer data cleaning and preprocessing
- Feature engineering using RFM Analysis
- Log transformation and feature scaling
- Customer segmentation using K-Means Clustering
- Cluster evaluation using WCSS and Silhouette Score
- PCA for dimensionality reduction and visualization
- Customer segment prediction
- Business recommendations for each customer segment
- Interactive Streamlit dashboard
- Downloadable reports

---

## Machine Learning Pipeline

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
RFM Analysis
      │
      ▼
Log Transformation
      │
      ▼
Standard Scaling
      │
      ▼
K-Means Clustering
      │
      ▼
Cluster Evaluation
      │
      ▼
PCA Visualization
      │
      ▼
Prediction API
      │
      ▼
Interactive Dashboard
```

---

## Dataset

**Online Retail Store Dataset**

Contains two years of transaction history including:

- Invoice Number
- Stock Code
- Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

---

## Project Structure

```
Customer Intelligence Platform
│
├── app.py
├── main.py
├── requirements.txt
│
├── data
│   ├── raw
│   └── processed
│
├── models
│   ├── scaler.pkl
│   ├── kmeans_model.pkl
│   └── pca.pkl
│
├── reports
│
└── src
    ├── business.py
    ├── clustering.py
    ├── config.py
    ├── dashboard.py
    ├── data_loader.py
    ├── feature_engineering.py
    ├── predict.py
    └── preprocessing.py
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Streamlit

---

## Customer Segments

### Cluster 0 — Inactive Customers
- Low spending
- Low purchase frequency
- Long inactive period

### Cluster 1 — Regular Customers
- Moderate spending
- Consistent purchasing behavior

### Cluster 2 — VIP Customers
- Highest revenue contribution
- High purchase frequency
- Loyal customers

### Cluster 3 — High Value Customers
- Strong purchasing potential
- Suitable for loyalty campaigns

---

## Dashboard Modules

- Executive Dashboard
- Customer Explorer
- Customer Segments
- Business Analytics
- AI Insights
- Customer Predictor
- Reports
- Project Overview

---

## Model Evaluation

The project evaluates clustering performance using:

- WCSS (Elbow Method)
- Silhouette Score

The optimal number of clusters was selected after comparing multiple K values.

---

## Business Value

This project demonstrates how machine learning can help organizations:

- Identify high-value customers
- Reduce customer churn
- Improve customer retention
- Design targeted marketing campaigns
- Increase customer lifetime value
- Support business decision making

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the preprocessing and model training pipeline:

```bash
python main.py
```

Launch the dashboard:

```bash
streamlit run app.py
```

---

## Author

**Abdul Munim Bandesha**

AI Developer | Machine Learning | Data Analytics

---

## License

This project is developed for educational and portfolio purposes.