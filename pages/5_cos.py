import streamlit as st
from streamlit_echarts import st_echarts

causes = [
    "Meningitis", "Dementia", "Parkinson's disease", "Nutritional deficiencies", "Malaria",
    "Drowning", "Homicide", "Maternal disorders", "HIV/AIDS", "Drug use disorders",
    "Tuberculosis", "Cardiovascular diseases", "Lower respiratory infections", "Neonatal disorders",
    "Alcohol use disorders", "Suicide", "Natural disasters", "Diarrheal diseases",
    "Heat (hot and cold exposure)", "Cancers", "Conflict and terrorism", "Diabetes",
    "Kidney diseases", "Poisonings", "Road injuries", "Chronic respiratory diseases",
    "Digestive diseases", "Fire", "Acute hepatitis", "Measles", "COVID-19"
]

raw_data = "213,962 1,952,677 388,194 222,274 748,131 274,230 397,410 191,152 718,079 137,278 1,162,796 19,414,854 2,183,001 1,831,535 158,469 746,379 9,427 1,165,398 36,024 9,888,413 96,489 1,656,635 1,527,639 56,209 1,195,697 4,414,182 2,516,332 117,406 71,846 56,049 7,887,554"
numbers = [int(x.replace(',', '')) for x in raw_data.split()]
total_deaths = sum(numbers)
percentages = [n / total_deaths for n in numbers]

for i in range(0, len(causes), 4):
    cols = st.columns(4)  # tworzymy 4 kolumny
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(causes):
            cause = causes[idx]
            pct = percentages[idx]
            option = {
                "title": {"text": cause, "left": "center"},
                "series": [{
                    "type": "liquidFill",
                    "data": [pct],
                    "label": {"formatter": f"{pct*100:.2f}%", "fontSize": 20}
                }]
            }
            with col:
                st_echarts(option, height=250)

