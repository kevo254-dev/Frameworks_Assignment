import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ====================
# Load Data
# ====================
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df.dropna(subset=['title', 'publish_time'])

df = load_data()

# ====================
# Streamlit App Layout
# ====================
st.title("CORD-19 Data Explorer")
st.write("Simple interactive exploration of COVID-19 research papers")

# Filter by Year Range
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select Year Range:", min_year, max_year, (2020, 2021))
df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications Over Time
st.subheader("Publications Over Time")
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color="skyblue")
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = df_filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
top_journals.plot(kind="barh", ax=ax, color="orange")
ax.set_title("Top 10 Journals")
st.pyplot(fig)

# Top Sources
st.subheader("Top Sources")
top_sources = df_filtered['source_x'].value_counts().head(10)
fig, ax = plt.subplots()
top_sources.plot(kind="barh", ax=ax, color="green")
ax.set_title("Top 10 Sources")
st.pyplot(fig)

# Show Sample Data
st.subheader("Sample Data")
st.write(df_filtered.head())
