import streamlit as st
import streamlit.components.v1 as components
import base64

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="The Warrior Brothers | Expertos", page_icon="🛡️", layout="wide")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" style="width:120px;">' if logo_base_64 else ""

# --- 2. DISEÑO CSS AVANZADO ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Open+Sans:wght@400;600&display=swap');
    
    .stApp {{ background-color: #ffffff; }}
    
    /* Header / Hero */
    .hero-section {{
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('https://images.unsplash.com/photo-1590054743267-333d45546960?q=80&w=2070&auto=format&fit=crop');
        background-size: cover; background-position: center;
        padding: 100px 20px; text-align: center; color: white;
        border-radius: 0 0 40px 40px; margin-bottom: 50px;
    }}
    
    .main-title {{ font-family: 'Montserrat', sans-serif; font-size: 4rem; font-weight: 900; margin: 20px 0; }}
    .sub-title {{ font-family: 'Open Sans', sans-serif; font-size: 1.2rem; color: #FFD700; letter-spacing: 3px; }}

    /* Cards de Servicios Mejoradas */
    .card-container {{
        background: #f8f9fa; border-radius: 20px; padding: 40px 20px; margin: 20px 0;
    }}
    
    .service-card {{
        background: white; border-radius: 15px; padding: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eee;
        transition: 0.4s; height: 100%;
    }}
    .service-card:hover {{
        transform: translateY(-10px); border-color: #FFD700;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1);
    }}
    
    .service-icon {{ font-size: 2.5rem; margin-bottom: 15px; display: block; }}
    .service-card h3 {{ font-family: 'Montserrat', sans-serif; color: #1a1a1a; margin-bottom: 15px; }}
    .service-card p {{ color: #666; line-height: 1.6; font-size: 0.95rem; }}

    /* Botón WhatsApp Flotante o Destacado */
    .btn-cta {{
        background: #25D366; color: white !important; padding: 20px 50px;
        border-radius: 50px; font-weight: 700; text-decoration: none;
        font-size: 1.2rem; display: inline-block; transition: 0.3s;
        box-shadow: 0 10px 20px rgba(37,211,102,0.3);
    }}
    .btn-cta:hover {{ transform: scale(1.05); background: #128C7E; }}

    /* Footer / Info */
    .footer-box {{
        background: #1a1a1a; color: white; padding: 40px; border-radius: 20px;
    }}
    .social-link {{
        color: white !important; text-decoration: none; margin-right: 20px;
        font-weight: 600; border-bottom: 2px solid #FFD700; padding-bottom: 5px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SECCIÓN HERO ---
st.markdown(f"""
    <div class="hero-section">
        {logo_html}
        <h1 class="main-title">THE WARRIOR BROTHERS</h1>
        <p class="sub-title">MAESTROS ARTESANOS EN CALZADO</p>
        <br>
        <a href="https://wa.me/593994718745" class="btn-cta">📱 COTIZAR POR WHATSAPP</a>
    </div>
    """, unsafe_allow_html=True)

# --- 4. SECCIÓN SERVICIOS (ORGANIZACIÓN) ---
st.markdown("<h2 style='text-align:center; font-family:Montserrat;'>Nuestras Especialidades</h2>", unsafe_allow_html=True)

st.markdown('<div class="card-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class="service-card">
        <span class="service-icon">👞</span>
        <h3>Restauración de Suelas</h3>
        <p>Especialistas en cambio de suelas de montaña (Vibram), cuero y unidades de goma para un agarre perfecto.</p>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="service-card">
        <span class="service-icon">🎨</span>
        <h3>Recolor y Tinturado</h3>
        <p>Devolvemos la vida a tus zapatos con tintes europeos de máxima calidad. Cambio de color y retoque de desgaste.</p>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""<div class="service-card">
        <span class="service-icon">🎒</span>
        <h3>Marroquinería</h3>
        <p>Reparación integral de bolsos, chaquetas y accesorios de cuero. Costuras reforzadas y cambio de cierres.</p>
    </div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. VISIBILIDAD DE CONTACTO Y MAPA ---
st.write("<br>", unsafe_allow_html=True)
col_left, col_right = st.columns([1, 1.3])

with col_left:
    st.markdown(f"""
        <div class="footer-box">
            <h2 style="color:#FFD700;">Visítanos</h2>
            <p style="font-size:1.1rem;">📍 <b>Dirección:</b><br>Lauro Guerrero y José A. Eguiguren, Loja, Ecuador</p>
            <p><b>⏰ Horarios:</b><br>Lun - Vie: 08:00 - 19:00<br>Sáb: 08:00 - 15:30</p>
            <br>
            <h3 style="color:#FFD700;">Síguenos</h3>
            <div style="margin-top:20px;">
                <a href="https://www.facebook.com/TheWarriorBrothersLoja" class="social-link">Facebook</a>
                <a href="https://www.instagram.com/thewarriorbrothers2023" class="social-link">Instagram</a>
                <a href="https://www.tiktok.com/@the.warrior.broth" class="social-link">TikTok</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    mapa_html = f"""
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2319.6535553983294!2d-79.20821527422483!3d-3.9967444553015996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91cb491f5912b73b%3A0xa1e733db367e07a6!2sThe%20Warrior%20Brothers!5e1!3m2!1ses!2sec!4v1776383384965!5m2!1ses!2sec" 
        width="100%" height="450" style="border:0; border-radius:20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);" 
        allowfullscreen="" loading="lazy">
    </iframe>
    """
    components.html(mapa_html, height=480)

st.markdown("<br><center style='color:#888;'>© 2026 The Warrior Brothers - Loja | Pasión por el detalle 🛡️⚒️</center><br>", unsafe_allow_html=True)
