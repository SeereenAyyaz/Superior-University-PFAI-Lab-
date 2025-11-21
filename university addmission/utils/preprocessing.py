import json
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def load_data(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def preprocess_data(data, max_len=10):
    sentences = []
    labels = []
    tags = []

    for intent in data['intents']:
        tag = intent['tag']
        tags.append(tag)
        for pattern in intent['patterns']:
            tokens = nltk.word_tokenize(pattern.lower())
            tokens = [lemmatizer.lemmatize(word) for word in tokens]
            sentences.append(" ".join(tokens))
            labels.append(tag)
    
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(sentences)
    X = tokenizer.texts_to_sequences(sentences)
    X = pad_sequences(X, maxlen=max_len)
    
    tag_index = {tag:i for i, tag in enumerate(tags)}
    y = np.array([tag_index[label] for label in labels])

    return X, y, tokenizer, tag_index
if __name__ == "__main__":
    data = load_data('intents.json')
    X, y, tokenizer, tag_index = preprocess_data(data)
    print("Preprocessed Data:")
    print("X shape:", X.shape)
    print("y shape:", y.shape)