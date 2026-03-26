import streamlit as st
import base64

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="👞", layout="wide")

# --- FUNCIÓN LOGO ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" class="logo-img">' if logo_base_64 else ""

# --- ESTILOS CSS (CORREGIDOS PARA VISIBILIDAD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Roboto:wght@300;400;700&display=swap');

    /* Fondo general */
    .stApp { background-color: #f8f9fa; }

    /* Hero Container (Negro) */
    .hero-container {
        background: #121212; padding: 70px 40px; border-radius: 30px;
        text-align: center; color: white; box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        border: 1px solid #333; margin-bottom: 40px;
    }

    .flex-header { display: flex; align-items: center; justify-content: center; gap: 20px; flex-wrap: wrap; }
    .logo-img { width: 100px; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1)); }

    /* Título Amarillo Difuminado */
    .main-title { 
        font-family: 'Montserrat', sans-serif; font-size: 4.2rem; letter-spacing: -2px; 
        margin: 0; background: linear-gradient(90deg, #FFFFFF 30%, #FFD700 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; line-height: 1.1;
    }

    .sub-title { font-family: 'Roboto', sans-serif; font-size: 1.5rem; color: #FFD700; font-weight: 400; margin-top: 10px; }

    /* Botón WhatsApp */
    .whatsapp-btn {
        background: linear-gradient(45deg, #25D366, #128C7E); color: white !important;
        padding: 18px 40px; text-decoration: none; border-radius: 50px;
        font-family: 'Montserrat', sans-serif; font-weight: 700; display: inline-block;
        transition: 0.4s; box-shadow: 0 10px 25px rgba(37, 211, 102, 0.3); margin-top: 25px;
    }
    .whatsapp-btn:hover { transform: translateY(-3px); box-shadow: 0 15px 35px rgba(37, 211, 102, 0.5); }

    /* TARJETAS DE SERVICIO (TEXTO OSCURO PARA VISIBILIDAD) */
    .service-card {
        background: white; border-radius: 20px; padding: 30px 20px; text-align: center;
        border: 2px solid #e0e0e0; box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        height: 100%; transition: 0.3s;
    }
    .service-card:hover { transform: translateY(-5px); border-color: #FFD700; }
    
    .service-card h3 { color: #1a1a1a !important; font-family: 'Montserrat', sans-serif; margin-bottom: 10px; }
    .service-card p { color: #444444 !important; font-family: 'Roboto', sans-serif; font-size: 1rem; }

    /* CAJAS DE INFORMACIÓN (TEXTO OSCURO) */
    .info-box {
        background: #ffffff; padding: 25px; border-radius: 20px;
        border-left: 8px solid #121212; box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        color: #1a1a1a !important;
    }
    .info-box h3 { color: #1a1a1a !important; margin-bottom: 15px; }
    .info-box p { color: #333333 !important; margin: 8px 0; }

    /* Botones Redes */
    .social-btn {
        display: inline-flex; align-items: center; gap: 8px;
        padding: 10px 20px; border-radius: 10px; text-decoration: none;
        color: white !important; font-weight: bold; margin: 5px; transition: 0.3s;
    }
    .tiktok { background: #000000; border: 1px solid #fe2c55; }
    .facebook { background: #1877F2; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. CABECERA ---
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

# --- 2. SERVICIOS ---
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
        st.markdown(f"""
            <div class="service-card">
                <h3>{ser[0]}</h3>
                <p>{ser[1]}</p>
            </div>
        """, unsafe_allow_html=True)

# --- 3. SECCIÓN REDES Y CONTACTO ---
st.write("<br>", unsafe_allow_html=True)
col_redes, col_info = st.columns(2)

with col_redes:
    st.markdown("""
        <div class="info-box">
            <h3>📱 Síguenos en Redes</h3>
            <p>Mira nuestras restauraciones en video:</p>
            <a href="https://www.tiktok.com/" class="social-btn tiktok">🎵 TikTok</a>
            <a href="https://www.facebook.com/" class="social-btn facebook">👤 Facebook</a>
        </div>
    """, unsafe_allow_html=True)

with col_info:
    st.markdown("""
        <div class="info-box" style="border-left-color: #FFD700;">
            <h3>📍 Información de Contacto</h3>
            <p><b>Dirección:</b> Centro de la ciudad, Loja, Ecuador</p>
            <p><b>WhatsApp:</b> 099 471 8745</p>
            <p><b>Horario:</b> Lun - Vie (08:00 - 18:00)</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><center style='color: #666;'>© 2026 The Warrior Brothers | Loja, Ecuador 🛡️⚒️</center>", unsafe_allow_html=True)
