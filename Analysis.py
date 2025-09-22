import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("metadata.csv")

# Basic info
print("Shape:", df.shape)
print(df.info())
print(df.head())
print("Missing values:\n", df.isnull().sum().head(10))

# Clean and prepare
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df_clean = df.dropna(subset=['title', 'publish_time'])

# =======================
# Analysis & Visualizations
# =======================

# 1. Publications by Year
year_counts = df_clean['year'].value_counts().sort_index()
plt.figure(figsize=(8,4))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# 2. Top Journals
top_journals = df_clean['journal'].value_counts().head(10)
plt.figure(figsize=(8,4))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis")
plt.title("Top Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()

# 3. Distribution by Source
top_sources = df_clean['source_x'].value_counts().head(10)
plt.figure(figsize=(8,4))
sns.barplot(y=top_sources.index, x=top_sources.values, palette="mako")
plt.title("Top Sources of Publications")
plt.xlabel("Number of Papers")
plt.ylabel("Source")
plt.show()
