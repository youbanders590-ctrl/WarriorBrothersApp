import streamlit as st

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="👞", layout="wide")

# --- ESTILOS ---
st.markdown("""
    <style>
    .stApp { background-color: #fcfdfa; }
    .hero-black {
        background-color: #1e1e1e; 
        color: white; 
        padding: 60px; 
        border-radius: 20px; 
        text-align: center;
    }
    .header-box {
        display: flex; 
        align-items: center; 
        justify-content: center; 
        gap: 20px; 
        margin-bottom: 20px;
    }
    .logo-img { width: 80px; }
    .title-text { font-size: 3.5rem; font-weight: 900; margin: 0; color: white; }
    .whatsapp-btn {
        background-color: #25D366; 
        color: white !important; 
        padding: 15px 30px; 
        text-decoration: none; 
        border-radius: 50px; 
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA (AQUÍ ESTÁ EL TRUCO) ---
# He usado una sola línea para evitar que Streamlit se confunda
cabecera_html = f"""
<div class="hero-black">
    <div class="header-box">
        <img src="https://raw.githubusercontent.com/TheWarriorBrothers/Vitrina/main/logo.png" class="logo-img">
        <h1 class="title-text">THE WARRIOR BROTHERS</h1>
    </div>
    <p style="font-size: 1.5rem; color: #ccc;">Maestría en Restauración de Calzado y Cuero</p>
    <p>Artesanía lojana con precisión digital.</p>
    <br><br>
    <a href="https://wa.me/593994718745" class="whatsapp-btn">Cotizar mi Trabajo Ahora</a>
</div>
"""

st.markdown(cabecera_html, unsafe_allow_html=True)

# --- SERVICIOS ---
st.write("") # Espacio
st.header("🛠️ Nuestros Servicios")
c1, c2, c3 = st.columns(3)
with c1:
    st.info("👞 **Suelas y Pisos**")
with c2:
    st.info("🎨 **Tinturado Pro**")
with c3:
    st.info("👠 **Tacos y Tapas**")
