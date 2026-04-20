import streamlit as st
import streamlit.components.v1 as components
import base64

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="The Warrior Brothers - Expertos en Calzado", page_icon="👞", layout="wide")

# --- 2. FUNCIÓN PARA EL LOGO ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" class="logo-img">' if logo_base_64 else ""

# --- 3. ESTILOS VISUALES (CSS MEJORADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Roboto:wght@300;400&display=swap');
    
    .stApp { background-color: #fdfdfd; }
    
    /* Hero Section Elegante */
    .hero-container {
        background: #1a1a1a; padding: 80px 20px; border-radius: 0 0 50px 50px;
        text-align: center; color: white; box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        margin-top: -60px; margin-bottom: 50px;
    }
    .main-title { 
        font-family: 'Montserrat', sans-serif; font-size: clamp(2rem, 7vw, 4rem); 
        font-weight: 900; letter-spacing: -1px; margin-bottom: 10px;
    }
    .sub-title { color: #FFD700; font-weight: 400; letter-spacing: 2px; font-size: 1.1rem; }

    /* Contenedor de Servicios Tipo Grid */
    .service-section-title {
        text-align: center; font-family: 'Montserrat', sans-serif;
        font-weight: 700; color: #1a1a1a; margin: 40px 0 20px 0;
        text-transform: uppercase; border-bottom: 2px solid #FFD700; display: inline-block;
    }

    .service-card {
        background: white; border-radius: 15px; padding: 30px;
        text-align: left; border: 1px solid #eee; height: 100%;
        transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(0,0,0,0.02);
    }
    .service-card:hover {
        transform: translateY(-5px); border-color: #FFD700;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    .service-card h3 { color: #111; font-size: 1.4rem; margin-bottom: 10px; }
    .service-card p { color: #555; font-size: 0.95rem; line-height: 1.5; }
    .price-tag { color: #FFD700; font-weight: 700; font-size: 1.1rem; display: block; margin-top: 15px; }

    /* Botones */
    .whatsapp-btn {
        background: #25D366; color: white !important; padding: 18px 40px;
        text-decoration: none; border-radius: 8px; font-weight: 700;
        display: inline-block; margin-top: 30px; transition: 0.3s;
    }
    
    .social-btn {
        padding: 10px 15px; border-radius: 5px; color: white !important;
        text-decoration: none; margin-right: 10px; font-size: 0.9rem; font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. HERO ---
st.markdown(f"""
    <div class="hero-container">
        <h1 class="main-title">THE WARRIOR BROTHERS</h1>
        <p class="sub-title">RESTAURACIÓN PROFESIONAL DE CALZADO DE LUJO Y MONTAÑA</p>
        <a href="https://wa.me/593994718745" class="whatsapp-btn">SOLICITAR COTIZACIÓN</a>
    </div>
    """, unsafe_allow_html=True)

# --- 5. CATEGORÍAS DE SERVICIOS ---
def render_service(titulo, descripcion, precio="Consultar"):
    return f"""
    <div class="service-card">
        <h3>{titulo}</h3>
        <p>{descripcion}</p>
        <span class="price-tag">{precio}</span>
    </div>
    """

st.markdown("<center><h2 class='service-section-title'>Nuestros Servicios Especializados</h2></center>", unsafe_allow_html=True)

# Fila 1: Suelas y Tacones
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(render_service("👞 Suelas y Medias Suelas", "Cambio completo de suelas de cuero o goma (Vibram/Dainite) para zapatos de vestir y botas."), unsafe_allow_html=True)
with c2:
    st.markdown(render_service("👠 Renovación de Tacones", "Reemplazo de tapas de tacón, bloques de madera o plástico y forrado de tacones en cuero."), unsafe_allow_html=True)
with c3:
    st.markdown(render_service("🧗 Calzado de Montaña", "Especialistas en botas de trekking. Cambio de suelas con máximo agarre y refuerzos laterales."), unsafe_allow_html=True)

# Fila 2: Estética y Cuero
c4, c5, c6 = st.columns(3)
with c4:
    st.markdown(render_service("🎨 Tinturado y Recolor", "Restauración de color original o cambio total de tono usando tintes europeos de alta fijación."), unsafe_allow_html=True)
with c5:
    st.markdown(render_service("✨ Limpieza Deep Clean", "Tratamiento profundo para gamuza, nubuck y cuero liso. Incluye hidratación y protección."), unsafe_allow_html=True)
with c6:
    st.markdown(render_service("🎒 Marroquinería", "Reparación de bolsos, carteras, mochilas y chaquetas. Cambio de cierres, broches y costuras."), unsafe_allow_html=True)

# --- 6. SECCIÓN FINAL: CONTACTO Y MAPA ---
st.write("<br><br>", unsafe_allow_html=True)
col_info, col_mapa = st.columns([1, 1.2])

with col_info:
    st.markdown(f"""
        <div style="background: white; padding: 30px; border-radius: 20px; border: 1px solid #eee;">
            <h3 style="font-family: Montserrat;">📍 Contacto Directo</h3>
            <p><b>Dirección:</b> Lauro Guerrero y José A. Eguiguren, Loja, Ecuador</p>
            <p><b>Teléfono:</b> 099 471 8745</p>
            <br>
            <h4 style="font-family: Montserrat;">📱 Síguenos</h4>
            <a href="https://www.facebook.com/TheWarriorBrothersLoja" class="social-btn" style="background:#1877F2">Facebook</a>
            <a href="https://www.instagram.com/thewarriorbrothers2023" class="social-btn" style="background:#E1306C">Instagram</a>
            <a href="https://www.tiktok.com/@the.warrior.broth" class="social-btn" style="background:#000">TikTok</a>
        </div>
    """, unsafe_allow_html=True)

with col_mapa:
    mapa_html = f"""
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2319.6535553983294!2d-79.20821527422483!3d-3.9967444553015996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91cb491f5912b73b%3A0xa1e733db367e07a6!2sThe%20Warrior%20Brothers!5e1!3m2!1ses!2sec!4v1776383384965!5m2!1ses!2sec" 
        width="100%" height="400" style="border:0; border-radius:20px;" 
        allowfullscreen="" loading="lazy">
    </iframe>
    """
    components.html(mapa_html, height=420)

st.markdown("<center style='color: #aaa; margin-top: 50px;'>© 2026 The Warrior Brothers | Loja, Ecuador 🛡️⚒️</center><br>", unsafe_allow_html=True)
