import pandas as pd
import plotly.graph_objects as go
import streamlit as st


df = pd.DataFrame({
    "DIABETES": ['YES', 'NO', 'YES', 'NO', 'YES'],
    "COPD": ['NO', 'YES', 'NO', 'YES', 'NO'],
    "ASTHMA": ['YES', 'NO', 'YES', 'NO', 'YES'],
    "INMUSUPR": ['YES', 'NO', 'NO', 'YES', 'YES'],
    "HYPERTENSION": ['NO', 'YES', 'NO', 'YES', 'NO'],
    "CARDIOVASCULAR": ['YES', 'NO', 'YES', 'NO', 'YES'],
    "OBESITY": ['NO', 'YES', 'NO', 'YES', 'NO'],
    "CHRONIC_KIDNEY": ['YES', 'NO', 'YES', 'NO', 'YES'],
    "TOBACCO": ['NO', 'YES', 'NO', 'YES', 'NO'],
    "ICU": ['YES', 'NO', 'UNKNOWN', 'YES', 'NO'],
})


analysis = df.copy()


disease_columns = [
    "DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION", "CARDIOVASCULAR", 
    "OBESITY", "CHRONIC_KIDNEY", "TOBACCO", "ICU"
]


mappings = {
    "YES": 1,
    "NO": 2,
    "UNKNOWN": 99
}


for col in disease_columns:
    analysis[col] = analysis[col].map(mappings)


analysis_clean = analysis.dropna(subset=disease_columns)


correlation_matrix = analysis_clean[disease_columns].corr()


st.title("Interactive Correlation Between Diseases and ICU Admission")


fig = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='RdBu',  
    colorbar=dict(title='Correlation'),
    hovertemplate="Correlation: %{z}<br>From: %{x}<br>To: %{y}",
))

fig.update_layout(
    title="Correlation Matrix",
    xaxis_title="Diseases",
    yaxis_title="Diseases",
    hovermode="closest",
)

st.plotly_chart(fig)