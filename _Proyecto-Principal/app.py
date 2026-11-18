
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar resultados del framework
df_results = pd.read_csv('resultados_anomalias.csv')

st.title("Framework de Detección de Anomalías Institucionales")
st.subheader("Auditoría Inteligente mediante Deep Autoencoders")

# Motor de Analítica Prescriptiva
st.markdown("### Registros Críticos Identificados")
df_anomalias = df_results[df_results['Is_Anomaly'] == True]
st.dataframe(df_anomalias)

# Visualización
fig = px.histogram(df_results, x="Reconstruction_Error", color="Is_Anomaly",
                   title="Distribución del Error de Reconstrucción", 
                   labels={"Reconstruction_Error": "Índice de Anomalía (MSE)"})
st.plotly_chart(fig)

st.markdown("### Recomendaciones Prescriptivas")
for index, row in df_anomalias.iterrows():
    st.warning(f"Auditar ID Estudiante {row.get('student_id', index)}: " 
               f"El perfil estadístico presenta una divergencia alta (Score: {row['Reconstruction_Error']:.4f}). "
               "Verifique la consistencia en el cruce de datos sociodemográficos contra notas.")
