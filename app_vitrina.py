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
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" style="width:160px; filter: drop-shadow(0px 4px 10px rgba(0,0,0,0.5));">' if logo_base_64 else ""

# --- 2. DISEÑO CSS AVANZADO (FONDO Y LETRAS) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Playfair+Display:wght@700&display=swap');
    
    .stApp {{ background-color: #ffffff; }}

    /* FONDO DE PANTALLA BONITO (HERO SECTION) */
    .hero-container {{
        background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)), 
                    url('https://images.unsplash.com/photo-1590739225287-bd265003ad3c?q=80&w=2000&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 120px 20px;
        text-align: center;
        color: white;
        border-radius: 0 0 50px 50px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
        margin-bottom: 50px;
        margin-top: -60px; /* Sube la sección para que pegue al borde superior */
    }}

    /* TÍTULO CON LETRAS GRANDES QUE RESALTAN */
    .main-title {{
        font-family: 'Montserrat', sans-serif;
        font-size: clamp(3rem, 10vw, 6rem);
        font-weight: 900;
        text-transform: uppercase;
        margin: 20px 0;
        line-height: 1;
        letter-spacing: -2px;
        background: linear-gradient(to bottom, #FFFFFF, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 5px 15px rgba(0,0,0,0.8));
    }}

    .sub-hero {{
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: #f0f0f0;
        max-width: 800px;
        margin: 0 auto;
        font-style: italic;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{ background-color: #111111; border-right: 3px solid #FFD700; }}
    
    /* Botones de Redes */
    .social-btn {{
        display: inline-flex; align-items: center; justify-content: center;
        padding: 10px 20px; border-radius: 8px; text-decoration: none;
        color: white !important; font-weight: bold; margin: 5px;
        transition: 0.3s;
    }}
    .fb {{ background: #1877F2; }} .ig {{ background: #E1306C; }} .tk {{ background: #000; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. MENÚ LATERAL ---
with st.sidebar:
    st.markdown("<h2 style='color:white; text-align:center;'>MENÚ</h2>", unsafe_allow_html=True)
    opcion = st.radio("", ["🏠 Inicio", "🛠️ Servicios", "🛍️ Tienda", "📍 Contacto"])
    st.markdown("---")
    st.markdown("<p style='color:#FFD700; text-align:center;'>COMPARTIR:</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <center>
        <a href="https://facebook.com/TheWarriorBrothersLoja" target="_blank" style="color:white; text-decoration:none;">Facebook</a><br><br>
        <a href="https://instagram.com/thewarriorbrothers2023" target="_blank" style="color:white; text-decoration:none;">Instagram</a>
        </center>
    """, unsafe_allow_html=True)

# --- 4. CONTENIDO ---

if opcion == "🏠 Inicio":
    # LA PARTE CON EL LOGO, TÍTULO Y FONDO BONITO
    st.markdown(f"""
        <div class="hero-container">
            {logo_html}
            <h1 class="main-title">THE WARRIOR BROTHERS</h1>
            <p class="sub-hero">
                Más de 20 años de maestría artesanal en reparación de calzado, cuero y mochilas. 
                Los mejores materiales del mercado con garantía total.
            </p>
            <br>
            <a href="https://wa.me/593994718745" style="background:#25D366; color:white; padding:18px 40px; border-radius:50px; text-decoration:none; font-weight:bold; font-size:1.2rem; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">AGENDAR REPARACIÓN</a>
        </div>
    """, unsafe_allow_html=True)

    # Bloque de confianza
    col1, col2, col3 = st.columns(3)
    col1.metric("Experiencia", "20+ Años")
    col2.metric("Calidad", "Premium")
    col3.metric("Ubicación", "Loja, EC")

elif opcion == "🛠️ Servicios":
    st.header("Servicios de Taller")
    st.write("Especialistas en cuero, suelas Vibram y restauraciones complejas.")

elif opcion == "🛍️ Tienda":
    st.header("Productos Disponibles")
    st.info("Próximamente: Cordones reforzados, plantillas de confort y kits de limpieza profesional.")

elif opcion == "📍 Contacto":
    st.header("Contacto y Redes")
    c_info, c_map = st.columns([1, 1.5])
    with c_info:
        st.markdown("""
            <div style="background:#f8f9fa; padding:20px; border-radius:15px; border-left:6px solid #FFD700;">
                <p>📍 <b>Dirección:</b> Lauro Guerrero y José A. Eguiguren</p>
                <p>📞 <b>WhatsApp:</b> 099 471 8745</p>
                <a href="#" class="social-btn fb">Facebook</a>
                <a href="#" class="social-btn ig">Instagram</a>
            </div>
        """, unsafe_allow_html=True)
    with c_map:
        mapa_html = f'<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2319.6535553983294!2d-79.20821527422483!3d-3.9967444553015996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91cb491f5912b73b%3A0xa1e733db367e07a6!2sThe%20Warrior%20Brothers!5e1!3m2!1ses!2sec!4v1776383384965!5m2!1ses!2sec" width="100%" height="400" style="border:0; border-radius:20px;" allowfullscreen="" loading="lazy"></iframe>'
        components.html(mapa_html, height=420)

st.markdown("<br><hr><center>© 2026 The Warrior Brothers 🛡️⚒️</center>", unsafe_allow_html=True)
