import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, Node, Edge, Config

# Page Configuration
st.set_page_config(layout="wide", page_title="Data Center Compliance Dashboard")

# Assets Configuration
base_url = "https://raw.githubusercontent.com/johnmoncisco/splunkecdashboard/main/assets/"
svg_icon = base_url + "dc-svg.svg"

# Header Section
st.title("splunk> enterprise")
st.subheader("EU EED & EnEfG Compliance Monitoring Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.write("**Time Range:** Last 365 Days")
col2.write("**Facility:** EED-DE-8839201")
col3.write("**Mandate:** EED Reg 2024/1364")
col4.write("**Status:** EXPORT READY")

st.divider()

# --- Topology Section with Custom SVG ---
st.markdown("### Data Center Topology View")

nodes = [
    Node(id="DC", label="Frankfurt DC-04", size=50, shape="image", image=svg_icon),
    Node(id="SRV", label="Compute Node", size=40, shape="image", image=svg_icon),
    Node(id="NET", label="Network Edge", size=40, shape="image", image=svg_icon)
]

edges = [
    Edge(source="DC", target="SRV", label="Compute Path"),
    Edge(source="SRV", target="NET", label="Uplink")
]

config = Config(
    width=800, 
    height=400, 
    directed=True, 
    physics=True, 
    backgroundColor="#ffffff",
    nodeHighlightBehavior=True
)

clicked_node = agraph(nodes=nodes, edges=edges, config=config)

if clicked_node:
    st.info(f"Selected Asset: {clicked_node}")

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
    st.table(pd.DataFrame({
        "Source": ["Facility Input", "IT Load", "Cooling", "Lighting"],
        "MWh": [72450.00, 58427.42, 9820.10, 4202.48]
    }))

with col_right:
    st.markdown("#### Telemetry Summary")
    st.table(pd.DataFrame({
        "Metric": ["Active Servers", "Storage", "Ingress", "Egress"],
        "Value": ["14,280 Units", "184.50 PB", "1.12 EB", "1.48 EB"]
    }))