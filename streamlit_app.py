import streamlit as st
import pandas as pd

st.title("📊 Metadata Explorer")

# Load a sample of the dataset (not the full 1.54 GB at once)
try:
    df = pd.read_csv("metadata_sample.csv", nrows=5000)  # sample only
    df.to_csv("metadata_sample.csv", index=False)
    st.success("Sample data loaded successfully!")
except Exception as e:
    st.error(f"Error loading data: {e}")
    df = None

if df is not None:
    # Show dataset preview
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Show basic info
    st.subheader("Basic Information")
    st.write(f"Number of rows (sampled): {len(df)}")
    st.write(f"Columns: {list(df.columns)}")

    # ---- Search Feature ----
    st.subheader("🔍 Search")
    search_term = st.text_input("Enter keyword to search in titles or abstracts:")
    if search_term:
        results = df[
            df["title"].str.contains(search_term, case=False, na=False) |
            df["abstract"].str.contains(search_term, case=False, na=False)
        ]
        st.write(f"Found {len(results)} matching rows")
        st.write(results.head(10))

    # ---- Filter by Year ----
    st.subheader("📅 Filter by Year")
    years = df["publish_time"].dropna().astype(str).str[:4].unique()
    years = sorted([y for y in years if y.isdigit()])
    selected_year = st.selectbox("Select Year", years)
    if selected_year:
        filtered = df[df["publish_time"].astype(str).str.startswith(selected_year)]
        st.write(f"Articles published in {selected_year}: {len(filtered)}")
        st.write(filtered.head(10))

            # ---- Publications by Year ----
    # ---- Publications by Year ----
st.subheader("📈 Publications Over Time")
df["year"] = pd.to_datetime(df["publish_time"], errors="coerce").dt.year
year_counts = df["year"].dropna().value_counts().sort_index()
st.line_chart(year_counts)

    # ---- Top Journals ----
st.subheader("🏛️ Top Journals (Sample Data)")
if "journal" in df.columns:
    top_journals = df["journal"].dropna().value_counts().head(10)
    st.bar_chart(top_journals)

        # ---- Word Cloud of Titles ----
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    st.subheader("☁️ Word Cloud of Paper Titles")
    text = " ".join(df["title"].dropna().astype(str).tolist())
    wordcloud = WordCloud(
    width=1200, height=600,
    background_color="white",
    max_words=200
).generate(text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

