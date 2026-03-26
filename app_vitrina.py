import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="🛡️ The Warrior Brothers | Maestros en Reparación de Calzado",
    page_icon="👞",
    layout="wide",
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    .stApp { background-color: #fcfdfa; color: #1e1e1e; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    
    .whatsapp-btn {
        background-color: #25D366; color: white !important; padding: 15px 30px; text-decoration: none;
        font-size: 1.1rem; border-radius: 50px; font-weight: bold; text-align: center;
        display: inline-block; transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    
    .header-container {
        display: flex; align-items: center; justify-content: center; margin-bottom: 25px;
    }
    .header-logo {
        max-width: 80px; height: auto; margin-right: 20px;
    }
    .header-title {
        color: white !important; font-size: 3.5rem; font-weight: 900; letter-spacing: -2px; margin: 0;
    }
    
    .service-card {
        background-color: white; border-radius: 15px; padding: 25px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06); text-align: center; height: 100%;
        border: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. SECCIÓN HÉROE (CON EL FIX PARA QUE NO SALGA TEXTO) ---
st.markdown("""
    <div style="background-color: #1e1e1e; color: white; padding: 100px 40px; text-align: center; border-radius: 20px; margin-bottom: 50px;">
        
        <div class="header-container">
            <img src="https://raw.githubusercontent.com/tu_usuario/tu_repo/main/logo.png" class="header-logo">
            <h1 class="header-title">THE WARRIOR BROTHERS</h1>
        </div>
        
        <p style="font-size: 1.6rem; font-weight: 300; color: #ccc;">Maestría en Restauración de Calzado y Cuero</p>
        <p style="font-size: 1.1rem; margin-top: 20px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">
            No solo reparamos, devolvemos la esencia a tus artículos favoritos. Artesanía lojana con precisión digital.
        </p>
        <br>
        <a href="https://wa.me/593994718745?text=¡Hola%20Warrior%20Brothers!%20Quisiera%20cotizar%20una%20reparación" target="_blank" class="whatsapp-btn">Cotizar mi Trabajo Ahora</a>
    </div>
    """, unsafe_allow_html=True)

# --- 2. SERVICIOS ---
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

# --- 3. CONTACTO ---
st.markdown("""
    <div style="text-align: center; color: #777; padding: 40px; border-top: 1px solid #eee; margin-top: 60px;">
        <p>© 2026 The Warrior Brothers. Orgullosamente Lojanos. 🛡️⚒️</p>
    </div>
    """, unsafe_allow_html=True)
