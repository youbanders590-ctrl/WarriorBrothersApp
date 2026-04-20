import streamlit as st
import streamlit.components.v1 as components
import base64

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="The Warrior Brothers | Inicio", page_icon="🛡️", layout="wide")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" style="width:180px;">' if logo_base_64 else ""

# --- 2. ESTILOS CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');
    
    .stApp { background-color: #ffffff; }
    
    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #111111; border-right: 2px solid #FFD700; }
    
    /* Hero Section */
    .hero-main {
        padding: 80px 40px; text-align: center; background: #fdfdfd;
        border-radius: 30px; border: 1px solid #eee; margin-top: 20px;
    }
    .main-title { font-family: 'Montserrat', sans-serif; font-size: 3.5rem; font-weight: 900; color: #1a1a1a; }
    .highlight { color: #FFD700; }
    
    /* Tarjetas */
    .store-card {
        background: white; border-radius: 20px; padding: 25px; text-align: center;
        border: 1px solid #eee; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: 0.3s;
    }
    .store-card:hover { transform: translateY(-5px); border-color: #FFD700; }
    
    /* Botones de Redes Sociales */
    .social-btn {
        display: inline-flex; align-items: center; justify-content: center;
        padding: 12px 20px; border-radius: 10px; text-decoration: none;
        color: white !important; font-weight: bold; margin: 10px 5px; min-width: 150px;
        font-family: 'Montserrat', sans-serif; transition: 0.3s;
    }
    .social-btn:hover { transform: scale(1.05); filter: brightness(1.2); }
    .fb { background-color: #1877F2; }
    .ig { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); }
    .tk { background-color: #000000; border: 1px solid #fe2c55; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MENÚ DE NAVEGACIÓN (SIDEBAR) ---
with st.sidebar:
    if logo_html: st.markdown(f"<center>{logo_html}</center>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:white; text-align:center;'>MENÚ</h3>", unsafe_allow_html=True)
    opcion = st.radio("", ["🏠 Inicio", "🛠️ Servicios del Taller", "🛍️ Productos de Tienda", "📍 Ubicación y Redes"])
    st.markdown("---")
    st.markdown("<p style='color:#FFD700; text-align:center; font-weight:bold;'>SÍGUENOS:</p>", unsafe_allow_html=True)
    # Accesos rápidos en el menú
    st.markdown("""
        <center>
        <a href="https://www.facebook.com/TheWarriorBrothersLoja" target="_blank" style="text-decoration:none; color:white;">Facebook</a><br><br>
        <a href="https://www.instagram.com/thewarriorbrothers2023" target="_blank" style="text-decoration:none; color:white;">Instagram</a><br><br>
        <a href="https://www.tiktok.com/@the.warrior.broth" target="_blank" style="text-decoration:none; color:white;">TikTok</a>
        </center>
    """, unsafe_allow_html=True)

# --- 4. CONTENIDO ---

if opcion == "🏠 Inicio":
    st.markdown(f"""
        <div class="hero-main">
            <h1 class="main-title">THE WARRIOR <span class="highlight">BROTHERS</span></h1>
            <p style="font-size: 1.3rem; color: #444; max-width: 850px; margin: 0 auto; line-height: 1.6;">
                Somos especialistas en la reparación de calzado, artículos de cuero, bolsos, carteras y mochilas. 
                Con <b>más de 20 años de experiencia</b>, somos líderes en nuestra labor, utilizando los 
                <b>mejores materiales del mercado</b> y ofreciendo garantía total en cada trabajo.
            </p>
            <br>
            <a href="https://wa.me/593994718745" style="background:#25D366; color:white; padding:15px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">COTIZAR POR WHATSAPP</a>
        </div>
    """, unsafe_allow_html=True)

elif opcion == "🛠️ Servicios del Taller":
    st.header("Servicios Especializados")
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown('<div class="store-card"><h3>👞 Calzado</h3><p>Suelas Vibram, tacos y restauración de color.</p></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="store-card"><h3>🎒 Mochilas</h3><p>Cambio de cierres, correas y reconstrucción.</p></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="store-card"><h3>👜 Marroquinería</h3><p>Limpieza y reparación de carteras y maletas.</p></div>', unsafe_allow_html=True)

elif opcion == "🛍️ Productos de Tienda":
    st.header("Cuidado del Calzado")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="store-card"><h3>🧶 Cordones</h3><p>Reforzados de alta duración</p><p style="color:#25D366; font-weight:bold;">$2.50</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="store-card"><h3>👟 Plantillas</h3><p>Gel y Confort Anatómico</p><p style="color:#25D366; font-weight:bold;">$5.00</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="store-card"><h3>🧼 Limpiadores</h3><p>Kits profesionales</p><p style="color:#25D366; font-weight:bold;">$8.50</p></div>', unsafe_allow_html=True)

elif opcion == "📍 Ubicación y Redes":
    st.header("Contacto y Redes Sociales")
    col_a, col_b = st.columns([1, 1.2])
    with col_a:
        st.markdown("""
            <div style="background:#f8f9fa; padding:25px; border-radius:20px; border-left:5px solid #FFD700;">
                <h4>📍 Nuestra Ubicación</h4>
                <p>Lauro Guerrero y José A. Eguiguren, Loja, Ecuador</p>
                <h4>⏰ Horario de Atención</h4>
                <p>Lun - Vie: 08:00 - 19:00<br>Sáb: 08:00 - 15:30</p>
                <hr>
                <h4>📱 Redes Sociales</h4>
                <a href="https://www.facebook.com/TheWarriorBrothersLoja" class="social-btn fb" target="_blank">👤 Facebook</a>
                <a href="https://www.instagram.com/thewarriorbrothers2023" class="social-btn ig" target="_blank">📸 Instagram</a>
                <a href="https://www.tiktok.com/@the.warrior.broth" class="social-btn tk" target="_blank">🎵 TikTok</a>
            </div>
        """, unsafe_allow_html=True)
    with col_b:
        mapa_html = f"""<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2319.6535553983294!2d-79.20821527422483!3d-3.9967444553015996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91cb491f5912b73b%3A0xa1e733db367e07a6!2sThe%20Warrior%20Brothers!5e1!3m2!1ses!2sec!4v1776383384965!5m2!1ses!2sec" width="100%" height="450" style="border:0; border-radius:20px;" allowfullscreen="" loading="lazy"></iframe>"""
        components.html(mapa_html, height=480)

# --- 5. FOOTER ---
st.markdown("<br><hr><center>© 2026 The Warrior Brothers | Loja - Ecuador 🇪🇨</center>", unsafe_allow_html=True)
