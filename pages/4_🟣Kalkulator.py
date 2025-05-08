import streamlit as st

page_bg_img_sidebar = """
<style>
[data-testid="stSidebar"] {
    background: radial-gradient(circle at 51% 50%, #202125, #2d035e, #b444fb); 
    background-blend-mode: multiply;
    background-size: cover;
    overflow: hidden; 
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

st.title("🍏 Kalkulator BMI i zapotrzebowania energetycznego")

gender = st.selectbox("Płeć", ["Mężczyzna", "Kobieta"])
age = st.number_input("Wiek", min_value=10, max_value=100, value=25)
height = st.number_input("Wzrost (m)", min_value=1.0, max_value=2.5, value=1.75)
weight = st.number_input("Waga (kg)", min_value=30, max_value=300, value=70)

activity_options = {
    "Siedzący tryb życia. Brak regularnej aktywności fizycznej, typowe dzienne zajęcia niewymagające dużego wysiłku, jak np.: mycie naczyń, robienie zakupów, praca biurowa, jazda samochodem.": 1.4,
    "Niska aktywność fizyczna. Do aktywności typowej dla siedzącego trybu życia dochodzi 30-60 minut umiarkowanego wysiłku fizycznego, jak np. spokojna jazda rowerem, spacer (5-6 km/h).": 1.5,
    "Umiarkowana aktywność fizyczna. Co najmniej godzinny wysiłek o średnim stopniu nasilenia kilka razy w tygodniu.": 1.7,
    "Umiarkowana aktywność fizyczna. Co najmniej godzinny wysiłek o średnim stopniu nasilenia każdego dnia lub wykonywanie pracy fizycznej.": 1.9,
    "Aktywny tryb życia. Minimum 60-minutowy wysiłek o średnim stopniu nasilenia każdego dnia i co najmniej godzina energicznej aktywności fizycznej, jak np. jogging, pływanie, wspinaczka górska, gra w tenisa ziemnego czy szybki marsz (8 km/h).": 2.0,
    "Ekstremalnie wysoka aktywność fizyczna, np. wyczynowe uprawianie sportu.": 2.2
}

activity_label = st.selectbox("Poziom aktywności", list(activity_options.keys()))
activity_level = activity_options[activity_label] 

bmi = weight/height**2

if gender=='Kobieta':
    ppm = 655.1 + (9.563*weight) + (1.85*height*100) - (4.676*age)
    cpm = ppm * activity_level
else:
    ppm = 66.5 + (13.75*weight) + (5.003*height*100) - (6.775*age)
    cpm = ppm * activity_level

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif 18.5 <= bmi < 25:
        return "waga prawidłowa"
    elif 25 <= bmi < 30:
        return "nadwaga"
    elif 30 <= bmi < 35:
        return "I stopień otyłości"
    elif 35 <= bmi < 40:
        return "II stopień otyłości"
    else:
        return "III stopień otyłości"

category = get_bmi_category(bmi)

st.markdown(f"### **{category} (BMI {bmi:.2f})**")

category_positions = {
    "niedowaga": 8,
    "waga prawidłowa": 25,
    "nadwaga": 42,
    "I stopień otyłości": 58,
    "II stopień otyłości": 75,
    "III stopień otyłości": 92
}


position_percent = category_positions[category]

st.markdown(f"""
<style>
.bmi-wrapper {{
    position: relative;
    width: 100%;
    margin-bottom: 40px;
}}

.bmi-arrow {{
    position: absolute;
    top: -20px;
    left: {position_percent}%;
    transform: translateX(-50%);
    font-size: 24px;
    color: #000;
}}

.bmi-bar {{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    height: 20px;
    border-radius: 5px;
    overflow: hidden;
}}

.bmi-labels {{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    font-size: 12px;
    margin-top: 5px;
    text-align: center;
}}
</style>

<div class="bmi-wrapper">
    <div class="bmi-arrow">▼</div>
    <div class="bmi-bar">
        <div style="background-color:#00cfe8;"></div>
        <div style="background-color:#00e676;"></div>
        <div style="background-color:#c6ff00;"></div>
        <div style="background-color:#ffca28;"></div>
        <div style="background-color:#ffa000;"></div>
        <div style="background-color:#f44336;"></div>
    </div>
    <div class="bmi-labels">
        <div>niedowaga</div>
        <div>waga<br>prawidłowa</div>
        <div>nadwaga</div>
        <div>otyłość I</div>
        <div>otyłość II</div>
        <div>otyłość III</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.bmi-box {
    background-color: #f7f7f7;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 0px 8px rgba(0,0,0,0.05);
    font-weight: bold;
    color: #333333;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="bmi-box">BMI<br><span style="font-size: 24px;">{bmi:.2f}</span></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="bmi-box">PPM<br><span style="font-size: 24px;">{ppm:.0f} kcal</span></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="bmi-box">CPM<br><span style="font-size: 24px;">{cpm:.0f} kcal</span></div>', unsafe_allow_html=True)
