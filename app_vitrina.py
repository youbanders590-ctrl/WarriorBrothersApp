import streamlit as st
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
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" style="width:180px; margin-bottom: 10px;">' if logo_base_64 else ""

# --- 2. DISEÑO CSS (CENTRADO TOTAL Y LETRAS GRANDES) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Open+Sans:wght@600;700&display=swap');
    
    .stApp {{ background-color: #0e1117; }}

    .main-container {{
        text-align: center;
        padding: 60px 20px;
        color: white;
        font-family: 'Open Sans', sans-serif;
    }}

    /* TÍTULO PRINCIPAL CENTRADO Y GRANDE */
    .main-title {{
        font-family: 'Montserrat', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        color: #FFD700;
        margin: 0px 0px 40px 0px;
        text-transform: uppercase;
        line-height: 1;
    }}

    /* SUBTÍTULO DE SECCIÓN */
    .section-headline {{
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 30px;
    }}

    /* PÁRRAFOS GRANDES Y CLAROS */
    .content-text {{
        font-size: 1.6rem;
        line-height: 1.6;
        max-width: 1100px;
        margin: 0 auto 30px auto;
        color: #e0e0e0;
    }}

    .price-notice {{
        font-size: 1.8rem;
        font-weight: 700;
        color: #FFD700;
        margin: 40px 0;
        text-transform: uppercase;
    }}

    .disclaimer {{
        font-size: 1.2rem;
        color: #aaaaaa;
        max-width: 900px;
        margin: 0 auto;
        font-style: italic;
    }}

    /* BOTÓN WHATSAPP */
    .wa-button {{
        display: inline-block;
        background-color: #25D366;
        color: white !important;
        padding: 20px 50px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.5rem;
        margin-top: 50px;
        transition: 0.3s;
    }}
    .wa-button:hover {{ transform: scale(1.05); background-color: #128c7e; }}

    /* OCULTAR MENÚ LATERAL SI NO SE USA */
    [data-testid="stSidebar"] {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTENIDO DE LA PÁGINA ---
st.markdown(f"""
    <div class="main-container">
        <center>{logo_html}</center>
        
        <h1 class="main-title">THE WARRIOR BROTHERS</h1>
        
        <h2 class="section-headline">Reparación Profesional de Calzado</h2>
        
        <p class="content-text">
            Como nuestro servicio estrella, somos expertos en reparación de calzado. 
            Con <b>40 años de experiencia combinada</b> de nuestros dos zapateros, ¡nos encargamos de todo! 
            Desde restauraciones completas de calzado de alta gama hasta el cambio de tacones de zapatos de uso diario. 
            También ofrecemos <b>servicio de envío a domicilio</b>. Contáctenos para solicitar un presupuesto.
        </p>
        
        <p class="price-notice">
            EL PRECIO SE DETERMINA TRAS LA INSPECCIÓN DEL CALZADO
        </p>
        
        <p class="disclaimer">
            Tenga en cuenta que la reparación de calzado es un servicio personalizado. Dado que cada zapato usado tiene diferentes formas, tamaños y condiciones, nos esforzamos al máximo para reparar sus zapatos con la mayor calidad posible, considerando su estado actual y los métodos disponibles en la industria.
        </p>
        
        <a href="https://wa.me/593994718745" class="wa-button">WHATSAPP: 099 471 8745</a>
    </div>
""", unsafe_allow_html=True)
