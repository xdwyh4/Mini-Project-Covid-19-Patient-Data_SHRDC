import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    file_path = "dataset.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

st.title("Distribution of Cases by Gender & Age Group")

# Create age group bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

# Create age group column
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=age_bins, labels=age_labels, right=False)

# Map gender codes to labels
gender_map = {1: 'Male', 2: 'Female'}
df['SEX'] = df['SEX'].map(gender_map)

# Group data by age group and gender
gender_distribution = df['SEX'].value_counts()
age_group_distribution = df['AGE_GROUP'].value_counts().sort_index()

st.sidebar.subheader("Filter Options")
gender = st.sidebar.multiselect("Select Gender", ['Female', 'Male'], default=['Female', 'Male'])
age_group = st.sidebar.multiselect("Select Age Groups", age_labels, default=age_labels)

# Filter the data based on selections
filtered_gender_distribution = gender_distribution[gender]
filtered_age_group_distribution = age_group_distribution[age_group]

# Chart selection: Bar Chart for Gender or Line Chart for Age Group
chart_type = st.radio("Select Chart Type", ['Bar Chart (Gender)', 'Line Chart (Age Group)'])

fig, ax = plt.subplots(figsize=(10, 6))

if chart_type == 'Bar Chart (Gender)':
    filtered_gender_distribution.plot(kind='bar', color=['lightcoral', 'lightblue'], ax=ax)
    ax.set_title('Distribution of Cases by Gender', fontsize=14)
    ax.set_xlabel('Gender', fontsize=12)
    ax.set_ylabel('Number of Cases', fontsize=12)
else:
    filtered_age_group_distribution.plot(kind='line', marker='o', ax=ax)
    ax.set_title('Distribution of Cases by Age Group', fontsize=14)
    ax.set_xlabel('Age Group', fontsize=12)
    ax.set_ylabel('Number of Cases', fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)