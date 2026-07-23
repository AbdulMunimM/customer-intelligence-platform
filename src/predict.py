import joblib
import numpy as np
import pandas as pd

from src.config import MODELS
from src.business import get_cluster_info


def load_models():
    """
    Load trained scaler and KMeans model.
    """
    scaler = joblib.load(MODELS / "scaler.pkl")
    model = joblib.load(MODELS / "kmeans_model.pkl")

    return scaler, model


def prepare_customer(recency, frequency, monetary):
    """
    Prepare customer features for prediction.
    """

    customer = pd.DataFrame({
        "Recency": [recency],
        "Frequency": [frequency],
        "Monetary": [monetary]
    })

    # Apply the same log transformation used during training
    customer = np.log1p(customer)

    return customer


def predict_cluster(recency, frequency, monetary):
    """
    Predict the customer segment.
    """

    scaler, model = load_models()

    customer = prepare_customer(
        recency,
        frequency,
        monetary
    )

    # Scale features
    customer_scaled = scaler.transform(customer)

    # Convert back to DataFrame to preserve feature names
    customer_scaled = pd.DataFrame(
        customer_scaled,
        columns=["Recency", "Frequency", "Monetary"]
    )

    # Predict cluster
    cluster = int(model.predict(customer_scaled)[0])

    # Get business interpretation
    info = get_cluster_info(cluster)

    return cluster, info