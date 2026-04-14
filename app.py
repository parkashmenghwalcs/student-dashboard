import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page settings
st.set_page_config(page_title="Student Dashboard", layout="wide")

# Title
st.title("📊 Student Data Dashboard")

# Load data
df = pd.read_csv("students.csv")

# Sidebar filter
st.sidebar.header("🔍 Filter Options")
subject = st.sidebar.selectbox("Select Subject", df["Subject"].unique())

# Filtered data
filtered_df = df[df["Subject"] == subject]

# Layout (columns)
col1, col2 = st.columns(2)

# Column 1 → Data + Average
with col1:
    st.subheader("📄 Student Data")
    st.dataframe(filtered_df)

    st.subheader("📊 Average Marks")
    st.write(filtered_df["Marks"].mean())

# Column 2 → Top Student
with col2:
    st.subheader("🏆 Top Student")
    top_student = df.loc[df["Marks"].idxmax()]
    st.success(f"{top_student['Name']} with {top_student['Marks']} marks")

# Full width Graph
st.subheader("📈 Marks Comparison")

fig, ax = plt.subplots()
sns.barplot(x="Name", y="Marks", data=filtered_df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Pie Chart
st.subheader("🥧 Marks Distribution")

fig2, ax2 = plt.subplots()
ax2.pie(df["Marks"], labels=df["Name"], autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("✨ Created by Parkash | Data Science Project")