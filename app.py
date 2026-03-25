import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="The Warrior Brothers", layout="centered", page_icon="🛡️")

# --- ESTILO PARA CENTRAR TODO ---
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        text-align: center;
    }
    .stImage {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_key_url=True)

# --- LOGO PEQUEÑO Y CENTRADO ---
logo_url = "https://raw.githubusercontent.com/mikekrieger79/warriorbrothersapp/main/logo.png"

# Creamos columnas para forzar el centro del logo
col_izq, col_centro, col_der = st.columns([2, 1, 2])
with col_centro:
    try:
        st.image(logo_url, width=80) # Logo pequeño como pediste
    except:
        st.write("🛡️")

st.header("THE WARRIOR BROTHERS")
st.caption("Zapatería y Restauración de Cuero")
st.divider()

# --- CONEXIÓN A GOOGLE SHEETS ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- FECHA AUTOMÁTICA ---
ahora = datetime.now()
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M")

# --- FORMULARIO DE REGISTRO ---
# El formulario mantiene el orden pero con un diseño limpio
with st.form("registro_trabajo", clear_on_submit=True):
    st.markdown(f"📅 **Fecha de Ingreso:** `{fecha_formateada}`")
    
    cliente = st.text_input("👤 Nombre del Cliente:").strip()
    celular = st.text_input("📱 WhatsApp (sin el 0):")
    articulo = st.text_input("👞 Artículo (Ej: Botas, Bolso):")
    reparacion = st.text_area("🛠️ Detalle de la Reparación:")
    
    c1, c2 = st.columns(2)
    with c1:
        total = st.number_input("💰 Valor Total $", min_value=0.0, step=0.5)
    with c2:
        abono = st.number_input("💵 Abono Inicial $", min_value=0.0, step=0.5)
    
    saldo = total - abono
    st.subheader(f"Saldo Pendiente: ${saldo:.2f}")
    
    entrega = st.date_input("📆 Fecha de Entrega Prometida")

    submit = st.form_submit_button("💾 GUARDAR EN REGISTRO")

# --- LÓGICA DE GUARDADO ---
if submit:
    if cliente and articulo:
        try:
            nuevo_registro = pd.DataFrame([{
                "Fecha": fecha_formateada,
                "Cliente": cliente.upper(),
                "Celular": str(celular),
                "Articulo": articulo.lower(),
                "Reparacion": reparacion.lower(),
                "Total": float(total),
                "Abono": float(abono),
                "Saldo": float(saldo),
                "Entrega": entrega.strftime("%d/%m/%Y")
            }])

            # Leer datos actuales, pegar el nuevo y subir
            df_actual = conn.read(worksheet="Data", ttl=0)
            df_final = pd.concat([df_actual, nuevo_registro], ignore_index=True)
            conn.update(worksheet="Data", data=df_final)

            st.success(f"✅ ¡Trabajo de {cliente} registrado!")
            st.balloons()
            
            # Botón de WhatsApp para el recibo
            mensaje_wa = f"Hola {cliente.upper()}, THE WARRIOR BROTHERS confirma la recepción de tu {articulo}. Total: ${total}, Abono: ${abono}, Saldo: ${saldo}. Entrega: {entrega.strftime('%d/%m/%Y')}."
            link_wa = f"https://wa.me/593{celular}?text={mensaje_wa.replace(' ', '%20')}"
            st.link_button("📲 Enviar Recibo por WhatsApp", link_wa)

        except Exception as e:
            st.error(f"Hubo un detalle al guardar, mi rey: {e}")
    else:
        st.warning("⚠️ El nombre y el artículo son obligatorios.")

# --- TABLA DE CONTROL ---
st.divider()
st.write("### 📋 Últimos Registros")
try:
    df_vista = conn.read(worksheet="Data", ttl=0)
    st.dataframe(df_vista.tail(5), use_container_width=True)
except:
    st.info("Conectando con la base de datos...")
