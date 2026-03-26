import streamlit as st
import streamlit.components.v1 as components
import base64

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="👞", layout="wide")

# --- FUNCIÓN PARA CARGAR LOGO ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" class="logo-img">' if logo_base_64 else ""

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Roboto:wght@300;400;700&display=swap');

    .stApp { background-color: #f8f9fa; }

    .hero-container {
        background: #121212; padding: 60px 20px; border-radius: 30px;
        text-align: center; color: white; box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        border: 1px solid #333; margin-bottom: 40px;
    }

    .flex-header { display: flex; align-items: center; justify-content: center; gap: 20px; flex-wrap: wrap; }
    .logo-img { width: 100px; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1)); }

    .main-title { 
        font-family: 'Montserrat', sans-serif; font-size: clamp(2rem, 8vw, 4.2rem); 
        margin: 0; background: linear-gradient(90deg, #FFFFFF 30%, #FFD700 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; line-height: 1.1;
    }

    .sub-title { font-family: 'Roboto', sans-serif; font-size: 1.3rem; color: #FFD700; margin-top: 10px; }

    .whatsapp-btn {
        background: linear-gradient(45deg, #25D366, #128C7E); color: white !important;
        padding: 15px 35px; text-decoration: none; border-radius: 50px;
        font-family: 'Montserrat', sans-serif; font-weight: 700; display: inline-block;
        margin-top: 25px; transition: 0.3s;
    }

    .service-card {
        background: white; border-radius: 20px; padding: 25px; text-align: center;
        border: 2px solid #e0e0e0; box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        height: 100%; transition: 0.3s; margin-bottom: 20px;
    }
    
    .service-card h3 { color: #1a1a1a !important; font-family: 'Montserrat', sans-serif; font-size: 1.2rem; }
    .service-card p { color: #444444 !important; font-family: 'Roboto', sans-serif; }

    .info-box {
        background: #ffffff; padding: 25px; border-radius: 20px;
        border-left: 8px solid #121212; box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        color: #1a1a1a !important; margin-bottom: 20px;
    }

    .social-btn {
        display: inline-flex; align-items: center; gap: 8px;
        padding: 10px 20px; border-radius: 10px; text-decoration: none;
        color: white !important; font-weight: bold; margin: 5px;
    }
    .tiktok { background: #000000; border: 1px solid #fe2c55; }
    .facebook { background: #1877F2; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. SECCIÓN HERO ---
st.markdown(f"""
    <div class="hero-container">
        <div class="flex-header">
            {logo_html}
            <h1 class="main-title">THE WARRIOR BROTHERS</h1>
        </div>
        <p class="sub-title">MAESTRÍA EN RESTAURACIÓN DE CALZADO Y CUERO</p>
        <a href="https://wa.me/593994718745" class="whatsapp-btn">Cotizar mi Trabajo Ahora</a>
    </div>
    """, unsafe_allow_html=True)

# --- 2. SECCIÓN SERVICIOS ---
st.markdown("<h2 style='text-align: center; color: #1a1a1a; font-family: Montserrat; margin-bottom: 30px;'>Nuestros Servicios</h2>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
servicios = [
    ["👞 Suelas", "Cambio de suelas de alta montaña y ciudad."],
    ["🎨 Tinturado", "Restauración de color con pigmentos europeos."],
    ["👠 Tacos", "Reparación estructural para calzado fino."],
    ["🎒 Cuero", "Costura y restauración de bolsos y chaquetas."]
]
for col, ser in zip([c1, c2, c3, c4], servicios):
    with col:
        st.markdown(f"""<div class="service-card"><h3>{ser[0]}</h3><p>{ser[1]}</p></div>""", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# --- 3. SECCIÓN CONTACTO Y UBICACIÓN ---
col_info, col_mapa = st.columns([1, 1.2])

with col_info:
    st.markdown("""
        <div class="info-box">
            <h3>📱 Síguenos en Redes</h3>
            <p>Mira nuestras restauraciones paso a paso:</p>
            <a href="https://www.tiktok.com/" class="social-btn tiktok">🎵 TikTok</a>
            <a href="https://www.facebook.com/" class="social-btn facebook">👤 Facebook</a>
        </div>
        <div class="info-box" style="border-left-color: #FFD700;">
            <h3>📍 Ubicación y Horarios</h3>
            <p><b>Dirección:</b> Lauro Guerrero y José A. Eguiguren, Loja, Ecuador</p>
            <p><b>WhatsApp:</b> 099 471 8745</p>
            <p><b>Horario:</b> Lun - Vie (08:00 - 18:00)</p>
        </div>
    """, unsafe_allow_html=True)

with col_mapa:
    st.markdown("<h3 style='color: #1a1a1a; font-family: Montserrat; margin-left: 5px;'>Visítanos en nuestro Taller</h3>", unsafe_allow_html=True)
    
    # Mapa configurado para Lauro Guerrero y José A. Eguiguren
    # El ancho al 100% permite que sea responsivo en móviles.
    mapa_html = """
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15930.5644781603!2d-79.206495!3d-3.996165!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91cb315992955f3f%3A0x6a02b6623788770a!2sLauro%20Guerrero%20%26%20Jos%C3%A9%20Antonio%20Eguiguren%2C%20Loja!5e0!3m2!1ses!2sec!4v1710000000000!5m2!1ses!2sec" 
        width="100%" 
        height="380" 
        style="border:0; border-radius:20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);" 
        allowfullscreen="" 
        loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade">
    </iframe>
    """
    components.html(mapa_html, height=400)

st.markdown("<br><center style='color: #666; font-size: 0.9rem;'>© 2026 The Warrior Brothers | Loja, Ecuador 🛡️⚒️</center><br>", unsafe_allow_html=True)
