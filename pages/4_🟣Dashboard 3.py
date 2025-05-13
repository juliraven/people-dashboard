import streamlit as st

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
