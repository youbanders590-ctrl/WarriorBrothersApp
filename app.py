import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse
import pytz
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="💪")
zona_ec = pytz.timezone('America/Guayaquil')

# --- INTERFAZ ---
st.title("🛡️ Sistema The Warrior Brothers")

with st.form("formulario_cliente", clear_on_submit=True):
    st.subheader("Nuevo Registro de Trabajo")
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre del Cliente:")
        celular = st.text_input("Celular (ej: 099...)")
        articulo = st.text_input("Artículo:")
    with col2:
        trabajo = st.text_input("Reparación:")
        precio_total = st.number_input("Precio Total ($)", min_value=0.0)
        abono = st.number_input("Abono Inicial ($)", min_value=0.0)
        dias_entrega = st.number_input("Días entrega", min_value=1, value=2)

    submit = st.form_submit_button("📄 Generar Recibo y Guardar")

if submit:
    if nombre and celular:
        # CÁLCULOS
        saldo = precio_total - abono
        ahora = datetime.now(zona_ec)
        f_entrega = (ahora + timedelta(days=dias_entrega)).strftime("%d/%m/%Y")
        
        # 1. GUARDAR EN GOOGLE SHEETS
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df_existente = conn.read()
            nueva_fila = pd.DataFrame([{
                "Fecha": ahora.strftime("%Y-%m-%d %H:%M"),
                "Cliente": nombre.upper(),
                "Celular": celular,
                "Artículo": articulo,
                "Trabajo": trabajo,
                "Total": precio_total,
                "Abono": abono,
                "Saldo": saldo,
                "Fecha_Entrega": f_entrega
            }])
            df_final = pd.concat([df_existente, nueva_fila], ignore_index=True)
            conn.update(data=df_final)
            st.success("✅ ¡Guardado en Excel!")
        except Exception as e:
            st.error(f"Error al guardar: {e}")

        # 2. BOTÓN DE WHATSAPP
        mensaje = f"Hola *{nombre.upper()}*, de *THE WARRIOR BROTHERS* 🛡️. Recibimos su *{articulo}* para *{trabajo}*. Total: ${precio_total} | Abono: ${abono} | Saldo: ${saldo} | Entrega: {f_entrega}"
        link_wa = f"https://wa.me/593{celular.lstrip('0')}?text={urllib.parse.quote(mensaje)}"
        st.markdown(f'''<a href="{link_wa}" target="_blank"><button style="background-color: #25D366; color: white; padding: 15px; border: none; border-radius: 10px; width: 100%; cursor: pointer; font-weight: bold;">📲 ENVIAR A WHATSAPP</button></a>''', unsafe_allow_html=True)
