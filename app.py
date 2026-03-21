import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse
import pytz
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Warrior Brothers Admin", page_icon="🛡️")
zona_ec = pytz.timezone('America/Guayaquil')

# --- SEGURIDAD ---
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

if not st.session_state["password_correct"]:
    st.title("🔐 Acceso Restringido")
    password = st.text_input("Contraseña:", type="password")
    if st.button("Entrar"):
        if password == "WARRIOR2026":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Clave incorrecta")
    st.stop()

# --- APP ---
st.title("🛡️ Los Hermanos Guerreros")

with st.form("formulario_calzado", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("👤 Nombre del Cliente:")
        celular = st.text_input("📱 Celular (WhatsApp):")
        zapato = st.text_input("👞 Tipo de Calzado:")
    with col2:
        reparacion = st.text_input("🛠️ Reparación:")
        total = st.number_input("💰 Total ($)", min_value=0.0)
        abono = st.number_input("💵 Abono ($)", min_value=0.0)
        dias = st.number_input("📅 Días entrega:", min_value=1, value=3)

    submit = st.form_submit_button("💾 REGISTRAR Y GUARDAR")

if submit:
    if nombre and celular:
        saldo = total - abono
        ahora = datetime.now(zona_ec)

        f_h = ahora.strftime("%d/%m/%Y %H:%M")
        f_e = (ahora + timedelta(days=dias)).strftime("%d/%m/%Y")

        # --- GUARDAR EN GOOGLE SHEETS (SOLUCIÓN DEFINITIVA) ---
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)

            nueva_fila = {
                "Fecha": f_h,
                "Cliente": nombre.upper(),
                "Celular": celular,
                "Calzado": zapato,
                "Reparacion": reparacion,
                "Total": float(total),
                "Abono": float(abono),
                "Saldo": float(saldo),
                "Entrega": f_e
            }

            conn.insert(worksheet="Hoja 1", data=nueva_fila)

            st.success("✅ Guardado correctamente en Google Sheets")

        except Exception as e:
            st.error(f"❌ Error al guardar: {e}")

        # --- LIMPIAR NÚMERO ---
        numero = celular.replace(" ", "").replace("-", "")

        if numero.startswith("0"):
            numero = "593" + numero[1:]
        else:
            numero = "593" + numero

        # --- MENSAJE WHATSAPP (EMOJIS CORRECTOS) ---
        mensaje = f"""🛡️ *THE WARRIOR BROTHERS*
------------------------------------------
👋 Hola *{nombre.upper()}*!
Confirmamos la recepción de su calzado:

👞 *Calzado:* {zapato}
🛠️ *Trabajo:* {reparacion}

------------------------------------------
💰 *Total:* ${total:.2f}
💵 *Abono:* ${abono:.2f}
💳 *Saldo pendiente:* *${saldo:.2f}*

------------------------------------------
📅 *Fecha de entrega:* {f_e}

✨ ¡Gracias por su confianza!
"""

        # 🔥 CORRECCIÓN CLAVE
        texto_final = urllib.parse.quote_plus(mensaje, encoding='utf-8')

        link_wa = f"https://wa.me/{numero}?text={texto_final}"

        st.markdown(f"""
        <a href="{link_wa}" target="_blank" style="
            background-color: #25D366;
            color: white;
            padding: 18px;
            text-align: center;
            display: block;
            border-radius: 12px;
            font-weight: bold;
            text-decoration: none;
            margin-top: 20px;">
            📲 ENVIAR COMPROBANTE POR WHATSAPP
        </a>
        """, unsafe_allow_html=True)

    else:
        st.error("❌ Llena los campos obligatorios.")
