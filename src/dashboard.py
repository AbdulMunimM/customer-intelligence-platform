"""
dashboard.py

Loads processed datasets and provides dashboard metrics
for the Streamlit application.
"""

import pandas as pd

from src.config import PROCESSED_DATA


# ==========================================================
# LOAD DATA
# ==========================================================

clean_df = pd.read_csv(PROCESSED_DATA / "clean_data.csv")
rfm = pd.read_csv(PROCESSED_DATA / "rfm.csv")
clustered_df = pd.read_csv(PROCESSED_DATA / "clustered_customers.csv")
cluster_summary = pd.read_csv(PROCESSED_DATA / "cluster_summary.csv")
evaluation = pd.read_csv(PROCESSED_DATA / "evaluation.csv")
pca_df = pd.read_csv(PROCESSED_DATA / "pca.csv")


# ==========================================================
# DASHBOARD METRICS
# ==========================================================

def get_dashboard_metrics():
    """
    Returns high-level KPIs for the Executive Dashboard.
    """

    metrics = {

        "revenue":
            clean_df["TotalAmount"].sum(),

        "customers":
            rfm.shape[0],

        "transactions":
            len(clean_df),

        "countries":
            clean_df["Country"].nunique(),

        "vip_customers":
            (clustered_df["Cluster"] == 2).sum(),

        "average_order_value":
            clean_df["TotalAmount"].mean(),

        "average_customer_value":
            rfm["Monetary"].mean(),

        "average_frequency":
            rfm["Frequency"].mean(),

        "average_recency":
            rfm["Recency"].mean()
    }

    return metrics


# ==========================================================
# RETURN DATASETS
# ==========================================================

def get_clean_data():
    return clean_df.copy()


def get_rfm():
    return rfm.copy()


def get_clustered_data():
    return clustered_df.copy()


def get_cluster_summary():
    return cluster_summary.copy()


def get_evaluation():
    return evaluation.copy()


def get_pca_data():
    return pca_df.copy()


# ==========================================================
# CHART DATA
# ==========================================================

def revenue_by_country(top_n=10):
    """
    Top countries by revenue.
    """

    country = (
        clean_df
        .groupby("Country")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    return country


def customer_segments():
    """
    Number of customers in each cluster.
    """

    segment = (
        clustered_df["Cluster"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    segment.columns = ["Cluster", "Customers"]

    return segment


def monthly_revenue():
    """
    Monthly revenue trend.
    """

    df = clean_df.copy()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    df["Month"] = (
        df["InvoiceDate"]
        .dt
        .to_period("M")
        .astype(str)
    )

    revenue = (
        df.groupby("Month")["TotalAmount"]
        .sum()
        .reset_index()
    )

    return revenue


# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

def get_business_insights():
    """
    Generate simple business insights.
    """

    total_customers = len(clustered_df)

    vip = (
        clustered_df["Cluster"] == 2
    ).sum()

    vip_percent = vip / total_customers * 100

    lost = (
        clustered_df["Cluster"] == 0
    ).sum()

    lost_percent = lost / total_customers * 100

    insights = [

        {
            "title":
                "VIP Customers",

            "value":
                f"{vip_percent:.1f}%",

            "message":
                "of customers belong to the VIP segment."
        },

        {
            "title":
                "Lost Customers",

            "value":
                f"{lost_percent:.1f}%",

            "message":
                "of customers are inactive and may require a re-engagement campaign."
        },

        {
            "title":
                "Recommendation",

            "value":
                "Priority",

            "message":
                "Focus on retaining VIP customers while launching targeted campaigns for lost customers."
        }

    ]

    return insights


# ==========================================================
# PROJECT SUMMARY
# ==========================================================

def project_summary():
    """
    Returns project statistics.
    """

    return {

        "clean_rows":
            len(clean_df),

        "customers":
            len(rfm),

        "clusters":
            clustered_df["Cluster"].nunique(),

        "countries":
            clean_df["Country"].nunique(),

        "revenue":
            clean_df["TotalPrice"].sum()
    }