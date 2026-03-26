import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse
import pytz
import sqlite3

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="THE WARRIOR BROTHERS PRO", page_icon="👞", layout="wide")
zona_ec = pytz.timezone('America/Guayaquil')

# Inicializar Base de Datos Local
def init_db():
    conn = sqlite3.connect('warrior_pro.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS recibos 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  fecha TEXT, cliente TEXT, celular TEXT,
                  articulo TEXT, reparacion TEXT, total REAL, 
                  abono REAL, saldo REAL, entrega TEXT)''')
    conn.commit()
    conn.close()

init_db()

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
        else:
            st.error("Contraseña incorrecta.")
    st.stop()

# --- 3. DISEÑO DE INTERFAZ ---
st.markdown("<h1 style='text-align: center;'>🛡️ THE WARRIOR BROTHERS</h1>", unsafe_allow_html=True)

tab_registro, tab_historial = st.tabs(["📝 REGISTRAR TRABAJO", "📊 CAJA Y CONTROL"])

# --- PESTAÑA 1: REGISTRO ---
with tab_registro:
    with st.form("form_registro", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("👤 Cliente:")
            celular = st.text_input("📱 WhatsApp:")
            articulo = st.text_input("💼 Artículo:")
        with col2:
            reparacion = st.text_input("🛠️ Reparación:")
            total = st.number_input("💰 Total ($):", min_value=0.0, format="%.2f")
            abono = st.number_input("💵 Abono ($):", min_value=0.0, format="%.2f")
            fecha_entrega = st.date_input("📅 Fecha de entrega:")
            
        submit = st.form_submit_button("💾 GUARDAR Y GENERAR")

    if submit:
        if nombre and celular:
            saldo = total - abono
            f_registro = datetime.now(zona_ec).strftime("%d/%m/%Y %H:%M")
            f_entrega = fecha_entrega.strftime("%d/%m/%Y")
            
            conn = sqlite3.connect('warrior_pro.db')
            c = conn.cursor()
            c.execute("""INSERT INTO recibos (fecha, cliente, celular, articulo, reparacion, total, abono, saldo, entrega) 
                         VALUES (?,?,?,?,?,?,?,?,?)""", 
                      (f_registro, nombre.upper(), celular, articulo, reparacion, total, abono, saldo, f_entrega))
            conn.commit()
            conn.close()
            
            st.success(f"✅ ¡Trabajo de {nombre.upper()} registrado!")
            
            msg = f"👞🔨 *THE WARRIOR BROTHERS*\n¡Hola {nombre.upper()}!\nSaldo: ${saldo:.2f}\nEntrega: {f_entrega}"
            link = f"https://api.whatsapp.com/send?phone=593{celular.lstrip('0')}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">📲 ENVIAR POR WHATSAPP</div></a>', unsafe_allow_html=True)

# --- PESTAÑA 2: HISTORIAL Y BORRADO ---
with tab_historial:
    conn = sqlite3.connect('warrior_pro.db')
    df = pd.read_sql_query("SELECT * FROM recibos ORDER BY id DESC", conn)
    conn.close()

    if not df.empty:
        # Métricas
        m1, m2, m3 = st.columns(3)
        m1.metric("Ingreso Total", f"${df['total'].sum():.2f}")
        m2.metric("Caja (Abonos)", f"${df['abono'].sum():.2f}")
        m3.metric("Por Cobrar", f"${df['saldo'].sum():.2f}")
        
        st.divider()
        st.dataframe(df, use_container_width=True)
        
        # --- SECCIÓN DE LIMPIEZA PARA PRUEBAS ---
        st.sidebar.divider()
        st.sidebar.warning("⚙️ ZONA DE MANTENIMIENTO")
        confirmar_borrado = st.sidebar.checkbox("Confirmar que quiero borrar todo")
        
        if st.sidebar.button("🗑️ BORRAR TODA LA BASE DE DATOS"):
            if confirmar_borrado:
                conn = sqlite3.connect('warrior_pro.db')
                c = conn.cursor()
                c.execute("DELETE FROM recibos") # Esto vacía la tabla
                conn.commit()
                conn.close()
                st.sidebar.success("Base de datos limpiada. Reiniciando...")
                st.rerun()
            else:
                st.sidebar.error("⚠️ Primero marca la casilla de confirmación.")
    else:
        st.info("No hay registros todavía.")
