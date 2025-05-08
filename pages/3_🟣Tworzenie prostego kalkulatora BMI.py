import streamlit as st
from streamlit_extras.app_logo import add_logo

add_logo('logo.png', height=350)

st.sidebar.markdown(
    """
    <style>
        }
        [data-testid="stSidebar"] {
            padding-top: 0px;
            padding: 10px;
            font-family: sans-serif;
            font-size: 18px;
            width: 150px !important; /* Wymuszenie */
            min-width: 150px !important;
            max-width: 150px !important;
        }

        [data-testid="stSidebarHeader"] {
            height: 30px;
            padding: 5px 10px; 
            margin: 0; 
            display: flex; 
            align-items: center;
            justify-content: center; 
        }
        .main {
            margin-left: 170px;
    </style>
    """,
    unsafe_allow_html=True,
)

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

st.title("Tworzenie prostego kalkulatora BMI")

st.markdown(
    '''
    <p>
    W celu utworzenia prostego interaktywnego kalkulatora BMI, należy zdefiniować opcje, jakie będzie miał do wyboru użytkownik. W przypadku kalkulatora BMI będą to:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
activity_options = {
    "Siedzący tryb życia. Brak regularnej aktywności fizycznej, typowe dzienne zajęcia niewymagające dużego wysiłku, jak np.: mycie naczyń, robienie zakupów, praca biurowa, jazda samochodem.": 1.4,
    "Niska aktywność fizyczna. Do aktywności typowej dla siedzącego trybu życia dochodzi 30-60 minut umiarkowanego wysiłku fizycznego, jak np. spokojna jazda rowerem, spacer (5-6 km/h).": 1.5,
    "Umiarkowana aktywność fizyczna. Co najmniej godzinny wysiłek o średnim stopniu nasilenia kilka razy w tygodniu.": 1.7,
    "Umiarkowana aktywność fizyczna. Co najmniej godzinny wysiłek o średnim stopniu nasilenia każdego dnia lub wykonywanie pracy fizycznej.": 1.9,
    "Aktywny tryb życia. Minimum 60-minutowy wysiłek o średnim stopniu nasilenia każdego dnia i co najmniej godzina energicznej aktywności fizycznej, jak np. jogging, pływanie, wspinaczka górska, gra w tenisa ziemnego czy szybki marsz (8 km/h).": 2.0,
    "Ekstremalnie wysoka aktywność fizyczna, np. wyczynowe uprawianie sportu.": 2.2
}

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    gender = st.selectbox("Płeć", ["Mężczyzna", "Kobieta"])

with col2:
    age = st.number_input("Wiek", min_value=10, max_value=100, value=25)

with col3:
    height = st.number_input("Wzrost (m)", min_value=1.0, max_value=2.5, value=1.75)

with col4:
    weight = st.number_input("Waga (kg)", min_value=30, max_value=300, value=70)

with col5:
    activity_label = st.selectbox("Poziom aktywności", list(activity_options.keys()))
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Używając opcji <code>st.columns()</code> tworzymy układ siatki. Dzięki temu wszystkie dostępne dla użytkownika opcje będą wyświetlały się w jednym wierszu.  
    </p>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <p>
    W dalszej części wystyarczy umieścić niezbędne funkcje obliczające np. wartości BMI, PPM, CPM dla wybranych przez użytkownika opcji, a następnie wyświetlić oblicozne wartości za pomocą funkcji <code>st.write()</code>.
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
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
st.markdown(f"### **{ppm} (PPM {ppm:.0f}) kcal**")
st.markdown(f"### **{cpm} (CPM {cpm:.0f}) kcal**")

'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Utworzony w ten sposób i ulepszony wizualnie kalkulator znajduje się w zakładce 🟣Kalkulator.
    </p>
    ''',
    unsafe_allow_html=True
)

st.page_link("pages/4_🟣Kalkulator.py", label="➡️ Przejdź do zakładki:  **Kalkulator**")
