import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "DIABETES": [1, 2, 1, 2, 2],
    "COPD": [1, 2, 2, 2, 1],
    "ASTHMA": [2, 1, 2, 1, 2],
    "INMUSUPR": [2, 2, 1, 1, 2],
    "HYPERTENSION": [1, 2, 1, 2, 1],
    "CARDIOVASCULAR": [1, 2, 1, 2, 2],
    "OBESITY": [2, 1, 2, 1, 2],
    "CHRONIC_KIDNEY": [2, 1, 2, 1, 2],
    "TOBACCO": [1, 2, 1, 1, 2],
    "OUTCOME": ['DECEASED', 'RECOVERED', 'DECEASED', 'RECOVERED', 'DECEASED']
})

st.title("Common Diseases Among Deceased Patients")

# Select outcome
selected_outcome = st.selectbox("Select Outcome", df["OUTCOME"].unique())

# Filter data based on selected outcome
filtered_df = df[df["OUTCOME"] == selected_outcome]

# Disease columns
disease_columns = ["DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION", "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY", "TOBACCO"]
disease_counts = filtered_df[disease_columns].sum()

plt.figure(figsize=(10, 6))
disease_counts.sort_values(ascending=True).plot(kind='bar', color='lightcoral')
plt.xlabel('Diseases')
plt.ylabel('Number of Patients')
plt.title(f'Common Diseases Among {selected_outcome} Patients')
plt.tight_layout()

st.pyplot(plt)