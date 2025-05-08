import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

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

st.balloons()

st.markdown(
    """
    <style>
    .container {
        display: flex;
        justify-content: center; /* Wyrównanie poziome */
        align-items: center; /* Wyrównanie pionowe */
        height: 70vh; /* Ustawia wysokość na 100% wysokości okna przeglądarki */
        text-align: center;
    }
    .emoji-top {
        margin-top: -20px; /* Zmniejszenie marginesu górnego */
        font-size: 20px; /* Zmniejszenie czcionki dla h1 */
        color: #ff5733; /* Zmiana koloru czcionki na pomarańczowy */
    }
    .h2-style {
        font-size: 14px; /* Zmniejszenie czcionki dla h2 */
        color: #b444fb !important; /* Zmiana koloru czcionki */
    }
    </style>
    
    <div class="container">
        <div>
            <h1 class="emoji-top">Dziękujemy za uwagę!</h1> 
            <h2 class="h2-style">Weronika Kępińska, Julia Kruk, Zuzanna Sulecka</h2>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)
