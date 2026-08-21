import streamlit as st
import pandas as pd
import numpy as np
from streamlit_agraph import agraph, Node, Config
from streamlit_autorefresh import st_autorefresh

# Page Configuration
st.set_page_config(layout="wide", page_title="Live DC Compliance")

# Auto-refresh setup (5000 milliseconds = 5 seconds)
st_autorefresh(interval=5000, key="datarefresh")

# Assets Configuration
base_url = "https://raw.githubusercontent.com/johnmoncisco/splunkecdashboard/main/assets/"
svg_icon = base_url + "dc-svg.svg"

# Simulate Live Telemetry
pue = round(1.24 + np.random.uniform(-0.02, 0.02), 3)
it_load = round(58427.42 + np.random.uniform(-50, 50), 2)

# Header Section
st.title("splunk> enterprise")
st.subheader("EU EED & EnEfG Compliance Monitoring Dashboard")
st.divider()

# --- Topology Section ---
st.markdown("### Facility Overview")
with st.container():
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 10px;">
            <h2 style="color: #2c3e50; margin: 0;">Frankfurt DC-04</h2>
        </div>
    """, unsafe_allow_html=True)
    nodes = [Node(id="DC", label="", size=200, shape="image", image=svg_icon)]
    agraph(nodes=nodes, edges=[], config=Config(width=800, height=300, physics=False, backgroundColor="#ffffff"))

st.divider()

# --- Live Metrics ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("PUE", f"{pue}", f"{round(pue-1.24, 3)}")
m2.metric("WUE", "0.18 L/kWh", "Stable")
m3.metric("ERF", "11.4 %", "Steady")
m4.metric("IT Load (MWh)", f"{it_load:,.2f}", "Fluctuating")

# --- Tables ---
col_left, col_right = st.columns(2)
with col_left:
    st.table(pd.DataFrame({"Source": ["Facility Input", "IT Load"], "MWh": [72450.00, it_load]}))
with col_right:
    st.table(pd.DataFrame({"Metric": ["Active Servers", "Storage"], "Value": ["14,280", "184.50 PB"]}))