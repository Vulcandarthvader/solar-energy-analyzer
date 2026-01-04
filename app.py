import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Solar ROI Analyzer",
    layout="centered"
)

st.title("☀️ Solar Power ROI Analyzer")
st.write(
    "Analyze solar generation, year-wise savings, and investment payback "
    "using real household electricity and solar data."
)

# -------------------------------
# Upload CSV
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload your electricity + solar CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    # -------------------------------
    # Load data
    # -------------------------------
    df = pd.read_csv(uploaded_file)

    # -------------------------------
    # Sidebar inputs
    # -------------------------------
    st.sidebar.header("Assumptions")

    GRID_TARIFF = st.sidebar.slider(
        "Grid Tariff (₹ / kWh)",
        min_value=4.0,
        max_value=10.0,
        value=6.5,
        step=0.1
    )

    INSTALL_COST = st.sidebar.number_input(
        "Installation Cost (₹)",
        value=170000,
        step=10000
    )

    # -------------------------------
    # Preprocessing
    # -------------------------------
    df["date"] = pd.to_datetime(
        df["year"].astype(str) + "-" + df["month"].astype(str) + "-01"
    )

    solar_df = df[df["solar_kwh"] > 0].copy()
    solar_df = solar_df.sort_values("date")

    # -------------------------------
    # Solar generation trend
    # -------------------------------
    st.subheader("📈 Monthly Solar Generation")

    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(
        solar_df["date"],
        solar_df["solar_kwh"],
        marker="o"
    )

    ax1.set_xlabel("Date")
    ax1.set_ylabel("Solar Generation (kWh)")
    ax1.set_title("Monthly Solar Generation Trend")

    plt.xticks(rotation=45)
    ax1.xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.tight_layout()

    st.pyplot(fig1)

    # -------------------------------
    # Annual solar & savings
    # -------------------------------
    annual_solar = solar_df.groupby("year")["solar_kwh"].sum()
    annual_savings = annual_solar * GRID_TARIFF
    cumulative_savings = annual_savings.cumsum()

    # -------------------------------
    # Year-wise savings bar chart
    # -------------------------------
    st.subheader("💸 Year-wise Savings")

    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.bar(
        annual_savings.index.astype(str),
        annual_savings.values
    )

    ax2.set_xlabel("Year")
    ax2.set_ylabel("Savings (₹)")
    ax2.set_title("Annual Savings from Solar Power")

    plt.tight_layout()
    st.pyplot(fig2)

    # -------------------------------
    # Cumulative ROI curve
    # -------------------------------
    st.subheader("📊 Cumulative Savings & Payback")

    fig3, ax3 = plt.subplots(figsize=(8, 4))
    ax3.plot(
        cumulative_savings.index.astype(str),
        cumulative_savings.values,
        marker="o",
        label="Cumulative Savings"
    )

    ax3.axhline(
        INSTALL_COST,
        color="red",
        linestyle="--",
        label="Installation Cost"
    )

    ax3.set_xlabel("Year")
    ax3.set_ylabel("Amount (₹)")
    ax3.set_title("Solar Investment Payback Curve")
    ax3.legend()

    plt.tight_layout()
    st.pyplot(fig3)

    # -------------------------------
    # Break-even year
    # -------------------------------
    break_even = cumulative_savings[cumulative_savings >= INSTALL_COST]

    if break_even.empty:
        st.warning("Break-even not reached within available years.")
    else:
        st.success(f"✅ Break-even Year: {break_even.index[0]}")

    # -------------------------------
    # Summary table
    # -------------------------------
    st.subheader("📋 Savings Summary")

    summary_df = pd.DataFrame({
        "Annual Savings (₹)": annual_savings.round(0),
        "Cumulative Savings (₹)": cumulative_savings.round(0)
    })

    st.dataframe(summary_df)

else:
    st.info("⬆️ Upload your CSV file to begin.")
