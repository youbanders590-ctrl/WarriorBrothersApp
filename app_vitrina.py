import streamlit as st
import base64

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="The Warrior Brothers | Maestros en Reparación",
    page_icon="👞",
    layout="wide",
)

# --- CARGA DEL LOGO (EL QUE YA FUNCIONA) ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

logo_base64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base64}" style="width:80px; margin-right:20px;">' if logo_base64 else ""

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #fcfdfa; color: #1e1e1e; }
    .hero-black {
        background-color: #1e1e1e; color: white; padding: 60px; 
        border-radius: 20px; text-align: center; margin-bottom: 40px;
    }
    .flex-header { display: flex; align-items: center; justify-content: center; margin-bottom: 10px; }
    .whatsapp-btn {
        background-color: #25D366; color: white !important; padding: 15px 30px; 
        text-decoration: none; border-radius: 50px; font-weight: bold; display: inline-block;
    }
    .service-card {
        background-color: white; border-radius: 15px; padding: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; height: 100%;
        border: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. ENCABEZADO (HERO) ---
st.markdown(f"""
    <div class="hero-black">
        <div class="flex-header">
            {logo_html}
            <h1 style="color: white; font-size: 3.5rem; font-weight: 900; margin: 0;">THE WARRIOR BROTHERS</h1>
        </div>
        <p style="font-size: 1.5rem; color: #ccc;">Especialistas en Restauración de Calzado y Cuero</p>
        <p>Artesanía lojana con precisión digital.</p>
        <br>
        <a href="https://wa.me/593994718745" class="whatsapp-btn">Cotizar mi Trabajo Ahora</a>
    </div>
    """, unsafe_allow_html=True)

# --- 2. SERVICIOS (RECUPERADOS) ---
st.header("🛠️ Nuestras Especialidades")
col1, col2, col3, col4 = st.columns(4)

servicios = [
    ["Suelas y Pisos", "👞 Cambio de suelas de caucho y cuero."],
    ["Tinturado Pro", "🎨 Restauración total de color."],
    ["Tacos y Tapas", "👠 Arreglo preciso para damas."],
    ["Accesorios", "🎒 Reparación de maletas y costuras."]
]

for col, ser in zip([col1, col2, col3, col4], servicios):
    with col:
        st.markdown(f"""<div class="service-card"><h4>{ser[0]}</h4><p>{ser[1]}</p></div>""", unsafe_allow_html=True)

# --- 3. SERVICIO A DOMICILIO ---
st.write("")
st.markdown("""
    <div style="background-color: #f1f1f1; padding: 40px; border-radius: 20px; text-align: center; border: 2px dashed #1e1e1e;">
        <h3>🚀 Servicio a Domicilio en Loja</h3>
        <p>Recogemos y entregamos tus zapatos por <b>+$5.00</b> adicionales.</p>
        <a href="https://wa.me/593994718745?text=Deseo%20servicio%20a%20domicilio" class="whatsapp-btn" style="background-color: #1e1e1e;">Solicitar Retiro</a>
    </div>
    """, unsafe_allow_html=True)

# --- 4. UBICACIÓN Y CONTACTO ---
st.write("")
st.header("📍 Encuéntranos")
c1, c2 = st.columns(2)

with c1:
    st.subheader("Información de Contacto")
    st.write("**Dirección:** Centro de la ciudad, Loja, Ecuador")
    st.write("**WhatsApp:** [0994718745](https://wa.me/593994718745)")
    st.write("**Horario:** Lun - Vie (08:00 - 19:00) | Sáb (08:00 - 15:30)")

with c2:
    st.info("🗺️ **Mapa de Loja**\n\nPróximamente integraremos el mapa interactivo aquí.")

st.markdown("<br><hr><center>© 2026 The Warrior Brothers. Orgullosamente Lojanos. 🛡️⚒️</center>", unsafe_allow_html=True)
