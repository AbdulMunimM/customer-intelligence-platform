"""
main.py

Customer Intelligence Platform
End-to-end ML pipeline
"""

import pandas as pd

from src.config import (
    RAW_DATA,
    PROCESSED_DATA,
)

from src.data_loader import load_online_retail_dataset
from src.preprocessing import clean_data
from src.feature_engineering import prepare_features

from src.clustering import (
    calculate_wcss,
    calculate_silhouette_scores,
    train_kmeans,
    add_clusters,
    create_cluster_summary,
    perform_pca,
    add_cluster_to_pca,
    save_models,
)

# ==========================================================
# LOAD DATA
# ==========================================================

excel_file = RAW_DATA / "online_retail_store_data.xlsx"

df = load_online_retail_dataset(excel_file)

print("Before Cleaning:", df.shape)

# ==========================================================
# DATA CLEANING
# ==========================================================

clean_df, cleaning_summary = clean_data(df)

print("After Cleaning:", clean_df.shape)
print(cleaning_summary)

# ==========================================================
# FEATURE ENGINEERING
# ==========================================================

rfm, rfm_log, rfm_scaled, scaler = prepare_features(clean_df)

print("\nRFM Shape:", rfm.shape)
print(rfm.head())

print("\nScaled RFM Shape:", rfm_scaled.shape)
print(rfm_scaled.head())

# Save original RFM BEFORE clustering
rfm.to_csv(
    PROCESSED_DATA / "rfm.csv",
    index=True
)

# ==========================================================
# MODEL EVALUATION
# ==========================================================

k_values, wcss = calculate_wcss(rfm_scaled)

silhouette_scores = calculate_silhouette_scores(rfm_scaled)

evaluation = pd.DataFrame({
    "K": k_values,
    "WCSS": wcss,
    "Silhouette Score": silhouette_scores
})

print("\nEvaluation Metrics")
print(evaluation)

# ==========================================================
# TRAIN FINAL MODEL
# ==========================================================

kmeans, labels = train_kmeans(
    rfm_scaled,
    n_clusters=4
)

rfm = add_clusters(rfm, labels)

print("\nCluster Counts")
print(rfm["Cluster"].value_counts().sort_index())

cluster_summary = create_cluster_summary(rfm)

print("\nCluster Summary")
print(cluster_summary)

# ==========================================================
# PCA
# ==========================================================

pca, pca_df = perform_pca(rfm_scaled)

pca_df = add_cluster_to_pca(
    pca_df,
    labels
)

print("\nPCA Shape")
print(pca_df.shape)
print(pca_df.head())

# ==========================================================
# SAVE MODELS
# ==========================================================

save_models(
    kmeans,
    scaler,
    pca
)

print("\nModels saved successfully.")

# ==========================================================
# PREPARE DATASETS FOR DASHBOARD
# ==========================================================

clean_df["TotalAmount"] = (
    clean_df["Quantity"] *
    clean_df["Price"]
)

# ==========================================================
# SAVE DATASETS
# ==========================================================

clean_df.to_csv(
    PROCESSED_DATA / "clean_data.csv",
    index=False
)

rfm.to_csv(
    PROCESSED_DATA / "clustered_customers.csv",
    index=True
)

cluster_summary.to_csv(
    PROCESSED_DATA / "cluster_summary.csv",
    index=True
)

evaluation.to_csv(
    PROCESSED_DATA / "evaluation.csv",
    index=False
)

pca_df.to_csv(
    PROCESSED_DATA / "pca.csv",
    index=False
)

print("\nDatasets saved successfully.")