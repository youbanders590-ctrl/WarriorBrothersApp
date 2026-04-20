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

# Carga del logo (asegúrate de que el archivo se llame logo.png)
logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" style="width:120px; vertical-align: middle; margin-right: 20px; filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.5));">' if logo_base_64 else ""

# --- 2. DISEÑO CSS PERSONALIZADO ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Open+Sans:wght@400;600&display=swap');
    
    .stApp {{ background-color: #ffffff; }}

    /* PORTADA PRINCIPAL CENTRADA */
    .hero-container {{
        background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
                    url('https://images.unsplash.com/photo-1556761175-b413da4baf72?q=80&w=2000&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        padding: 100px 40px;
        text-align: center; /* TODO CENTRADO */
        color: white;
        border-radius: 0 0 50px 50px;
        margin-top: -60px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
    }}

    .header-block {{
        display: flex;
        align-items: center;
        justify-content: center; /* CENTRA EL LOGO Y TÍTULO */
        flex-wrap: wrap;
        margin-bottom: 30px;
    }}

    .main-title {{
        font-family: 'Montserrat', sans-serif;
        font-size: clamp(2.5rem, 8vw, 5.5rem);
        font-weight: 900;
        margin: 0;
        text-transform: uppercase;
        background: linear-gradient(to bottom, #FFFFFF 50%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 4px 10px rgba(0,0,0,0.5));
    }}

    .section-headline {{
        font-family: 'Montserrat', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #FFD700;
        margin-top: 40px;
        margin-bottom: 20px;
    }}

    .content-text {{
        font-family: 'Open Sans', sans-serif;
        font-size: 1.25rem;
        max-width: 1000px;
        margin: 0 auto 25px auto;
        line-height: 1.8;
        color: #f5f5f5;
        text-align: center;
    }}

    .price-notice {{
        font-style: italic;
        color: #FFD700;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{ background-color: #111111; border-right: 3px solid #FFD700; }}

    /* Botón WhatsApp */
    .wa-button {{
        background-color: #25D366;
        color: white !important;
        padding: 20px 45px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        transition: 0.3s;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        margin-top: 20px;
    }}
    .wa-button:hover {{ transform: scale(1.05); background-color: #128C7E; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. MENÚ LATERAL ---
with st.sidebar:
    st.markdown("<h2 style='color:white; text-align:center;'>MENÚ</h2>", unsafe_allow_html=True)
    opcion = st.radio("", ["🏠 Inicio", "🛠️ Otros Servicios", "🛍️ Tienda", "📍 Contacto"])

# --- 4. CONTENIDO ---

if opcion == "🏠 Inicio":
    # PORTADA CENTRADA SIN TEXTO A LA DERECHA
    st.markdown(f"""
        <div class="hero-container">
            <div class="header-block">
                {logo_html}
                <h1 class="main-title">THE WARRIOR BROTHERS</h1>
            </div>
            
            <h2 class="section-headline">Reparación Profesional de Calzado</h2>
            
            <p class="content-text">
                Como nuestro servicio estrella, somos expertos en reparación de calzado. 
                Con <b>40 años de experiencia combinada</b> de nuestros dos zapateros, ¡nos encargamos de todo! 
                Desde restauraciones completas de calzado de alta gama hasta el cambio de tacones de zapatos de uso diario. 
                También ofrecemos <b>servicio de envío a domicilio</b>. Contáctenos para solicitar un presupuesto.
            </p>
            
            <p class="price-notice">
                Lista de precios estimados: el precio de cada reparación se determina tras la inspección del calzado.
            </p>
            
            <p class="content-text" style="font-size: 1rem; opacity: 0.9;">
                Tenga en cuenta que la reparación de calzado es un servicio personalizado. Dado que cada zapato usado tiene diferentes formas, tamaños y condiciones, nos esforzamos al máximo para reparar sus zapatos con la mayor calidad posible, considerando su estado actual y los métodos disponibles en la industria.
            </p>
            
            <a href="https://wa.me/593994718745" class="wa-button">WHATSAPP: 099 471 8745</a>
        </div>
    """, unsafe_allow_html=True)

else:
    st.info("Sección en mantenimiento. Por favor, regrese a la página de Inicio.")

# --- 5. FOOTER ---
st.markdown("<br><hr><center>© 2026 The Warrior Brothers | Loja, Ecuador 🛡️⚒️</center>", unsafe_allow_html=True)
