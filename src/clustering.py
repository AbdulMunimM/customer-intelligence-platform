import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

def calculate_wcss(data, k_range=range(2, 11)):
    """
    Calculate WCSS for different values of K.
    """

    wcss = []

    for k in k_range:

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(data)

        wcss.append(model.inertia_)

    return list(k_range), wcss

def calculate_silhouette_scores(data, k_range=range(2, 11)):
    """
    Calculate silhouette scores for different values of K.
    """

    scores = []

    for k in k_range:

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        labels = model.fit_predict(data)

        score = silhouette_score(data, labels)

        scores.append(score)

    return scores

def train_kmeans(data, n_clusters=4):
    """
    Train the K-Means model.
    """

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(data)

    return model, labels

def add_clusters(rfm, labels):
    """
    Add cluster labels to the RFM dataframe.
    """

    rfm = rfm.copy()

    rfm["Cluster"] = labels

    return rfm

def create_cluster_summary(rfm):
    """
    Create summary statistics for each cluster.
    """

    summary = (
        rfm
        .groupby("Cluster")[["Recency", "Frequency", "Monetary"]]
        .mean()
        .round(2)
    )

    return summary

def perform_pca(data, n_components=2):
    """
    Reduce dimensions using PCA.
    """

    pca = PCA(n_components=n_components)

    components = pca.fit_transform(data)

    pca_df = pd.DataFrame(
        components,
        columns=["PC1", "PC2"]
    )

    return pca, pca_df

def add_cluster_to_pca(pca_df, labels):
    """
    Add cluster labels to PCA dataframe.
    """

    pca_df = pca_df.copy()

    pca_df["Cluster"] = labels

    return pca_df

import joblib

from src.config import MODELS


def save_models(kmeans, scaler, pca):
    """
    Save trained models.
    """

    joblib.dump(
        kmeans,
        MODELS / "kmeans_model.pkl"
    )

    joblib.dump(
        scaler,
        MODELS / "scaler.pkl"
    )

    joblib.dump(
        pca,
        MODELS / "pca.pkl"
    )

    print("Models saved successfully.")