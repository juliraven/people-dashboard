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
import plotly.graph_objs as go

st.title("📊 UX Performance Dashboard")

# Sidebar z kontrolkami
st.sidebar.header("🔧 Ustawienia analizy")
metric_option = st.sidebar.selectbox(
    "Wybierz metrykę do analizy:",
    ("Page Load vs Bounce Rate", "Session Length vs PVs per Session")
)

date_range = st.sidebar.slider(
    "Zakres dni:",
    min_value=7, max_value=60, value=30, step=1
)

# Generowanie danych
np.random.seed(42)
x = np.linspace(0.5, 20, date_range)
page_load = np.exp(-x / 4) * 60000
bounce_rate = 30 + 30 * (1 - np.exp(-x / 5))
session_length = np.random.normal(17, 2, date_range)
pvs_per_session = np.random.uniform(1, 5, date_range)
time_series = pd.date_range(end=pd.Timestamp.today(), periods=date_range)

# Wyświetlenie wybranej metryki
if metric_option == "Page Load vs Bounce Rate":
    st.subheader("📉 Page Load vs Bounce Rate")

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=x, y=page_load, name='Page Load (LUX)', marker_color='rgb(55, 83, 109)', yaxis='y1'))
    fig1.add_trace(go.Scatter(x=x, y=bounce_rate, name='Bounce Rate (%)', line=dict(color='rgb(255,105,180)', width=2), yaxis='y2'))

    fig1.update_layout(
        xaxis=dict(title='Czas ładowania (s)'),
        yaxis=dict(title='Page Load (LUX)', side='left'),
        yaxis2=dict(title='Bounce Rate (%)', overlaying='y', side='right'),
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=40, r=40, t=40, b=40),
        height=400
    )
    st.plotly_chart(fig1, use_container_width=True)

elif metric_option == "Session Length vs PVs per Session":
    st.subheader("📈 Session Length vs PVs per Session")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=time_series, y=session_length, mode='lines', name='Session Length (min)', line=dict(color='lime')))
    fig2.add_trace(go.Scatter(x=time_series, y=pvs_per_session, mode='lines', name='PVs per Session', line=dict(color='cyan')))

    fig2.update_layout(
        xaxis_title='Data',
        yaxis_title='Wartość',
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=40, r=40, t=40, b=40),
        height=400
    )
    st.plotly_chart(fig2, use_container_width=True)

# Ogólne metryki (zawsze widoczne)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Page Load", "0.7s")
col2.metric("Page Views", "2.7M", delta="-5%")
col3.metric("Bounce Rate", "40.6%", delta="+1.2%")
col4.metric("Sessions", "479K")
