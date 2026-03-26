import streamlit as st
import base64

# 1. Configuración inicial
st.set_page_config(page_title="The Warrior Brothers", layout="wide")

# 2. Función para convertir tu logo.png en código que la web entienda
def cargar_logo(archivo):
    try:
        with open(archivo, "rb") as f:
            data = base64.b64encode(f.read()).decode()
            return f'data:image/png;base64,{data}'
    except:
        return None

logo_data = cargar_logo("logo.png")

# 3. Estilos (CSS) - Aquí definimos que el logo vaya al lado del texto
st.markdown("""
    <style>
    .hero-container {
        background-color: #1e1e1e;
        padding: 80px;
        border-radius: 20px;
        text-align: center;
        color: white;
    }
    .flex-header {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-bottom: 20px;
    }
    .logo-img { width: 90px; height: auto; }
    .main-title { font-size: 3.5rem; font-weight: 900; margin: 0; color: white; }
    .btn-wa {
        background-color: #25D366;
        color: white !important;
        padding: 15px 30px;
        text-decoration: none;
        border-radius: 50px;
        font-weight: bold;
        display: inline-block;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Construcción del diseño (HTML)
# Si el logo existe, lo ponemos; si no, solo el texto
logo_html = f'<img src="{logo_data}" class="logo-img">' if logo_data else ""

html_final = f"""
<div class="hero-container">
    <div class="flex-header">
        {logo_html}
        <h1 class="main-title">THE WARRIOR BROTHERS</h1>
    </div>
    <p style="font-size: 1.5rem; color: #ccc;">Maestría en Restauración de Calzado y Cuero</p>
    <p>Artesanía lojana con precisión digital.</p>
    <a href="https://wa.me/593994718745" class="btn-wa">Cotizar mi Trabajo Ahora</a>
</div>
"""

# CRUCIAL: El permiso 'unsafe_allow_html=True' debe ir aquí
st.markdown(html_final, unsafe_allow_html=True)

# 5. Resto de la página (Servicios simples para probar)
st.write("---")
col1, col2, col3 = st.columns(3)
with col1: st.subheader("👞 Suelas")
with col2: st.subheader("🎨 Tinturado")
with col3: st.subheader("👠 Tacos")
