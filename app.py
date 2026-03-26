import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse
import pytz

# --- 1. CONFIGURACIÓN ---
st.set_page_config(
    page_title="SISTEMA DE RECIBOS - WARRIOR BROTHERS",
    page_icon="👞",
    layout="wide"
)

zona_ec = pytz.timezone('America/Guayaquil')
hoy_ecuador = datetime.now(zona_ec).date()

# --- 2. SEGURIDAD ---
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.title("🔐 Acceso Privado")
    password = st.text_input("Ingresa la contraseña:", type="password")
    if st.button("Entrar"):
        if password == "WARRIOR2026":
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta.")
    st.stop()

# --- 3. MEMORIA DE LA SESIÓN (Evita el error de Google Sheets) ---
if "historial" not in st.session_state:
    st.session_state["historial"] = pd.DataFrame(columns=[
        "Fecha", "Cliente", "Articulo", "Reparacion", "Total", "Abono", "Saldo", "Entrega"
    ])

# --- 4. DISEÑO ---
st.markdown(
    """
    <div style='display: flex; align-items: center; justify-content: center; gap: 15px;'>
        <h1 style='margin: 0;'>🛡️ THE WARRIOR BROTHERS</h1>
    </div>
    <h3 style='text-align: center; color: #888; margin-top: 5px;'>Control de Órdenes y Recibos</h3>
    <br>
    """,
    unsafe_allow_html=True
)

# --- 5. FORMULARIO ---
with st.form("form_warrior", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("👤 Cliente:")
        celular = st.text_input("📱 WhatsApp (ej: 099...):")
        articulo = st.text_input("💼 Tipo de Artículo:")
    with col2:
        reparacion = st.text_input("🛠️ Reparación a realizar:")
        total = st.number_input("💰 Total ($):", min_value=0.0, format="%.2f")
        abono = st.number_input("💵 Abono ($):", min_value=0.0, format="%.2f")
        fecha_entrega = st.date_input("📅 Fecha de entrega:", value=hoy_ecuador)
    
    submit = st.form_submit_button("💾 GENERAR RECIBO")

if submit:
    if nombre and celular:
        saldo = total - abono
        ahora = datetime.now(zona_ec)
        f_h = ahora.strftime("%d/%m/%Y %H:%M")
        f_e = fecha_entrega.strftime("%d/%m/%Y")

        # Guardar en la tabla local para que no se pierda en la vista actual
        nueva_fila = pd.DataFrame([{
            "Fecha": f_h, "Cliente": nombre.upper(), "Articulo": articulo,
            "Reparacion": reparacion, "Total": f"{total:.2f}",
            "Abono": f"{abono:.2f}", "Saldo": f"{saldo:.2f}", "Entrega": f_e
        }])
        st.session_state["historial"] = pd.concat([nueva_fila, st.session_state["historial"]], ignore_index=True)

        # --- MENSAJE DE WHATSAPP ---
        msg_wa = (
            f"👞🔨 *THE WARRIOR BROTHERS*\n"
            f"¡Hola *{nombre.upper()}*! ✅\n"
            f"Recibimos su *{articulo.lower()}* para: {reparacion}\n\n"
            f"💰 *Total:* ${total:.2f}\n"
            f"💵 *Abono:* ${abono:.2f}\n"
            f"💳 *Saldo:* *${saldo:.2f}*\n"
            f"📅 *Entrega:* {f_e}\n\n"
            f"¡Gracias por su confianza! ✨"
        )
        
        texto_url = urllib.parse.quote(msg_wa)
        link_wa = f"https://api.whatsapp.com/send?phone=593{celular.lstrip('0')}&text={texto_url}"

        st.success("✅ Datos procesados correctamente.")
        st.markdown(f"""
            <a href="{link_wa}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; font-size:18px;">
                    📲 ENVIAR RECIBO POR WHATSAPP
                </div>
            </a>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ Nombre y Celular son obligatorios.")

# --- 6. TABLA DE CONTROL ---
st.divider()
st.subheader("📋 Trabajos de hoy")
st.dataframe(st.session_state["historial"], use_container_width=True)
