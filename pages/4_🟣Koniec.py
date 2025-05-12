import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

page_bg_img_sidebar = """
<style>
/* Ustawienie szerokości sidebaru */
section[data-testid="stSidebar"] {
    width: 240px !important;
    min-width: 240px !important;
    max-width: 240px !important;
    display: flex;
    align-items: center;       /* Wyśrodkowanie w pionie */
    justify-content: center;   /* Wyśrodkowanie w poziomie */
    flex-direction: column;
    height: 100vh;             /* Wysokość całego widoku */
    padding-top: 10px;
}

/* Styl samego wnętrza sidebaru */
[data-testid="stSidebar"] {
    background: linear-gradient(
        135deg,
        rgba(32, 33, 37, 0.6),
        rgba(45, 3, 94, 0.5),
        rgba(180, 68, 251, 0.4)
    );
    border: 1px solid rgba(180, 68, 251, 0.3);
    border-radius: 0px;
    padding: 24px;
    width: 100%;
    box-shadow:
        0 0 10px rgba(180, 68, 251, 0.25),
        0 4px 16px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12px) brightness(1.05);
    background-blend-mode: overlay;
    transition: none;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;  /* Wyśrodkowanie zawartości */
}

/* Główna treść */
section.main > div {
    padding-left: 220px !important;
}

/* Nagłówek przezroczysty */
header[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

/* Tło strony */
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
