

# dashboard_nps.py

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard NPS", layout="wide")
st.title("📊 Dashboard NPS – Clientes PJ")

uploaded_file = st.file_uploader("Selecione o arquivo CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, sep=';', encoding='latin1')
    df.columns = df.columns.str.strip().str.replace('�', 'ç').str.replace(' ', '_')

    df['Safra'] = pd.to_datetime(df['Safra'].astype(str), format='%Y%m')
    df['Safra_Formatada'] = df['Safra'].dt.strftime('%b/%Y')

    tipo = st.selectbox("Filtrar por tipo de cliente", ["Todos", "PROMOTOR", "NEUTRO", "DETRATOR"])
    if tipo != "Todos":
        df = df[df['Classificação_NPS'] == tipo]

    nps_counts = df.groupby(['Safra_Formatada', 'Classificação_NPS']).size().unstack(fill_value=0)
    nps_counts['Total'] = nps_counts.sum(axis=1)
    nps_counts['NPS'] = ((nps_counts.get('PROMOTOR', 0) - nps_counts.get('DETRATOR', 0)) / nps_counts['Total']) * 100
    nps_counts = nps_counts.sort_index(key=lambda x: pd.to_datetime(x, format='%b/%Y'))

    st.subheader("📈 Evolução do NPS por Safra")
    st.line_chart(nps_counts['NPS'])

    st.subheader("📌 Temas mais citados nos comentários")
    temas = df[df['Houve_Comentário'] == 'Sim']['Tema_Comentário'].value_counts().head(10)
    st.bar_chart(temas)

    st.subheader("🗣️ Comentários dos clientes")
    st.dataframe(df[df['Houve_Comentário'] == 'Sim'][['Safra_Formatada', 'Classificação_NPS', 'Tema_Comentário', 'Teor_Comentário']])
