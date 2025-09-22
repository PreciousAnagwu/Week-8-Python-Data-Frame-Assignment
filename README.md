# 📊 Metadata Explorer (Week 8 Python Dataframe Assignment)

This project is a **Streamlit web application** for exploring the **CORD-19 metadata dataset**.
It allows users to search research papers, filter by publication year, view publication trends, explore top journals, and generate word clouds of paper titles.

---

## 🚀 Features

* **Dataset Preview**: Displays a sample of the metadata for quick inspection.
* **Search Tool**: Enter a keyword to search through titles and abstracts.
* **Year Filter**: Filter publications by year and see how many papers were published.
* **Publications Over Time**: Line chart showing the trend of publications by year.
* **Top Journals**: Bar chart of the most common journals in the dataset.
* **Word Cloud**: Visualization of the most frequent words in paper titles.

---

## 📂 Dataset

* **`metadata_sample.csv`** → a smaller, shareable sample (used for GitHub/Streamlit Cloud).
* **`metadata.csv`** → the full dataset (\~1.5GB).

  * ⚠️ This file is very large and should **not** be pushed to GitHub.
  * The app will fall back to the sample file if the full dataset is unavailable.

---

## 🛠️ Installation & Setup

1. **Clone the repository**

   ```bash
    git clone https://github.com/PreciousAnagwu/Week-8-Python-Data-Frame-Assignment.git
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run streamlit_app.py
   ```

---

## 📦 Requirements

Main Python libraries used:

* `pandas`
* `streamlit`
* `matplotlib`
* `seaborn`
* `wordcloud`

---

## 🌐 Live Deployment
You can view the live app here:
👉 [Live Demo](https://week-8-python-data-frame-assignment-k2sqv8pqx3hwc5tqswnr7b.streamlit.app/)


---

## ✨ Acknowledgements

* **CORD-19 Dataset** provided by [Allen Institute for AI](https://www.semanticscholar.org/cord19).
* Built as part of the **PLP Academy Week 8 Python Assignment**.
#



