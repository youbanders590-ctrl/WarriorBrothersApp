import streamlit as st
import base64

# 1. Configuración de pantalla completa
st.set_page_config(page_title="The Warrior Brothers", layout="wide")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

# Intenta cargar tu logo
logo_b64 = get_base64_image("logo.png")
logo_tag = f'<img src="data:image/png;base64,{logo_b64}" style="width:250px;">' if logo_b64 else ""

# 2. El diseño "Maestro" (HTML y CSS puro)
st.markdown(f"""
    <style>
        /* Ocultar elementos de Streamlit que estorban */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        [data-testid="stSidebar"] {{display: none;}}
        .block-container {{padding: 0;}}

        /* Contenedor principal */
        .full-page {{
            background-color: #0e1117;
            color: white;
            font-family: 'Helvetica', sans-serif;
            text-align: center;
            min-height: 100vh;
            padding: 80px 20px;
        }}

        /* TÍTULO GIGANTE CENTRADO */
        .titulo {{
            font-size: 6rem;
            font-weight: 900;
            color: #FFD700;
            margin: 30px 0;
            text-transform: uppercase;
            letter-spacing: -2px;
        }}

        /* SUBTÍTULO */
        .subtitulo {{
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 50px;
        }}

        /* PÁRRAFO DE CUERPO GRANDE */
        .texto {{
            font-size: 1.8rem;
            line-height: 1.6;
            max-width: 1000px;
            margin: 0 auto 40px auto;
            color: #f0f0f0;
        }}

        /* AVISO DE PRECIO */
        .precio-aviso {{
            font-size: 2.2rem;
            font-weight: 900;
            color: #FFD700;
            margin: 50px 0;
        }}

        /* NOTA AL PIE */
        .nota {{
            font-size: 1.3rem;
            color: #999;
            max-width: 900px;
            margin: 0 auto;
            font-style: italic;
        }}

        /* BOTÓN WHATSAPP */
        .boton {{
            display: inline-block;
            background-color: #25D366;
            color: white !important;
            padding: 25px 60px;
            border-radius: 60px;
            text-decoration: none;
            font-weight: bold;
            font-size: 2rem;
            margin-top: 60px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
    </style>

    <div class="full-page">
        {logo_tag}
        
        <h1 class="titulo">THE WARRIOR BROTHERS</h1>
        
        <h2 class="subtitulo">Reparación Profesional de Calzado</h2>
        
        <p class="texto">
            Como nuestro servicio estrella, somos expertos en reparación de calzado. 
            Con <b>40 años de experiencia combinada</b> de nuestros dos zapateros, ¡nos encargamos de todo! 
            Desde restauraciones completas de calzado de alta gama hasta el cambio de tacones de zapatos de uso diario. 
            También ofrecemos <b>servicio de envío a domicilio</b>. Contáctenos para solicitar un presupuesto.
        </p>
        
        <p class="precio-aviso">
            EL PRECIO SE DETERMINA TRAS LA INSPECCIÓN DEL CALZADO
        </p>
        
        <p class="nota">
            Tenga en cuenta que la reparación de calzado es un servicio personalizado. Dado que cada zapato usado tiene diferentes formas, tamaños y condiciones, nos esforzamos al máximo para reparar sus zapatos con la mayor calidad posible, considerando su estado actual y los métodos disponibles en la industria.
        </p>
        
        <a href="https://wa.me/593994718745" class="boton">WHATSAPP: 099 471 8745</a>
    </div>
""", unsafe_allow_html=True)
