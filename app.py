import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="FM24 Advisor - Real Jaén", layout="wide")

# Configuración de la IA
st.sidebar.title("Configuración")
api_key = st.sidebar.text_input("Introduce tu Google API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.title("⚽ Real Jaén: Analista Táctico")
    
    tab1, tab2, tab3 = st.tabs(["Análisis de Plantilla", "Estrategia ABP", "Manual de Gestión"])

    with tab1:
        st.subheader("📋 Diagnóstico de Plantilla")
        datos = st.text_area("Pega aquí los datos de tus jugadores (de FM24 o Excel):")
        if st.button("Analizar Mercado"):
            prompt = f"Actúa como analista de FM24. Según estos datos: {datos}, dime a quién vender (especialmente si cobran mucho y son +30 años) y qué puestos reforzar para Tercera RFEF."
            response = model.generate_content(prompt)
            st.markdown(response.text)

    with tab2:
        st.subheader("🎯 Pizarra de Balón Parado")
        if st.button("Generar Táctica ABP"):
            prompt = "Genera una rutina de córners y faltas para FM24 enfocada en un equipo con centrales lentos pero delanteros altos. Dame instrucciones para copiar al juego."
            response = model.generate_content(prompt)
            st.write(response.text)

    with tab3:
        st.info("Aquí puedes pegar el texto de tu Manual Técnico para que la IA lo use siempre como referencia.")
        manual = st.text_area("Contenido del Manual:")
else:
    st.warning("Por favor, introduce tu API Key en la barra lateral para empezar.")
