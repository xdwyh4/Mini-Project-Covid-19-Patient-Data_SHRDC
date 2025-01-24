import streamlit as st
import pandas as pd
import plotly.express as px


# Pre-load CSV data (replace 'datacovid.csv' with your actual CSV file)
df = pd.read_csv('dataset.csv')

# Ensure 'Date Admission' column is in datetime format
df['ADMISSION DATE'] = pd.to_datetime(df['ADMISSION DATE'])

pre_chosen_categories = ['ORIGIN', 'PNEUMONIA', 'SEX', 'HOSPITALIZED', 'INTUBATED']

# Allow user to choose one of the pre-chosen categories
chosen_category = st.selectbox("Select a category to display in the line chart", pre_chosen_categories)

# Summarize data for the chosen category
summarized_data = df.groupby('ADMISSION DATE')[chosen_category].value_counts().unstack().fillna(0)
summarized_data = summarized_data.reset_index()

# Create line chart
fig = px.line(summarized_data, x='ADMISSION DATE', y=summarized_data.columns[1:], title=f'Line Chart of {chosen_category} Over Time')

# Display line chart
st.plotly_chart(fig)

# Display dataframe
st.write(df)