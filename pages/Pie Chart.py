
import streamlit as st
import pandas as pd
import plotly.express as px


# Pre-load CSV data (replace 'your_data.csv' with your actual CSV file)
df = pd.read_csv('dataset.csv')

# Pre-chosen categories
pre_chosen_categories = ['ORIGIN', 'PNEUMONIA', 'SEX', 'HOSPITALIZED', 'INTUBATED']

# Allow user to choose one of the pre-chosen categories
chosen_category = st.selectbox("Select a category to display in the chart", pre_chosen_categories)

# Allow user to choose the chart type
chart_type = st.radio("Select Chart Type", ['Pie Chart', 'Line Chart'])

# Summarize data for the chosen category
summarized_data = df[chosen_category].value_counts().reset_index()
summarized_data.columns = ['Category', 'Value']

# Display the chosen chart
if chart_type == 'Pie Chart':
    fig = px.pie(summarized_data, names='Category', values='Value', title=f'Pie Chart of {chosen_category}')
    st.plotly_chart(fig)
else:
    # For the line chart, show the cumulative distribution or count over categories
    summarized_data.sort_values(by='Category', inplace=True)
    fig = px.line(summarized_data, x='Category', y='Value', title=f'Line Chart of {chosen_category}')
    st.plotly_chart(fig)

# Display dataframe
st.write(df)
