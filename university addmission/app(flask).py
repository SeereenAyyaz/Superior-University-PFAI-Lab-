from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

lemmatizer = WordNetLemmatizer()
nltk.download('punkt')

app = Flask(__name__)

model = load_model("model/chatbot_model.h5")
with open("model/tokenizer.json", "r") as f:
    tokenizer = tokenizer_from_json(f.read())
with open("model/tag_index.json", "r") as f:
    tag_index = json.load(f)
with open("data/intents.json", "r") as f:
    intents = json.load(f)

index_tag = {v:k for k,v in tag_index.items()}

def preprocess_sentence(sentence, tokenizer, max_len=10):
    tokens = nltk.word_tokenize(sentence.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    seq = tokenizer.texts_to_sequences([" ".join(tokens)])
    seq = pad_sequences(seq, maxlen=max_len)
    return seq

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    message = request.form["message"]
    seq = preprocess_sentence(message, tokenizer)
    pred = model.predict(seq)
    tag = index_tag[np.argmax(pred)]
    
    for intent in intents['intents']:
        if intent['tag'] == tag:
            response = np.random.choice(intent['responses'])
            break
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
