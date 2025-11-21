from flask import Flask, request, render_template
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# Load dataset
df = pd.read_csv("qa_dataset.csv")  
df['Cleaned_Question'] = df['Question'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', str(x).lower()))

# Vectorize
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(df['Cleaned_Question'])
nn_model = NearestNeighbors(n_neighbors=3, metric='cosine')
nn_model.fit(question_vectors)

# Function to get answer
def get_answer(user_query, top_n=1):
    query_vec = vectorizer.transform([re.sub(r'[^a-zA-Z0-9\s]', '', str(user_query).lower())])
    distances, indices = nn_model.kneighbors(query_vec, n_neighbors=top_n)
    return df['Answer'].iloc[indices[0][0]]

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_msg = request.form["message"]
    answer = get_answer(user_msg)
    return {"response": answer}

if __name__ == "__main__":
    app.run(debug=True)
