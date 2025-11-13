import streamlit as st
# import os # Ya no es necesario

# --- Configuración de la Página ---
# Usamos layout="wide" para aprovechar mejor el espacio para las imágenes
st.set_page_config(
    page_title="Tutorial de Conexión a CCAD",
    page_icon="🖥️",
    layout="wide"
)

# --- INYECCIÓN DE CSS PERSONALIZADO ---
# (Se mantiene el mismo CSS de antes)
custom_css = """
<style>
    /* 1. Importar Fuentes de Google */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&family=Lato:wght@400;700&display=swap');
    
    /* 2. Fuente Global (Cuerpo de Texto) */
    .stApp {
        font-family: 'Lato', sans-serif;
    }

    /* 3. Títulos (st.title, st.header, st.subheader) */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        color: #1e293b; /* Color de texto oscuro (Slate 900) */
    }

    /* 4. Color del Cuerpo de Texto */
    .stMarkdown p, .stMarkdown li {
        color: #475569; /* Color de texto gris (Slate 600) */
        font-size: 1.05rem; /* Ligeramente más grande para legibilidad */
        line-height: 1.6;
    }

    /* 5. Estilo para 'st.info' (Prerrequisitos) */
    .stAlert[data-baseweb="alert"] {
        background-color: #eef2ff; /* Fondo claro (Indigo 50) */
        border-radius: 8px; /* Bordes redondeados */
        border: 1px solid #c7d2fe; /* Borde sutil */
    }
    .stAlert[data-baseweb="alert"] .stMarkdown p {
        color: #312e81; /* Texto índigo oscuro */
    }

    /* 6. Estilo para 'st.expander' (Pasos de MobaXterm) */
    .stExpander {
        border-radius: 8px !important;
        border: 1px solid #e2e8f0 !important; /* Borde claro (Slate 200) */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); /* Sombra sutil */
    }
    .stExpander header {
        background-color: #f8fafc; /* Fondo de cabecera (Slate 50) */
        border-radius: 8px 8px 0 0 !important;
    }
    .stExpander header p {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #334155; /* Color de cabecera (Slate 700) */
    }

    /* 7. Estilo para Bloques de Código (st.code) */
    .stCodeBlock {
        background-color: #eef2ff !important; /* Fondo claro (Indigo 50) */
        border-radius: 8px;
    }
    .stCodeBlock code {
        font-family: 'Courier New', Courier, monospace;
        color: #4f46e5; /* Color de acento (Indigo 600) */
        font-size: 0.95rem;
    }

    /* 8. Estilo para Imágenes (st.image) */
    .stImage img {
        border-radius: 12px; /* Coincide con .image-wrapper */
        border: 1px solid #e2e8f0; /* Borde sutil */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.07);
    }
    
    /* 9. Estilo para Pestañas (st.tabs) */
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 2px solid #e2e8f0; /* Borde inferior de la lista de pestañas */
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #64748b; /* Color de pestaña inactiva */
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        border-bottom-color: #4f46e5; /* Color de acento */
        color: #4f46e5;
    }

    /* 10. Estilo para Botón de Enlace (st.link_button) */
    .stLinkButton a {
        background-color: #4f46e5;
        color: #ffffff;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 700;
        font-family: 'Poppins', sans-serif;
        transition: background-color 0.3s ease;
    }
    .stLinkButton a:hover {
        background-color: #312e81; /* Color más oscuro al pasar el mouse */
        color: #ffffff;
        text-decoration: none;
    }
    
    /* 11. Estilo para st.success */
    .st-emotion-cache-1jicfl2 {
        background-color: #f0fdf4; /* Verde muy claro */
        border-color: #22c55e; /* Borde verde */
        border-radius: 8px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- FIN DE CSS PERSONALIZADO ---

# --- ENLACES DE IMÁGENES (REEMPLAZAR) ---
# Sube tus imágenes a Imgur (https://imgur.com), haz clic derecho,
# "Copiar dirección de la imagen" y pégala aquí.
# El enlace debe terminar en .png, .jpg, etc.

URL_PASO1_WIKI = "https://i.imgur.com/yI8PBBl.png"
URL_PASO2_ACCESO = "https://i.imgur.com/eIk4lJw.png"
URL_PASO3_SSH = "https://i.imgur.com/emV0D7e.png"
URL_MOBA1_SESSION = "https://i.imgur.com/VSSCDHf.png"
URL_MOBA2_SSH_DIALOG = "https://i.imgur.com/4nSRIWF.png"
URL_MOBA3_HOST = "https://i.imgur.com/aAnybh5.png"
URL_MOBA4_NEW_PASS = "https://i.imgur.com/GK2L8zY.png"
URL_MOBA5_FILL_PASS = "https://i.imgur.com/L3NQMO1.png"
URL_MOBA6_FINISH_CONFIG = "https://i.imgur.com/O4eLCAX.png"
URL_MOBA7_SUCCESS = "https://i.imgur.com/m99s2db.png"

# --- FIN DE ENLACES DE IMÁGENES ---


# --- Título e Introducción ---
st.title("🖥️ Tutorial: Conexión a CCAD")
st.subheader("Guía paso a paso para acceder al clúster de supercómputo")

st.info("Este tutorial asume que usted ya ha solicitado y recibido sus credenciales de acceso (usuario y contraseña) por parte del equipo de CCAD.")

# --- SECCIÓN: Explicación sobre las imágenes (MODIFICADA) ---
st.warning("""
**¡Atención!**
Esta aplicación usa imágenes de ejemplo. Para ver tus propias capturas de pantalla, 
debes subirlas a un servicio como [Imgur](https://imgur.com) y pegar las URLs 
en las variables (ej: `URL_PASO1_WIKI`) al inicio de este script `app.py`.
""")
# --- FIN SECCIÓN ---

st.divider()

# --- Sección 1: Encontrar la Documentación ---
st.header("1. Localizar la Documentación")
st.markdown("El primer paso es consultar la documentación oficial en el sitio web de Supercómputo.")

col1, col2 = st.columns(2)

# Ya no se usa la función helper, se llama a st.image directamente
with col1:
    st.markdown("#### Paso 1.1: Ir a la Wiki")
    st.markdown("Ingrese a **supercomputo.unc.edu.ar** y busque el enlace a **\"Wiki y tutoriales\"**.")
    # Ruta de imagen con URL
    st.image(URL_PASO1_WIKI, caption="Página de inicio. Clic en 'Wiki y tutoriales'.")

with col2:
    st.markdown("#### Paso 1.2: Navegar a 'Acceso'")
    st.markdown("Una vez en la wiki, busque la sección de **\"Primeros pasos\"** y haga clic en **\"Acceso\"**.")
    # Ruta de imagen con URL
    st.image(URL_PASO2_ACCESO, caption="Menú de la Wiki. Clic en 'Acceso'.")

st.divider()

# --- Sección 2: Métodos de Conexión ---
st.header("2. Métodos de Conexión")
st.markdown("La documentación muestra las dos formas principales de conexión.")

# Usamos pestañas para separar las guías de Linux/Mac y Windows
tab_linux, tab_windows = st.tabs(["🐧 Conexión desde Linux / Mac", "🪟 Conexión desde Windows (MobaXterm)"])

# --- Pestaña de Linux / Mac ---
with tab_linux:
    st.subheader("Método por Terminal (Linux/Mac)")
    st.markdown("""
    Casi todas las distribuciones de Linux y macOS ya incluyen un cliente SSH preinstalado. 
    Puede conectarse abriendo una **Terminal** y ejecutando el comando:
    """)
    
    st.code("ssh $USUARIO@serafin.ccad.unc.edu.ar", language="bash")
    
    st.markdown("O para los otros clústeres disponibles:")
    
    st.code("""
ssh $USUARIO@mendieta.ccad.unc.edu.ar
ssh $USUARIO@eulogia.ccad.unc.edu.ar
ssh $USUARIO@mulatona.ccad.unc.edu.ar
ssh $USUARIO@nabucodonosor.ccad.unc.edu.ar
    """, language="bash")
    
    st.markdown("La variable `$USUARIO` es su nombre de usuario comunicado en el mail de confirmación.")
    
    # Ruta de imagen con URL
    st.image(URL_PASO3_SSH, caption="Ejemplo de la documentación para conexión SSH.")

# --- Pestaña de Windows ---
with tab_windows:
    st.subheader("Guía con MobaXterm (Windows)")
    st.markdown("Para Windows, la documentación recomienda usar el cliente **MobaXterm**.")
    st.link_button("Descargar MobaXterm", "https://mobaxterm.mobatek.net/download.html")
    
    st.markdown("---")
    st.markdown("Siga estos pasos para configurar su conexión:")

    # Usamos expanders para cada paso, para que la guía sea fácil de seguir
    with st.expander("Paso 1: Iniciar una nueva sesión", expanded=True):
        st.markdown("Abra MobaXterm. En la esquina superior izquierda, haga clic en el botón **'Session'**.")
        # Ruta de imagen con URL
        st.image(URL_MOBA1_SESSION, caption="Clic en 'Session' para empezar.")

    with st.expander("Paso 2: Seleccionar el tipo de sesión SSH"):
        st.markdown("En la ventana de 'Session settings', seleccione **'SSH'** como su tipo de sesión. Es la primera opción.")
        # Ruta de imagen con URL
        st.image(URL_MOBA2_SSH_DIALOG, caption="Seleccionar 'SSH'.")

    with st.expander("Paso 3: Configurar Host y Credenciales"):
        st.markdown("1.  En **'Remote host'**, ingrese la dirección del clúster (ej: `nabucodonosor.ccad.unc.edu.ar`).")
        st.markdown("2.  Haga clic en el **ícono de usuario** con un '+' (a la derecha de 'Specify username') para agregar sus credenciales.")
        # Ruta de imagen con URL
        st.image(URL_MOBA3_HOST, caption="Ingresar Host y hacer clic en el ícono de usuario.")
        
        st.markdown("3.  En la ventana de 'MobaXterm passwords', haga clic en **'New'**.")
        # Ruta de imagen con URL
        st.image(URL_MOBA4_NEW_PASS, caption="Clic en 'New' para agregar una nueva credencial.")
        
        st.markdown("4.  Complete los campos: **Name** (un nombre para recordarlo, ej: 'CCAD Felipe'), su **Username** y **Password** provistos por CCAD. Clic en 'OK'.")
        # Ruta de imagen con URL
        st.image(URL_MOBA5_FILL_PASS, caption="Completar los datos de la credencial.")

    with st.expander("Paso 4: Finalizar Configuración y Conectar"):
        st.markdown("1.  De vuelta en 'Session settings', marque la casilla **'Specify username'**.")
        st.markdown("2.  Seleccione la credencial que acaba de crear en el menú desplegable.")
        st.markdown("3.  Haga clic en **'OK'** para iniciar la sesión.")
        # Ruta de imagen con URL
        st.image(URL_MOBA6_FINISH_CONFIG, caption="Seleccionar la credencial guardada y hacer clic en 'OK'.")

    with st.expander("Paso 5: ¡Conexión Exitosa!"):
        st.markdown("Si todos los pasos son correctos, la sesión se iniciará y verá la terminal de bienvenida del clúster, lista para recibir sus comandos.")
        # Ruta de imagen con URL
        st.image(URL_MOBA7_SUCCESS, caption="Terminal de bienvenida del clúster de CCAD.")

st.divider()

# --- Sección Final ---
st.header("3. ¿Preguntas?")
st.success("¡Felicidades! Si llegó hasta aquí, ya está conectado al clúster.")
st.markdown("Para más ayuda, consulte la wiki oficial o contacte a soporte de CCAD a través de [supercomputo.unc.edu.ar](https://supercomputo.unc.edu.ar).")

st.balloons()

