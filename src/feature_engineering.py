import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def calculate_total_amount(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create TotalAmount column.
    """

    df = df.copy()

    df["TotalAmount"] = df["Quantity"] * df["Price"]

    return df

def create_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create Recency, Frequency and Monetary features.
    """

    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("Customer ID").agg({

        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,

        "Invoice": "nunique",

        "TotalAmount": "sum"

    })

    rfm.columns = [
        "Recency",
        "Frequency",
        "Monetary"
    ]

    return rfm

def log_transform(rfm: pd.DataFrame) -> pd.DataFrame:
    """
    Apply log transformation to RFM features.
    """

    rfm_log = np.log1p(rfm)

    return rfm_log

def scale_features(rfm_log: pd.DataFrame):
    """
    Standardize RFM features.
    """

    scaler = StandardScaler()

    scaled = scaler.fit_transform(rfm_log)

    scaled_df = pd.DataFrame(
        scaled,
        columns=rfm_log.columns,
        index=rfm_log.index
    )

    return scaled_df, scaler

def prepare_features(df: pd.DataFrame):
    """
    Complete feature engineering pipeline.

    Returns
    -------
    rfm : DataFrame
        Original RFM features

    rfm_log : DataFrame
        Log-transformed RFM features

    rfm_scaled : DataFrame
        Standardized RFM features

    scaler : StandardScaler
        Fitted scaler
    """

    df = calculate_total_amount(df)

    rfm = create_rfm(df)

    rfm_log = log_transform(rfm)

    rfm_scaled, scaler = scale_features(rfm_log)

    return rfm, rfm_log, rfm_scaled, scaler