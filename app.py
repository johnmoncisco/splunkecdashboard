import streamlit as st
import pandas as pd
import numpy as np
from streamlit_agraph import agraph, Node, Config

# Page Configuration
st.set_page_config(layout="wide", page_title="Live DC Compliance")

# Assets
base_url = "https://raw.githubusercontent.com/johnmoncisco/splunkecdashboard/main/assets/"
svg_icon = base_url + "dc-svg.svg"

# Sidebar for Simulation Controls
st.sidebar.header("Simulation Settings")
live_mode = st.sidebar.checkbox("Enable Live Telemetry", value=True)

# Generate Dynamic Values
if live_mode:
    pue = round(1.24 + np.random.uniform(-0.02, 0.02), 3)
    it_load = round(58427.42 + np.random.uniform(-50, 50), 2)
else:
    pue = 1.24
    it_load = 58427.42

# Header Section
st.title("splunk> enterprise")
st.subheader("EU EED & EnEfG Compliance Monitoring Dashboard")
st.divider()

# --- Topology View ---
with st.container():
    st.markdown("<div style='text-align: center; font-size: 24px; font-weight: bold; color: #2c3e50;'>Frankfurt DC-04</div>", unsafe_allow_html=True)
    nodes = [Node(id="DC", label="", size=200, shape="image", image=svg_icon)]
    config = Config(width=800, height=300, directed=False, physics=False, backgroundColor="#ffffff")
    agraph(nodes=nodes, edges=[], config=config)

st.divider()

# --- Live Metrics Section ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("PUE", f"{pue}", f"{round(pue-1.24, 3)}")
m2.metric("WUE", "0.18 L/kWh", "Stable")
m3.metric("ERF", "11.4 %", "Steady")
m4.metric("IT Load (MWh)", f"{it_load:,.2f}", "Fluctuating")

# --- Tables ---
col_left, col_right = st.columns(2)
with col_left:
    st.markdown("#### Energy Consumption (MWh)")
    st.table(pd.DataFrame({"Source": ["Facility Input", "IT Load"], "MWh": [72450.00, it_load]}))
with col_right:
    st.markdown("#### Telemetry Summary")
    st.table(pd.DataFrame({"Metric": ["Active Servers", "Storage"], "Value": ["14,280", "184.50 PB"]}))

# Auto-refresh button (hidden, or manual)
if live_mode:
    st.sidebar.info("Dashboard is in Live Mode. Interact to see updates.")