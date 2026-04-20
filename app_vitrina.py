import streamlit as st
import base64

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="🛡️", layout="wide")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

# Carga del logo (asegúrate de que el archivo esté en la misma carpeta)
logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" style="width:220px; margin-bottom: 20px;">' if logo_base_64 else ""

# --- 2. ESTILO CSS (CENTRADO Y LETRAS GRANDES) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Open+Sans:wght@700&display=swap');
    
    /* Fondo oscuro y limpieza de márgenes */
    .stApp {{
        background-color: #0e1117;
    }}

    .main-box {{
        text-align: center;
        padding: 50px 10px;
        color: white;
        font-family: 'Open Sans', sans-serif;
    }}

    /* TÍTULO GIGANTE Y CENTRADO */
    .titulo-principal {{
        font-family: 'Montserrat', sans-serif;
        font-size: 5.5rem;
        font-weight: 900;
        color: #FFD700;
        margin: 20px 0;
        text-transform: uppercase;
        line-height: 1.1;
    }}

    /* SUBTÍTULO RESALTADO */
    .subtitulo {{
        font-size: 3.2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 40px;
    }}

    /* TEXTO DE DESCRIPCIÓN GRANDE */
    .texto-cuerpo {{
        font-size: 1.8rem;
        line-height: 1.6;
        max-width: 1200px;
        margin: 0 auto 40px auto;
        color: #f0f0f0;
    }}

    /* AVISO DE PRECIOS */
    .aviso-precio {{
        font-size: 2rem;
        font-weight: 900;
        color: #FFD700;
        margin: 40px 0;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}

    /* TEXTO PEQUEÑO DE DESCARGO */
    .nota-final {{
        font-size: 1.3rem;
        color: #bbbbbb;
        max-width: 1000px;
        margin: 0 auto;
        font-style: italic;
        line-height: 1.4;
    }}

    /* BOTÓN WHATSAPP GIGANTE */
    .boton-wa {{
        display: inline-block;
        background-color: #25D366;
        color: white !important;
        padding: 25px 60px;
        border-radius: 60px;
        text-decoration: none;
        font-weight: 800;
        font-size: 1.8rem;
        margin-top: 50px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
    }}
    
    /* Quitar menús innecesarios */
    [data-testid="stSidebar"] {{ display: none; }}
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    </style>

    <div class="main-box">
        <center>{logo_html}</center>
        
        <h1 class="titulo-principal">THE WARRIOR BROTHERS</h1>
        
        <h2 class="subtitulo">Reparación Profesional de Calzado</h2>
        
        <p class="texto-cuerpo">
            Como nuestro servicio estrella, somos expertos en reparación de calzado. 
            Con <b>40 años de experiencia combinada</b> de nuestros dos zapateros, ¡nos encargamos de todo! 
            Desde restauraciones completas de calzado de alta gama hasta el cambio de tacones de zapatos de uso diario. 
            También ofrecemos <b>servicio de envío a domicilio</b>. Contáctenos para solicitar un presupuesto.
        </p>
        
        <p class="aviso-precio">
            EL PRECIO SE DETERMINA TRAS LA INSPECCIÓN DEL CALZADO
        </p>
        
        <p class="nota-final">
            Tenga en cuenta que la reparación de calzado es un servicio personalizado. Dado que cada zapato usado tiene diferentes formas, tamaños y condiciones, nos esforzamos al máximo para reparar sus zapatos con la mayor calidad posible, considerando su estado actual y los métodos disponibles en la industria.
        </p>
        
        <a href="https://wa.me/593994718745" class="boton-wa">WHATSAPP: 099 471 8745</a>
    </div>
""", unsafe_allow_html=True)
