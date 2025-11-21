import glob
import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

path = r"C:\path\to\Urdu-Ghazal-Corpus" 
files = sorted(glob.glob(path + r'\**\*.csv', recursive=True))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # remove punctuation
    text = re.sub(r'\s+', ' ', text)            # remove extra spaces
    return text

columns = ['Poet', 'Title', 'Urdu_Text', 'Translated_Text']
columns.append('Cleaned_Text')
all_shayari = []

for file in files:
    df = pd.read_csv(file, names=columns[:-1], skiprows=1)
    df['Cleaned_Text'] = df['Translated_Text'].astype(str).apply(clean_text)
    all_shayari.extend(df[columns].values.tolist())

shayari_df = pd.DataFrame(all_shayari, columns=columns)
shayari_df.to_csv('cleaned_shayari_data.csv', index=False)
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(shayari_df['Cleaned_Text'])
nn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
nn_model.fit(tfidf_matrix)

def get_similar_shayari(query, count=5):
    query_cleaned = clean_text(query)
    query_vec = vectorizer.transform([query_cleaned])
    distances, indices = nn_model.kneighbors(query_vec, n_neighbors=count)

    for i in range(count):
        print(f"Shayari {i+1}, Distance: {distances[0][i]:.4f}")
        print(shayari_df['Translated_Text'].iloc[indices[0][i]])
        print("-"*50)
get_similar_shayari("Love and longing in Urdu poetry")
