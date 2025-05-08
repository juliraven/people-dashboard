import streamlit as st

st.set_page_config(page_title="Moja Strona", page_icon=":guardsman:", layout="wide", initial_sidebar_state="collapsed")

# Treść strony
st.title("Strona bez Sidebaru")
st.write("Ten tekst jest widoczny, ale sidebar jest ukryty.")


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
    .emoji-top {
        margin-top: -20px; /* Zmniejszenie marginesu górnego */
    }
    </style>
    
    <div style="text-align: center;">
        <h1 class="emoji-top"></h1> 
        <h2></h2>
    </div>
    """, 
    unsafe_allow_html=True
)
