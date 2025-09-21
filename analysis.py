import pandas as pd

# Load the dataset

df = pd.read_csv("metadata.csv", nrows =5000)

# Look at the first 5 rows
print(df.head())

# Check the size (rows, columns)
print("Shape:", df.shape)

# Info about data types
print(df.info())

# Check for missing values
print(df.isnull().sum())


# Convert publish_time column to datetime format
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract publication year
df['year'] = df['publish_time'].dt.year

# Handle missing titles: remove rows without titles
df = df.dropna(subset=['title'])

# Create a new column for abstract word count
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

print(df[['title', 'year', 'abstract_word_count']].head())


import matplotlib.pyplot as plt
import seaborn as sns

year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue")
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis")
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()


from wordcloud import WordCloud

# Combine all titles into one string
title_text = " ".join(df['title'].dropna())

# Create word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(title_text)

plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Frequent Words in Paper Titles")
plt.show()


top_sources = df['source_x'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(y=top_sources.index, x=top_sources.values, palette="coolwarm")
plt.title("Top Sources of COVID-19 Papers")
plt.xlabel("Number of Papers")
plt.ylabel("Source")
plt.show()
