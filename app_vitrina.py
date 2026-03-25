import streamlit as st
from datetime import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="🛡️ The Warrior Brothers | Maestros en Reparación de Calzado",
    page_icon="👞",
    layout="wide",
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Fondo y texto general */
    .stApp { background-color: #fcfdfa; color: #1e1e1e; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    
    /* Títulos Principales */
    h1, h2, h3 { font-weight: 700; color: #1e1e1e; letter-spacing: -1px; }
    h1 { font-size: 3.5rem; margin-bottom: 0.5rem; }
    h2 { font-size: 2.2rem; border-bottom: 3px solid #1e1e1e; padding-bottom: 10px; margin-top: 40px; }
    
    /* Botones de WhatsApp */
    .whatsapp-btn {
        background-color: #25D366; color: white !important; padding: 15px 30px; text-decoration: none;
        font-size: 1.1rem; border-radius: 50px; font-weight: bold; text-align: center;
        display: inline-block; transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        border: none;
    }
    .whatsapp-btn:hover { background-color: #1ebe57; transform: translateY(-3px); color: white !important; }

    /* Tarjetas de Servicios */
    .service-card {
        background-color: white; border-radius: 15px; padding: 25px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06); transition: transform 0.3s ease;
        border: 1px solid #eee; text-align: center; height: 100%;
    }
    .service-card:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
    .service-card h4 { margin-top: 15px; font-weight: 600; font-size: 1.3rem; }
    .service-card p { color: #555; font-size: 0.95rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. SECCIÓN HÉROE (CON TU LOGO OFICIAL) ---
# RECUERDA: Cambia 'URL_DE_TU_IMAGEN_PNG' por el enlace de tu logo que subiste a GitHub o ImgBB
st.markdown("""
    <div style="background-color: #1e1e1e; color: white; padding: 90px 40px; text-align: center; border-radius: 20px; margin-bottom: 50px;">
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <img src="URL_DE_TU_IMAGEN_PNG" style="max-width: 180px; height: auto; filter: brightness(0) invert(1);">
        </div> 
        <h1 style="color: white; margin-bottom: 10px;">The Warrior Brothers</h1>
        <p style="font-size: 1.6rem; font-weight: 300; color: #ccc;">Maestría en Restauración de Calzado y Cuero</p>
        <p style="font-size: 1.1rem; margin-top: 20px; max-width: 800px; margin-left: auto; margin-right: auto;">
            No solo reparamos, devolvemos la esencia a tus artículos favoritos. Artesanía lojana con precisión digital.
        </p>
        <br>
        <a href="https://wa.me/593994718745?text=¡Hola%20Warrior%20Brothers!%20Quisiera%20cotizar%20una%20reparación" target="_blank" class="whatsapp-btn">Cotizar mi Trabajo Ahora</a>
    </div>
    """, unsafe_allow_html=True)

# --- 2. SECCIÓN DE SERVICIOS ---
st.header("🛠️ Especialidades del Taller")
col1, col2, col3, col4 = st.columns(4)

servicios = [
    ["Suelas y Pisos", "Cambio de suelas de caucho, cuero y montaña.", "👞"],
    ["Tinturado", "Restauración de color profesional para cuero y gamuza.", "🎨"],
    ["Tacos y Tapas", "Arreglo preciso para calzado de dama y caballero.", "👠"],
    ["Accesorios", "Reparación de maletas, mochilas y costuras de chompas.", "🎒"]
]

for col, ser in zip([col1, col2, col3, col4], servicios):
    with col:
        st.markdown(f"""
            <div class="service-card">
                <div style="font-size: 50px; padding: 20px;">{ser[2]}</div>
                <h4>{ser[0]}</h4>
                <p>{ser[1]}</p>
            </div>
            """, unsafe_allow_html=True)

# --- 3. SECCIÓN A DOMICILIO ---
st.markdown("""
    <div style="background-color: #f1f1f1; padding: 60px 30px; border-radius: 20px; margin-top: 50px; text-align: center; border: 2px dashed #1e1e1e;">
        <h2 style="border:none; margin-top:0;">🚀 Servicio a Domicilio en Loja</h2>
        <p style="font-size: 1.2rem; max-width: 700px; margin: 20px auto;">Recogemos tus zapatos y los entregamos listos en la puerta de tu hogar o taller.</p>
        <p style="font-weight: bold; font-size: 2.5rem; color: #1e1e1e; margin-top: 10px;">+$5.00</p>
        <p style="color: #777;">Cobertura en toda el área urbana de Loja.</p>
        <br>
        <a href="https://wa.me/593994718745?text=Hola!%20Deseo%20el%20servicio%20a%20domicilio" class="whatsapp-btn">Solicitar Retiro</a>
    </div>
    """, unsafe_allow_html=True)

# --- 4. CONTACTO Y UBICACIÓN ---
st.header("📍 Encuéntranos")
c1, c2 = st.columns([1, 1.5])

with c1:
    st.subheader("Información")
    st.markdown("""
        **📍 Dirección:**<br>
        Loja, Ecuador (Centro de la ciudad)<br><br>
        **📱 WhatsApp:**<br>
        [0994718745](https://wa.me/593994718745)<br><br>
        **🕒 Horarios:**<br>
        Lun - Vie: 08h00 a 18h00<br>
        Sáb: 09h00 a 13h00
        """, unsafe_allow_html=True)

with c2:
    # Espacio para el mapa
    st.markdown("""
        <div style="width: 100%; height: 350px; background-color: #eee; border-radius: 20px; display: flex; align-items: center; justify-content: center; flex-direction: column;">
            <p style="color: #777;">[ Mapa de Loja - The Warrior Brothers ]</p>
            <p style="font-size: 0.8rem; color: #999;">Ubicación estratégica para tu comodidad</p>
        </div>
        """, unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown("""
    <div style="text-align: center; color: #777; padding: 40px; border-top: 1px solid #eee; margin-top: 60px;">
        <p>© 2026 The Warrior Brothers. Orgullosamente Lojanos. 🛡️⚒️</p>
    </div>
    """, unsafe_allow_html=True)
