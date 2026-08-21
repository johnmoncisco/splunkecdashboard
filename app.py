import streamlit as st
import pandas as pd
import numpy as np
from streamlit_agraph import agraph, Node, Config
from streamlit_autorefresh import st_autorefresh

# Page Config
st.set_page_config(layout="wide", page_title="Splunk Enterprise Dashboard")

# Auto-refresh (5s)
st_autorefresh(interval=5000, key="datarefresh")

# Assets
base_url = "https://raw.githubusercontent.com/johnmoncisco/splunkecdashboard/main/assets/"
svg_icon = base_url + "dc-svg.svg"

# Simulated Data
pue = round(1.24 + np.random.uniform(-0.02, 0.02), 3)

# Header Section
st.title("splunk> enterprise")
st.markdown("### EU EED & EnEfG Compliance Monitoring Dashboard")
st.caption("LIVE STREAMING | App: Environmental_Telemetry_v3 | User: m.vance@nexuscloud.eu")
st.divider()

# --- Top Row: Metadata ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("FACILITY ID", "EED-DE-8839201")
c2.metric("REGULATORY MANDATE", "EED Reg 2024/1364")
c3.metric("TIME RANGE", "Last 365 Days")
c4.metric("DATA INGESTION", "index=dc_telemetry_prod")
st.divider()

# --- Main Dashboard Grid ---
col_left, col_right = st.columns([1, 2])

with col_left:
    st.subheader("Topology")
    st.markdown("<div style='text-align: center;'>Frankfurt DC-04</div>", unsafe_allow_html=True)
    nodes = [Node(id="DC", label="", size=180, shape="image", image=svg_icon)]
    agraph(nodes=nodes, edges=[], config=Config(width=300, height=300, physics=False, backgroundColor="#ffffff"))

with col_right:
    # KPI Grid
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("PUE", f"{pue}", "-0.03")
    k2.metric("WUE", "0.18 L/kWh", "Optimal")
    k3.metric("ERF", "11.4 %", "8,259 MWh")
    k4.metric("RENEWABLE", "100 %", "PPA")
    
    st.subheader("Energy Consumption & Heat Balance (MWH)")
    st.table(pd.DataFrame({
        "Metric": ["Facility Energy Input", "IT Equipment Load", "Cooling Plant Load", "Exported Waste Heat"],
        "MWH (YTD)": [72450.00, 58427.42, 9820.10, 8259.30],
        "Status": ["VALIDATED", "VALIDATED", "ACTIVE", "OFF-TAKING"]
    }))

    st.subheader("EED ICT Capacity & Network Telemetry Summary")
    st.table(pd.DataFrame({
        "Metric Name": ["Active Physical Servers", "Raw Provisioned Storage", "Edge Router Interconnect", "Annual Ingress Volume", "Annual Egress Volume"],
        "Aggregated Value": ["14,280", "184.50", "800.00", "1.12", "1.48"],
        "Unit": ["Units", "PB", "Gbps", "EB", "EB"]
    }))

# --- Bottom Row: Submission Pipeline ---
st.subheader("Automated EU Regulatory Submission Pipeline")
pipeline_df = pd.DataFrame({
    "Target Framework": ["German EnEfG §13 / §17", "EU EED Reg 2024/1364"],
    "Filing Agency": ["BfEE (Federal Energy Office)", "European Commission"],
    "Deadline": ["March 31, 2026", "May 15, 2026"],
    "Export Status": ["EXPORT READY", "EXPORT READY"]
})
st.table(pipeline_df)