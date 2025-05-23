import pandas as pd
import plotly.graph_objects as go
import streamlit as st

df1 = pd.read_csv('life-expectancy-at-different-ages.csv')

countries = list(df1["Entity"].unique())
default_country = "World" if "World" in countries else countries[0]
selected_country = st.selectbox("Wybierz kraj lub region", countries, index=countries.index(default_country))

df_country = df1[df1["Entity"] == selected_country].sort_values("Year").dropna()
df_country["Year"] = df_country["Year"].astype(int)

age_columns = {
    "przy urodzeniu": "Period life expectancy at birth - 0",
    "10 lat": "Period life expectancy - 10",
    "25 lat": "Period life expectancy - 25",
    "45 lat": "Period life expectancy - 45",
    "65 lat": "Period life expectancy - 65",
    "80 lat": "Period life expectancy - 80",
}

violet_colors = [
    "#a6cee3",
    "#1f78b4",
    "#6baed6",
    "#3182bd",
    "#08519c",
    "#08306b",
]

fig = go.Figure()

# Dodaj linie na pełny zakres lat od razu (bez animacji)
for i, (age_label, col_name) in enumerate(age_columns.items()):
    fig.add_trace(go.Scatter(
        x=df_country["Year"],
        y=df_country[col_name],
        mode="lines",
        name=age_label,
        line=dict(color=violet_colors[i])
    ))

fig.update_layout(
    xaxis_title="Rok",
    yaxis_title="Oczekiwana długość życia",
    xaxis=dict(
        tickmode="linear",  # liniowe ticki
        dtick=5,            # co 5 lat etykieta
        tickangle=0,        # kąt etykiet, zmień na 45 jeśli chcesz pochylić
        showgrid=True,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    )
)

st.markdown(f"<h3 style='text-align: center; color: black;'>Długość życia osób w różnym wieku</h3>", unsafe_allow_html=True)
st.plotly_chart(fig, config={"displayModeBar": False})
