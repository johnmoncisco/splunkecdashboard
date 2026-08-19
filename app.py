import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, Node, Config

# Page Configuration
st.set_page_config(layout="wide", page_title="Data Center Compliance Dashboard")

# Assets Configuration
base_url = "https://raw.githubusercontent.com/johnmoncisco/splunkecdashboard/main/assets/"
svg_icon = base_url + "dc-svg.svg"

# Header Section
st.title("splunk> enterprise")
st.subheader("EU EED & EnEfG Compliance Monitoring Dashboard")
st.divider()

# --- Centered Facility Header & Graph ---
st.markdown("### Facility Overview")

# Use a container to group the label and image together
with st.container():
    # Centered Label with enough top margin to prevent overlap
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 10px;">
            <h2 style="color: #2c3e50; margin: 0;">Frankfurt DC-04</h2>
        </div>
    """, unsafe_allow_html=True)

    # Node configuration - label is empty because we added it via HTML above
    nodes = [
        Node(id="DC", label="", size=200, shape="image", image=svg_icon)
    ]

    # Configure graph with enough height to prevent clipping
    config = Config(
        width=800, 
        height=300, 
        directed=False, 
        physics=False, 
        backgroundColor="#ffffff"
    )

    # Render graph
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