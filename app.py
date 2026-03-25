import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
from pytz import timezone

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="The Warrior Brothers", layout="centered", page_icon="🛡️")

# --- DISEÑO PARA CENTRAR LOGO Y TÍTULO ---
# Usamos columnas para que el logo quede en el centro exacto
col_izq, col_centro, col_der = st.columns([2, 1, 2])

with col_centro:
    # Como ya veo que tienes 'logo.png' en tu GitHub, lo llamamos directo
    st.image("logo.png", width=85) 

# Título y subtítulo centrados
st.markdown("<h1 style='text-align: center;'>THE WARRIOR BROTHERS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>Zapatería y Restauración de Cuero</p>", unsafe_allow_html=True)
st.divider()

# --- CONEXIÓN A GOOGLE SHEETS ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- FECHA ACTUAL (ECUADOR) ---
ec_tz = timezone('America/Guayaquil')
fecha_actual = datetime.now(ec_tz).strftime("%d/%m/%Y %H:%M")

# --- FORMULARIO DE REGISTRO ---
with st.form("registro_trabajo", clear_on_submit=True):
    st.markdown(f"📅 **Fecha de Ingreso:** `{fecha_actual}`")
    
    cliente = st.text_input("👤 Nombre del Cliente:").strip()
    celular = st.text_input("📱 WhatsApp (sin el 0):")
    articulo = st.text_input("👞 Artículo:")
    reparacion = st.text_area("🛠️ Detalle de la Reparación:")
    
    c1, c2 = st.columns(2)
    with c1:
        total = st.number_input("💰 Valor Total $", min_value=0.0, step=0.5, format="%.2f")
    with c2:
        abono = st.number_input("💵 Abono Inicial $", min_value=0.0, step=0.5, format="%.2f")
    
    saldo = total - abono
    st.markdown(f"<h3 style='text-align: center;'>Saldo Pendiente: ${saldo:.2f}</h3>", unsafe_allow_html=True)
    
    entrega = st.date_input("📆 Fecha de Entrega Prometida")

    # Botón centrado y grande
    submit = st.form_submit_button("💾 GUARDAR REGISTRO")

# --- LÓGICA DE GUARDADO ---
if submit:
    if cliente and articulo:
        try:
            nuevo_registro = pd.DataFrame([{
                "Fecha": fecha_actual,
                "Cliente": cliente.upper(),
                "Celular": str(celular),
                "Articulo": articulo.lower(),
                "Reparacion": reparacion.lower(),
                "Total": float(total),
                "Abono": float(abono),
                "Saldo": float(saldo),
                "Entrega": entrega.strftime("%d/%m/%Y")
            }])

            df_actual = conn.read(worksheet="Data", ttl=0)
            df_final = pd.concat([df_actual, nuevo_registro], ignore_index=True)
            conn.update(worksheet="Data", data=df_final)

            st.success(f"✅ ¡Trabajo de {cliente.upper()} registrado!")
            st.balloons()
            
            # Botón de WhatsApp
            if celular:
                mensaje = f"Hola {cliente.upper()}, THE WARRIOR BROTHERS confirma la recepción de tu {articulo}. Total: ${total:.2f}, Abono: ${abono:.2f}, Saldo: ${saldo:.2f}. Entrega: {entrega.strftime('%d/%m/%Y')}."
                link_wa = f"https://wa.me/593{celular}?text={mensaje.replace(' ', '%20')}"
                st.link_button("📲 Enviar Recibo por WhatsApp", link_wa)

        except Exception as e:
            st.error(f"Hubo un detalle, mi rey: {e}")
    else:
        st.warning("⚠️ Nombre y Artículo son necesarios.")

# --- TABLA DE HISTORIAL ---
st.divider()
st.write("### 📋 Últimos 5 Registros")
try:
    df_vista = conn.read(worksheet="Data", ttl=0)
    st.dataframe(df_vista.tail(5), use_container_width=True)
except:
    st.info("Cargando datos...")
