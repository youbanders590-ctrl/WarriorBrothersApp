import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
import urllib.parse
import pytz

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="WARRIOR PRO", page_icon="👞", layout="wide")
zona_ec = pytz.timezone('America/Guayaquil')

# ENLACE DE TU DOCUMENTO (EL QUE ME PASASTE)
URL_SHEET = "https://docs.google.com/spreadsheets/d/1GsFe5PRkuY79IreHaW8VzYIogGe_o4N_Uf419u5LZJ8/edit?usp=sharing"

# Establecer conexión
conn = st.connection("gsheets", type=GSheetsConnection)

# --- 2. SEGURIDAD ---
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.title("🔐 Acceso Privado")
    password = st.text_input("Contraseña:", type="password")
    if st.button("Entrar"):
        if password == "WARRIOR2026":
            st.session_state["autenticado"] = True
            st.rerun()
    st.stop()

# --- 3. DISEÑO ---
st.markdown("<h1 style='text-align: center;'>🛡️ THE WARRIOR BROTHERS</h1>", unsafe_allow_html=True)

tab_reg, tab_hist = st.tabs(["📝 REGISTRAR TRABAJO", "📊 VER EXCEL ONLINE"])

# --- PESTAÑA 1: REGISTRO ---
with tab_reg:
    with st.form("f_reg", clear_on_submit=True):
        col1, col2 = st.columns(2)
        nombre = col1.text_input("👤 Cliente:")
        celular = col1.text_input("📱 WhatsApp (sin el 0):")
        articulo = col1.text_input("💼 Artículo:")
        reparacion = col2.text_input("🛠️ Reparación:")
        total = col2.number_input("💰 Total $", min_value=0.0)
        abono = col2.number_input("💵 Abono $", min_value=0.0)
        f_ent = col2.date_input("📅 Entrega:")
        
        submit = st.form_submit_button("🚀 GUARDAR EN LA NUBE")

    if submit:
        if nombre and articulo:
            saldo = total - abono
            fecha_hoy = datetime.now(zona_ec).strftime("%d/%m/%Y %H:%M")
            f_entrega_str = f_ent.strftime("%d/%m/%Y")
            
            try:
                # Leer datos actuales
                df_actual = conn.read(spreadsheet=URL_SHEET)
                
                # Nueva fila coincidiendo exactamente con tus encabezados de Google Sheets
                nueva_fila = pd.DataFrame([{
                    "Fecha": fecha_hoy,
                    "Cliente": nombre.upper(),
                    "celular": celular,
                    "articulo": articulo,
                    "reparacion": reparacion,
                    "total": total,
                    "abono": abono,
                    "saldo entrega": saldo,
                    "entrega": f_entrega_str
                }])
                
                # Unir y actualizar
                df_final = pd.concat([df_actual, nueva_fila], ignore_index=True)
                conn.update(spreadsheet=URL_SHEET, data=df_final)
                
                st.success(f"✅ ¡Trabajo de {nombre.upper()} guardado!")
                
                # Botón de WhatsApp
                msg = f"👞🔨 *THE WARRIOR BROTHERS*\n¡Hola {nombre.upper()}!\nRecibimos tu {articulo}.\nSaldo pendiente: ${saldo:.2f}\nEntrega estimada: {f_entrega_str}"
                link_wa = f"https://api.whatsapp.com/send?phone=593{celular.lstrip('0')}&text={urllib.parse.quote(msg)}"
                st.markdown(f'<a href="{link_wa}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:10px;border-radius:10px;text-align:center;font-weight:bold;">📲 NOTIFICAR POR WHATSAPP</div></a>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error: {e}. Asegúrate de que el Excel esté como 'Editor' en Compartir.")

# --- PESTAÑA 2: VISTA ---
with tab_hist:
    st.subheader("🌐 Registros en Google Sheets")
    if st.button("🔄 Actualizar Tabla"):
        st.rerun()
        
    try:
        # Volver a leer para mostrar lo último que hay en la nube
        df_vista = conn.read(spreadsheet=URL_SHEET)
        st.dataframe(df_vista, use_container_width=True, hide_index=True)
    except:
        st.warning("No se pudo cargar la tabla. Revisa el botón Compartir en Google Sheets.")
