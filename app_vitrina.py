import streamlit as st
import streamlit.components.v1 as components
import base64

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="🛡️", layout="wide")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" style="width:180px; filter: drop-shadow(0px 5px 15px rgba(0,0,0,0.6));">' if logo_base_64 else ""

# --- 2. DISEÑO CSS PERSONALIZADO ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Open+Sans:wght@400;600&display=swap');
    
    .stApp {{ background-color: #ffffff; }}

    /* PORTADA PRINCIPAL (HERO) */
    .hero-container {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('https://images.unsplash.com/photo-1556761175-b413da4baf72?q=80&w=2000&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        text-align: center;
        color: white;
        border-radius: 0 0 50px 50px;
        margin-top: -60px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
    }}

    .main-title {{
        font-family: 'Montserrat', sans-serif;
        font-size: clamp(2.5rem, 8vw, 5rem);
        font-weight: 900;
        margin: 20px 0;
        letter-spacing: -1px;
        background: linear-gradient(to bottom, #FFFFFF 50%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 4px 10px rgba(0,0,0,0.5));
    }}

    .about-text {{
        font-family: 'Open Sans', sans-serif;
        font-size: 1.35rem;
        max-width: 900px;
        margin: 0 auto;
        line-height: 1.7;
        color: #f0f0f0;
    }}

    /* Estilo del Menú Lateral (Sidebar) */
    [data-testid="stSidebar"] {{ background-color: #111111; border-right: 3px solid #FFD700; }}
    [data-testid="stSidebar"] .stRadio > div {{ color: white !important; font-weight: bold; }}

    /* Botones de Redes Sociales */
    .social-btn {{
        display: inline-flex; align-items: center; justify-content: center;
        padding: 12px 25px; border-radius: 12px; text-decoration: none;
        color: white !important; font-weight: bold; margin: 10px 5px;
        font-family: 'Montserrat', sans-serif; transition: 0.3s;
        width: 180px;
    }}
    .fb {{ background: #1877F2; }}
    .ig {{ background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); }}
    .tk {{ background: #000000; border: 1px solid #fe2c55; }}

    .store-card {{
        background: white; border-radius: 20px; padding: 30px;
        border: 1px solid #eee; box-shadow: 0 5px 20px rgba(0,0,0,0.05);
        text-align: center; height: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. MENÚ DE NAVEGACIÓN ---
with st.sidebar:
    st.markdown("<h2 style='color:white; text-align:center;'>MENÚ</h2>", unsafe_allow_html=True)
    opcion = st.radio("", ["🏠 Inicio", "🛠️ Servicios del Taller", "🛍️ Productos (Tienda)", "📍 Contacto y Redes"])
    st.markdown("---")
    st.markdown("<p style='color:#FFD700; text-align:center;'>Loja, Ecuador</p>", unsafe_allow_html=True)

# --- 4. CONTENIDO POR SECCIÓN ---

if opcion == "🏠 Inicio":
    # PORTADA PRINCIPAL SOLICITADA
    st.markdown(f"""
        <div class="hero-container">
            {logo_html}
            <h1 class="main-title">THE WARRIOR BROTHERS</h1>
            <p class="about-text">
                Somos una tienda especializada en la <b>reparación de calzado, artículos de cuero, bolsos, carteras, mochilas</b> y más. 
                Contamos con <b>más de 20 años de experiencia</b>, posicionándonos como los mejores en nuestra labor. 
                Trabajamos con los <b>mejores materiales del mercado</b> para garantizar resultados de alta durabilidad y calidad.
            </p>
            <br>
            <a href="https://wa.me/593994718745" style="background:#25D366; color:white; padding:18px 40px; border-radius:50px; text-decoration:none; font-weight:bold; font-size:1.1rem; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">WHATSAPP: 099 471 8745</a>
        </div>
    """, unsafe_allow_html=True)

    # Sección extra de confianza
    st.write("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.success("⚒️ **Calidad Garantizada:** Materiales premium y mano de obra experta.")
    with c2:
        st.info("🕒 **Trayectoria:** Dos décadas cuidando el calzado de los lojanos.")

elif opcion == "🛠️ Servicios del Taller":
    st.header("Servicios de Reparación")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="store-card"><h3>👞 Calzado</h3><p>Suelas, tacos y restauraciones completas.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="store-card"><h3>🎒 Mochilas</h3><p>Costuras, cierres y refuerzos estructurales.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="store-card"><h3>👜 Cuero</h3><p>Limpieza y mantenimiento de carteras y maletas.</p></div>', unsafe_allow_html=True)

elif opcion == "🛍️ Productos (Tienda)":
    st.header("Productos para el cuidado")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="store-card"><h3>🧶 Cordones</h3><p>Reforzados de varios colores</p><p style="color:#25D366; font-size:1.5rem; font-weight:bold;">$2.50</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="store-card"><h3>👟 Plantillas</h3><p>Confort y Gel</p><p style="color:#25D366; font-size:1.5rem; font-weight:bold;">$5.00</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="store-card"><h3>🧼 Limpiadores</h3><p>Kits profesionales</p><p style="color:#25D366; font-size:1.5rem; font-weight:bold;">$8.50</p></div>', unsafe_allow_html=True)

elif opcion == "📍 Contacto y Redes":
    st.header("Ubicación y Redes Sociales")
    cl, cr = st.columns([1, 1.3])
    with cl:
        st.markdown(f"""
            <div style="background:#f8f9fa; padding:25px; border-radius:20px; border-left:5px solid #FFD700;">
                <h4>📍 Dirección</h4>
                <p>Lauro Guerrero y José A. Eguiguren, Loja, Ecuador</p>
                <hr>
                <h4>📱 Redes Sociales</h4>
                <a href="https://facebook.com/TheWarriorBrothersLoja" class="social-btn fb" target="_blank">Facebook</a>
                <a href="https://instagram.com/thewarriorbrothers2023" class="social-btn ig" target="_blank">Instagram</a>
                <a href="https://www.tiktok.com/@the.warrior.broth" class="social-btn tk" target="_blank">TikTok</a>
            </div>
        """, unsafe_allow_html=True)
    with cr:
        mapa_html = f'<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2319.6535553983294!2d-79.20821527422483!3d-3.9967444553015996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91cb491f5912b73b%3A0xa1e733db367e07a6!2sThe%20Warrior%20Brothers!5e1!3m2!1ses!2sec!4v1776383384965!5m2!1ses!2sec" width="100%" height="450" style="border:0; border-radius:20px;" allowfullscreen="" loading="lazy"></iframe>'
        components.html(mapa_html, height=480)

# --- 5. FOOTER ---
st.markdown("<br><hr><center>© 2026 The Warrior Brothers | Pasión por el Detalle 🛡️⚒️</center>", unsafe_allow_html=True)
