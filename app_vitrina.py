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

# Carga del logo
logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" style="width:200px; margin-bottom: 20px; filter: drop-shadow(0px 10px 20px rgba(0,0,0,0.6));">' if logo_base_64 else ""

# --- 2. DISEÑO CSS PARA LETRAS GRANDES Y CENTRADO ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Open+Sans:wght@600;800&display=swap');
    
    .stApp {{ background-color: #ffffff; }}

    /* CONTENEDOR HERO GIGANTE */
    .hero-container {{
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url('https://images.unsplash.com/photo-1590739225287-bd265003ad3c?q=80&w=2000&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        padding: 120px 40px;
        text-align: center;
        color: white;
        border-radius: 0 0 60px 60px;
        margin-top: -80px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }}

    /* TÍTULO GIGANTE */
    .main-title {{
        font-family: 'Montserrat', sans-serif;
        font-size: clamp(3.5rem, 12vw, 7rem); /* LETRAS MUY GRANDES */
        font-weight: 900;
        margin: 10px 0;
        text-transform: uppercase;
        line-height: 0.9;
        background: linear-gradient(to bottom, #FFFFFF 40%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 8px 15px rgba(0,0,0,0.8));
    }}

    /* SUBTÍTULOS RESALTADOS */
    .section-headline {{
        font-family: 'Montserrat', sans-serif;
        font-size: clamp(1.8rem, 5vw, 3.5rem);
        font-weight: 800;
        color: #FFD700;
        margin-top: 50px;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }}

    /* TEXTO DE CONTENIDO GRANDE */
    .content-text {{
        font-family: 'Open Sans', sans-serif;
        font-size: clamp(1.2rem, 3vw, 1.6rem); /* AUMENTO DE TAMAÑO */
        font-weight: 600;
        max-width: 1100px;
        margin: 30px auto;
        line-height: 1.6;
        color: #ffffff;
    }}

    .price-notice {{
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        color: #FFD700;
        font-size: 1.4rem;
        text-transform: uppercase;
        margin-top: 40px;
    }}

    .disclaimer-text {{
        font-size: 1.1rem;
        color: #cccccc;
        max-width: 900px;
        margin: 20px auto;
        font-style: italic;
    }}

    /* BOTÓN WHATSAPP GRANDE */
    .wa-button {{
        background-color: #25D366;
        color: white !important;
        padding: 25px 60px;
        border-radius: 60px;
        text-decoration: none;
        font-weight: 900;
        font-size: 1.5rem;
        display: inline-block;
        margin-top: 40px;
        box-shadow: 0 15px 30px rgba(37,211,102,0.4);
        transition: 0.3s;
    }}
    .wa-button:hover {{ transform: scale(1.1); }}

    /* Sidebar */
    [data-testid="stSidebar"] {{ background-color: #000000; border-right: 4px solid #FFD700; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("<h2 style='color:white; text-align:center; font-family:Montserrat;'>MENÚ</h2>", unsafe_allow_html=True)
    st.radio("", ["🏠 Inicio", "📍 Ubicación", "📱 Redes Sociales"])

# --- 4. CUERPO DE LA PÁGINA ---
st.markdown(f"""
    <div class="hero-container">
        {logo_html}
        <h1 class="main-title">THE WARRIOR BROTHERS</h1>
        
        <h2 class="section-headline">Reparación Profesional de Calzado</h2>
        
        <p class="content-text">
            Como nuestro servicio estrella, somos expertos en reparación de calzado. 
            Con <b>40 años de experiencia combinada</b> de nuestros dos zapateros, ¡nos encargamos de todo! 
            Desde restauraciones completas de calzado de alta gama hasta el cambio de tacones de uso diario. 
            También ofrecemos <b>servicio de envío a domicilio</b>.
        </p>
        
        <p class="price-notice">
            EL PRECIO SE DETERMINA TRAS LA INSPECCIÓN DEL CALZADO
        </p>
        
        <p class="disclaimer-text">
            Tenga en cuenta que la reparación de calzado es un servicio personalizado. Nos esforzamos al máximo para reparar sus zapatos con la mayor calidad posible, considerando su estado actual y los métodos disponibles en la industria.
        </p>
        
        <a href="https://wa.me/593994718745" class="wa-button">WHATSAPP: 099 471 8745</a>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<br><center style='color:#888; font-weight:bold;'>© 2026 THE WARRIOR BROTHERS | LOJA, ECUADOR 🛡️⚒️</center><br>", unsafe_allow_html=True)
