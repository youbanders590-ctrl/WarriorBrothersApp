import streamlit as st
import streamlit.components.v1 as components
import base64

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="👞", layout="wide")

# --- 2. FUNCIÓN PARA EL LOGO ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" class="logo-img">' if logo_base_64 else ""

# --- 3. ESTILOS VISUALES (CSS) ---
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
        font-family: 'Montserrat', sans-serif; font-size: clamp(2.5rem, 8vw, 4.5rem); 
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
    
    .info-box {
        background: #ffffff; padding: 25px; border-radius: 20px;
        border-left: 8px solid #121212; box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        color: #1a1a1a !important; margin-bottom: 20px;
    }
    
    .social-btn {
        display: inline-flex; align-items: center; gap: 8px;
        padding: 10px 20px; border-radius: 10px; text-decoration: none;
        color: white !important; font-weight: bold; margin: 5px; transition: 0.3s;
    }
    .tiktok { background: #000000; border: 1px solid #fe2c55; }
    .facebook { background: #1877F2; }
    .instagram { background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); }
    
    .schedule-list { list-style: none; padding: 0; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SECCIÓN HERO ---
st.markdown(f"""
    <div class="hero-container">
        <div class="flex-header">
            {logo_html}
            <h1 class="main-title">THE WARRIOR BROTHERS</h1>
        </div>
        <p class="sub-title">ESPECIALISTAS EN RESTAURACIÓN DE CALZADO Y CUERO</p>
        <a href="https://wa.me/593994718745" class="whatsapp-btn">Cotizar mi Trabajo Ahora</a>
    </div>
    """, unsafe_allow_html=True)

# --- 5. SECCIÓN SERVICIOS ---
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

# --- 6. SECCIÓN CONTACTO Y UBICACIÓN ---
col_info, col_mapa = st.columns([1, 1.2])

with col_info:
    st.markdown("""
        <div class="info-box">
            <h3>📱 Síguenos en Redes</h3>
            <div style="display: flex; flex-wrap: wrap;">
                <a href="https://www.tiktok.com/@the.warrior.broth" class="social-btn tiktok" target="_blank">🎵 TikTok</a>
                <a href="https://www.facebook.com/TheWarriorBrothersLoja" class="social-btn facebook" target="_blank">👤 Facebook</a>
                <a href="https://www.instagram.com/thewarriorbrothers2023" class="social-btn instagram" target="_blank">📸 Instagram</a>
            </div>
        </div>
        <div class="info-box" style="border-left-color: #FFD700;">
            <h3>📍 Ubicación y Horarios</h3>
            <p><b>Dirección:</b> Lauro Guerrero y José A. Eguiguren, Loja, Ecuador</p>
            <p><b>WhatsApp:</b> 099 471 8745</p>
            <p><b>Horario de atención:</b></p>
            <ul class="schedule-list">
                <li><b>Lun - Vie:</b> 08:00 - 19:00</li>
                <li><b>Sáb:</b> 08:00 - 15:30</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col_mapa:
    st.markdown("<h3 style='color: #1a1a1a; font-family: Montserrat; margin-left: 5px;'>Visítanos en nuestro Taller</h3>", unsafe_allow_html=True)
    
    # MAPA ACTUALIZADO CON TU IFRAME EXACTO
    mapa_html = f"""
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2319.6535553983294!2d-79.20821527422483!3d-3.9967444553015996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91cb491f5912b73b%3A0xa1e733db367e07a6!2sThe%20Warrior%20Brothers!5e1!3m2!1ses!2sec!4v1776383384965!5m2!1ses!2sec" 
        width="100%" 
        height="400" 
        style="border:0; border-radius:20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);" 
        allowfullscreen="" 
        loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade">
    </iframe>
    """
    components.html(mapa_html, height=450)

st.markdown("<br><center style='color: #666;'>© 2026 The Warrior Brothers | Loja, Ecuador 🛡️⚒️</center><br>", unsafe_allow_html=True)
