from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense
from utils.preprocessing import load_data, preprocess_data
import json

data = load_data('data/intents.json')
X, y, tokenizer, tag_index = preprocess_data(data, max_len=10)
num_classes = len(tag_index)

model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=16, input_length=10))
model.add(GlobalAveragePooling1D())
model.add(Dense(16, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(X, y, epochs=200, verbose=1)

model.save("model/chatbot_model.h5")
with open("model/tokenizer.json", "w") as f:
    f.write(tokenizer.to_json())
with open("model/tag_index.json", "w") as f:
    json.dump(tag_index, f)

print("Model and tokenizer saved successfully!")
