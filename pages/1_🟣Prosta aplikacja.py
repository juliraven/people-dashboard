import streamlit as st

page_bg_img_sidebar = """
<style>
[data-testid="stSidebar"] {
    background: radial-gradient(circle at 51% 40%, #b444fb, #2d035e, #202125); 
    background-blend-mode: multiply;
    background-size: cover;
    overflow: hidden; /* Prevent scrolling */
}

header[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

body {
    background-color: #202125; 
}

</style>
"""

st.markdown(page_bg_img_sidebar, unsafe_allow_html=True)


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 UX Performance Dashboard (Last 7 Days)")

# Symulacja danych
np.random.seed(42)
x = np.linspace(0.5, 20, 100)
page_load = np.exp(-x / 4) * 60000
bounce_rate = 30 + 30 * (1 - np.exp(-x / 5))

# Wykres 1: Load Time vs Bounce Rate
st.subheader("Load Time vs Bounce Rate")
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.bar(x, page_load, color=color, label="Page Load (LUX)")
ax1.set_ylabel('Page Load (LUX)', color=color)
ax2 = ax1.twinx()
color = 'tab:pink'
ax2.plot(x, bounce_rate, color=color, label="Bounce Rate (%)")
ax2.set_ylabel('Bounce Rate (%)', color=color)
fig.tight_layout()
st.pyplot(fig)

# Dane zagregowane
col1, col2, col3, col4 = st.columns(4)
col1.metric("Page Load", "0.7s")
col2.metric("Page Views", "2.7M", delta="-5%")
col3.metric("Bounce Rate", "40.6%", delta="+1.2%")
col4.metric("Sessions", "479K")

# Wykres 2: Session Length vs PVs per Session
st.subheader("Sessions Overview")
session_length = np.random.normal(17, 2, 100)
pvs_per_session = np.random.uniform(1, 5, 100)
fig2, ax = plt.subplots()
ax.plot(session_length, label="Session Length (min)", color='lime')
ax.plot(pvs_per_session, label="PVs per Session", color='cyan')
ax.legend()
st.pyplot(fig2)
