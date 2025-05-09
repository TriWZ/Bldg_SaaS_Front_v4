
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Triphorium Energy Dashboard", layout="wide")

st.title("🏢 Triphorium Energy Dashboard")

uploaded_file = st.file_uploader("Upload your building energy CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    
    # 分四列显示各项趋势图
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.subheader("⚡ Electricity Consumption (kWh)")
        fig1 = px.line(df, x="timestamp", y="electricity_kwh", title="Electricity Over Time")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("💧 Water Usage (tons)")
        fig2 = px.line(df, x="timestamp", y="water_tons", title="Water Usage Over Time")
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        st.subheader("🔥 Gas Consumption (m³)")
        fig3 = px.line(df, x="timestamp", y="gas_m3", title="Gas Consumption Over Time")
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("🌫️ CO2 Emissions (tons)")
        fig4 = px.line(df, x="timestamp", y="co2_tons", title="CO2 Emissions Over Time")
        st.plotly_chart(fig4, use_container_width=True)
