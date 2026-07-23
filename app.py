import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from src.config import PROCESSED_DATA
from src.dashboard import get_dashboard_metrics
from streamlit_option_menu import option_menu

from src.dashboard import get_dashboard_metrics
from src.predict import predict_cluster


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Customer Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# CUSTOM CSS
# =====================================================

import textwrap

st.markdown(
    textwrap.dedent("""
    <div style="
        background:linear-gradient(90deg,#2563EB,#1D4ED8);
        padding:30px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1 style="margin-bottom:5px;">
            📊 Customer Intelligence Platform
        </h1>
        <p style="font-size:18px;margin-bottom:0;">
            AI-Powered Customer Segmentation & Business Intelligence
        </p>
    </div>
    """),
    unsafe_allow_html=True
)


# =====================================================
# METRIC CARD
# =====================================================

def metric_card(title, value, subtitle, icon):

    st.markdown(
f"""<div class="metric-card">
<h4 style="margin-bottom:10px;">{icon} {title}</h4>
<h2 style="margin-top:0px;">{value}</h2>
<p style="color:gray;">{subtitle}</p>
</div>""",
        unsafe_allow_html=True
    )

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("# 📊")
    st.markdown("## Customer Intelligence")
    st.caption("AI-Powered Business Intelligence")

    st.divider()

    selected = option_menu(
        menu_title=None,

        options=[
            "Dashboard",
            "Customers",
            "Segments",
            "Analytics",
            "AI Insights",
            "Predictor",
            "Reports",
            "About"
        ],

        icons=[
            "speedometer2",
            "people",
            "diagram-3",
            "graph-up",
            "robot",
            "bullseye",
            "file-earmark-text",
            "info-circle"
        ],

        default_index=0,

        styles={

            "container": {
                "padding": "0!important",
                "background-color": "#F8FAFC"
            },

            "icon": {
                "color": "#60A5FA",
                "font-size": "18px"
            },

            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "4px",
                "--hover-color": "#E2E8F0"
            },

            "nav-link-selected": {
                "background-color": "#2563EB"
            }

        }
    )


# =====================================================
# PAGE ROUTING
# =====================================================

if selected == "Dashboard":

    metrics = get_dashboard_metrics()

    st.subheader("Executive Dashboard")

    st.write("")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        metric_card(
            "Revenue",
            f"£{metrics['revenue']:,.2f}",
            "Total Revenue",
            "💰"
        )

    with col2:
        metric_card(
            "Customers",
            f"{metrics['customers']:,}",
            "Unique Customers",
            "👥"
        )

    with col3:
        metric_card(
            "Transactions",
            f"{metrics['transactions']:,}",
            "Completed Orders",
            "🧾"
        )

    with col4:
        metric_card(
            "Countries",
            metrics["countries"],
            "Markets Served",
            "🌍"
        )

    with col5:
        metric_card(
            "VIP Customers",
            metrics["vip_customers"],
            "High Value Customers",
            "👑"
        )

    st.write("")
    st.divider()

    left, right = st.columns([2, 1])

    with left:

        st.subheader("Business Summary")

        st.markdown(f"""
**Total Revenue:** **£{metrics['revenue']:,.2f}**

**Average Customer Value:** **£{metrics['average_customer_value']:,.2f}**

**Average Order Value:** **£{metrics['average_order_value']:,.2f}**

**Average Purchase Frequency:** **{metrics['average_frequency']:.2f}**

**Average Recency:** **{metrics['average_recency']:.2f} days**
""")

    with right:

        st.subheader("Project Status")

        st.success("✔ Data Cleaning")

        st.success("✔ Feature Engineering")

        st.success("✔ RFM Analysis")

        st.success("✔ K-Means Clustering")

        st.success("✔ Customer Prediction")

        st.success("✔ Streamlit Dashboard")

    st.divider()

    st.info(
        "This dashboard summarizes the complete customer segmentation pipeline built using Machine Learning and RFM Analysis."
    )

# =====================================================
# CUSTOMER PREDICTOR
# =====================================================

elif selected == "Predictor":

    st.subheader("Customer Segment Predictor")

    st.write(
        "Enter the customer's RFM values to predict the customer segment."
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        recency = st.number_input(
            "Recency (Days)",
            min_value=1,
            value=30,
            step=1
        )

    with col2:
        frequency = st.number_input(
            "Frequency",
            min_value=1,
            value=5,
            step=1
        )

    with col3:
        monetary = st.number_input(
            "Monetary (£)",
            min_value=1.0,
            value=1000.0,
            step=100.0
        )

    st.write("")

    if st.button(
        "Predict Customer Segment",
        use_container_width=True
    ):

        cluster, info = predict_cluster(
            recency=recency,
            frequency=frequency,
            monetary=monetary
        )

        st.success("Prediction Completed Successfully")

        st.write("")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Predicted Cluster",
                cluster
            )

            st.metric(
                "Priority",
                info["priority"]
            )

        with c2:

            st.metric(
                "Customer Segment",
                info["name"]
            )

        st.write("")

        st.subheader("Segment Description")

        st.info(info["description"])

        st.subheader("Business Recommendation")

        st.success(info["recommendation"])

# =====================================================
# CUSTOMER EXPLORER
# =====================================================

elif selected == "Customers":

    st.subheader("Customer Explorer")

    rfm = pd.read_csv(PROCESSED_DATA / "rfm.csv")

    # -----------------------------
    # Customer KPIs
    # -----------------------------

    total_customers = len(rfm)

    active_customers = len(
        rfm[rfm["Recency"] <= 30]
    )

    loyal_customers = len(
        rfm[rfm["Frequency"] >= 10]
    )

    high_value_customers = len(
        rfm[rfm["Monetary"] >= 5000]
    )

    inactive_customers = len(
        rfm[rfm["Recency"] > 180]
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        metric_card(
            "Customers",
            f"{total_customers:,}",
            "Customer Database",
            "👥"
        )

    with c2:
        metric_card(
            "Active",
            f"{active_customers:,}",
            "Last 30 Days",
            "🟢"
        )

    with c3:
        metric_card(
            "Loyal",
            f"{loyal_customers:,}",
            "Frequent Buyers",
            "⭐"
        )

    with c4:
        metric_card(
            "High Value",
            f"{high_value_customers:,}",
            "Top Spending",
            "💎"
        )

    with c5:
        metric_card(
            "Inactive",
            f"{inactive_customers:,}",
            "Need Attention",
            "🔴"
        )

    st.divider()

    # -----------------------------
    # Search Customer
    # -----------------------------

    search = st.text_input(
        "🔍 Search Customer ID"
    )

    if search:

        filtered = rfm[
            rfm["Customer ID"].astype(str).str.contains(
                search,
                case=False
            )
        ]

    else:

        filtered = rfm

    st.dataframe(
        filtered,
        use_container_width=True,
        height=500
    )

    st.download_button(
        "Download Customer Data",
        filtered.to_csv(index=False),
        "customers.csv",
        "text/csv"
    )


# =====================================================
# CUSTOMER SEGMENTS
# =====================================================

elif selected == "Segments":

    st.subheader("Customer Segments")

    st.markdown("""
### Available Customer Segments

**Cluster 0 — Inactive Customers**
- Low spending
- Low purchase frequency
- Long time since last purchase

---

**Cluster 1 — Regular Customers**
- Active customers
- Moderate purchase frequency
- Moderate spending

---

**Cluster 2 — VIP Customers**
- Highest revenue contribution
- High purchase frequency
- Loyal customers

---

**Cluster 3 — High Value Customers**
- Good spending
- Moderate frequency
- Opportunity to become VIP
""")



# =====================================================
# BUSINESS ANALYTICS
# =====================================================

elif selected == "Analytics":

    st.subheader("Business Analytics")

    cluster_summary = pd.read_csv(
        PROCESSED_DATA / "cluster_summary.csv"
    )

    evaluation = pd.read_csv(
        PROCESSED_DATA / "evaluation.csv"
    )

    rfm = pd.read_csv(
        PROCESSED_DATA / "clustered_customers.csv"
    )

    # ---------------------------------
    # Charts
    # ---------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Revenue by Segment")

        revenue = (
            rfm.groupby("Cluster")["Monetary"]
            .sum()
            .reset_index()
        )

        st.bar_chart(
            revenue,
            x="Cluster",
            y="Monetary",
            use_container_width=True
        )

    with col2:

        st.markdown("### Customer Distribution")

        distribution = (
            rfm["Cluster"]
            .value_counts()
            .sort_index()
        )

        st.pyplot(
            distribution.plot.pie(
                autopct="%1.1f%%",
                ylabel=""
            ).get_figure()
        )

    st.divider()

    # ---------------------------------
    # Cluster Summary
    # ---------------------------------

    st.markdown("### Cluster Summary")

    st.dataframe(
        cluster_summary,
        use_container_width=True
    )

    st.divider()

    # ---------------------------------
    # Model Evaluation
    # ---------------------------------

    st.markdown("### K-Means Evaluation")

    st.dataframe(
        evaluation,
        use_container_width=True
    )


# =====================================================
# AI INSIGHTS
# =====================================================

elif selected == "AI Insights":

    st.subheader("AI Business Insights")

    st.success("✔ VIP customers generate the highest business value.")

    st.success("✔ Inactive customers represent the largest customer segment.")

    st.success("✔ High Value customers are suitable targets for loyalty campaigns.")

    st.success("✔ Regular customers have potential to become VIP customers.")



# =====================================================
# REPORTS
# =====================================================

elif selected == "Reports":

    st.subheader("Reports & Downloads")

    reports = [
        "clean_data.csv",
        "rfm.csv",
        "cluster_summary.csv",
        "evaluation.csv",
        "pca.csv"
    ]

    for report in reports:

        path = PROCESSED_DATA / report

        with open(path, "rb") as file:

            st.download_button(
                label=f"Download {report}",
                data=file,
                file_name=report,
                mime="text/csv"
            )



# =====================================================
# ABOUT
# =====================================================

elif selected == "About":

    st.subheader("About Customer Intelligence Platform")

    st.markdown("""
### Project Overview

Customer Intelligence Platform is an end-to-end Machine Learning project that performs customer segmentation using **RFM Analysis** and **K-Means Clustering**.

---

### Machine Learning Pipeline

- Data Collection
- Data Cleaning
- Feature Engineering
- RFM Analysis
- Log Transformation
- Standard Scaling
- K-Means Clustering
- PCA
- Customer Prediction
- Business Recommendations
- Streamlit Dashboard

---

### Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

### Developed By

**Abdul Munim Bandesha**

AI Developer | Machine Learning | Data Analytics
""")