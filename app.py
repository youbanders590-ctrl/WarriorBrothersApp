import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse
import pytz
import sqlite3

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="THE WARRIOR BROTHERS PRO", page_icon="👞", layout="wide")
zona_ec = pytz.timezone('America/Guayaquil')

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

if not st.session_state["autenticado"] or "autenticado" not in st.session_state:
    st.title("🔐 Acceso Privado")
    password = st.text_input("Contraseña:", type="password")
    if st.button("Entrar"):
        if password == "WARRIOR2026":
            st.session_state["autenticado"] = True
            st.rerun()
    st.stop()

# --- 3. DISEÑO ---
st.markdown("<h1 style='text-align: center;'>🛡️ THE WARRIOR BROTHERS</h1>", unsafe_allow_html=True)

tab_registro, tab_historial = st.tabs(["📝 REGISTRAR TRABAJO", "📊 CAJA Y CONTROL"])

# --- PESTAÑA 1: REGISTRO (Sin cambios) ---
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
            st.rerun()

# --- PESTAÑA 2: HISTORIAL CON SELECCIÓN VISUAL ---
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
        st.subheader("🗂️ Registro de Trabajos")

        # 1. Creamos una columna temporal de Checkbox en la tabla
        df.insert(0, "Seleccionar", False)

        # 2. Usamos el editor de datos para que el usuario marque los que quiere borrar
        df_editado = st.data_editor(
            df,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Seleccionar": st.column_config.CheckboxColumn(
                    "❌ Borrar",
                    help="Marca para eliminar",
                    default=False,
                )
            },
            disabled=["id", "fecha", "cliente", "celular", "articulo", "reparacion", "total", "abono", "saldo", "entrega"]
        )

        # 3. Botón para ejecutar el borrado de los seleccionados
        filas_seleccionadas = df_editado[df_editado["Seleccionar"] == True]
        
        if not filas_seleccionadas.empty:
            if st.button(f"🗑️ ELIMINAR {len(filas_seleccionadas)} REGISTRO(S) SELECCIONADO(S)", type="primary"):
                ids_a_borrar = filas_seleccionadas["id"].tolist()
                
                conn = sqlite3.connect('warrior_pro.db')
                c = conn.cursor()
                for id_b in ids_a_borrar:
                    c.execute("DELETE FROM recibos WHERE id=?", (id_b,))
                conn.commit()
                conn.close()
                
                st.success("Registros eliminados.")
                st.rerun()
    else:
        st.info("No hay registros todavía.")
