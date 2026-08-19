import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, Node, Config

# Page Configuration
st.set_page_config(layout="wide", page_title="Data Center Compliance Dashboard")

# CSS to ensure the Graph Label is visible (White text)
st.markdown("""
    <style>
    /* Force white text on the graph labels */
    .vis-network div.vis-label {
        color: white !important;
        font-weight: bold;
        text-shadow: 1px 1px 2px black; /* Add shadow to ensure readability on white bg */
    }
    </style>
    """, unsafe_allow_html=True)

# Assets Configuration
base_url = "https://raw.githubusercontent.com/johnmoncisco/splunkecdashboard/main/assets/"
svg_icon = base_url + "dc-svg.svg"

# Header Section
st.title("splunk> enterprise")
st.subheader("EU EED & EnEfG Compliance Monitoring Dashboard")

st.divider()

# --- Single Topology Node (Larger) ---
st.markdown("### Facility Overview")

nodes = [
    Node(id="DC", label="Frankfurt DC-04", size=200, shape="image", image=svg_icon)
]

config = Config(
    width=800, 
    height=400, 
    directed=False, 
    physics=False, 
    backgroundColor="#ffffff"
)

agraph(nodes=nodes, edges=[], config=config)

st.divider()

# --- Metrics Section ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("PUE", "1.24", "-0.03")
m2.metric("WUE", "0.18 L/kWh", "Optimal")
m3.metric("ERF", "11.4 %", "8,259 MWh")
m4.metric("Renewable", "100 %", "PPA")

# --- Tables ---
col_left, col_right = st.columns(2)
with col_left:
    st.markdown("#### Energy Consumption (MWh)")
    st.table(pd.DataFrame({"Source": ["Facility Input", "IT Load"], "MWh": [72450.00, 58427.42]}))
with col_right:
    st.markdown("#### Telemetry Summary")
    st.table(pd.DataFrame({"Metric": ["Active Servers", "Storage"], "Value": ["14,280", "184.50 PB"]}))