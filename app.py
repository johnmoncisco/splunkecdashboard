import streamlit as st
import pandas as pd

# Page config
st.set_page_config(layout="wide", page_title="EU EED Compliance Dashboard")

# CSS to match the dashboard aesthetic
st.markdown("""
    <style>
    .metric-card { background-color: #f0f2f6; padding: 20px; border-radius: 10px; }
    .header-info { font-size: 14px; color: #555; }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.title("splunk> enterprise")
st.subheader("EU EED & EnEfG Compliance Monitoring Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.write("**Time Range:** Last 365 Days")
col2.write("**Facility:** EED-DE-8839201")
col3.write("**Mandate:** EED Reg 2024/1364 + EnEfG")
col4.write("**Index:** index=dc_telemetry_prod")

st.divider()

# Key Performance Indicators
st.markdown("### Key Metrics")
m1, m2, m3, m4 = st.columns(4)
m1.metric("PUE", "1.24", "-0.03 vs 2024")
m2.metric("WUE", "0.18 L/kWh", "Optimal")
m3.metric("ERF", "11.4 %", "8,259.3 MWh")
m4.metric("Renewable Share", "100 %", "PPA + GO")

# Tables Section
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("#### Energy Consumption & Heat Balance (MWh)")
    energy_data = {
        "Source": ["Facility Energy Input", "IT Equipment Load", "Cooling Plant", "Aux & Lighting", "Waste Heat"],
        "MWh (YTD)": [72450.00, 58427.42, 9820.10, 4202.48, 8259.30],
        "Status": ["Validated", "Validated", "Active", "Active", "Off-taking"]
    }
    st.table(pd.DataFrame(energy_data))

with col_right:
    st.markdown("#### ICT Capacity & Network Telemetry")
    net_data = {
        "Metric": ["Active Physical Servers", "Raw Provisioned Storage", "Edge Router", "Ingress Vol", "Egress Vol"],
        "Value": ["14,280", "184.50 PB", "800.00 Gbps", "1.12 EB", "1.48 EB"]
    }
    st.table(pd.DataFrame(net_data))

# Regulatory Section
st.markdown("### Automated EU Regulatory Submission Pipeline")
reg_data = [
    {"Framework": "German EnEfG", "Agency": "BfEE", "Deadline": "March 31, 2026", "Status": "EXPORT READY"},
    {"Framework": "EU EED Reg", "Agency": "European Commission", "Deadline": "May 15, 2026", "Status": "EXPORT READY"}
]
st.dataframe(pd.DataFrame(reg_data), use_container_width=True)

# Footer for deployment
st.caption("Live Simulation: Integrated via Splunk Enterprise Telemetry")