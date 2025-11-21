import pandas as pd
import re

# URL of the raw CSV
url = [
        "https://raw.githubusercontent.com/ShathaTm/LK-Hadith-Corpus/refs/heads/master/AbuDaud/Chapter1.csv"
        "https://raw.githubusercontent.com/ShathaTm/LK-Hadith-Corpus/refs/heads/master/AbuDaud/Chapter8.csv"
]
# Columns
columns = [
    'Chapter_Number', 'Chapter_English', 'Chapter_Arabic',
    'Section_Number', 'Section_English', 'Section_Arabic',
    'Hadith_Number', 'English_Hadith', 'English_Isnad', 'English_Matn', 'English_Grade',
    'Arabic_Hadith', 'Arabic_Isnad', 'Arabic_Matn', 'Arabic_Grade'
]
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text
df = pd.read_csv(url, names=columns, skiprows=1)
df['Cleaned_Hadith'] = df['English_Hadith'].astype(str).apply(clean_text)

all_hadith = []
for idx, row in df.iterrows():
    chapter = row['Chapter_English']
    section = row['Section_English']
    hadith_num = row['Hadith_Number']
    question = f"What does Hadith {hadith_num} from Chapter '{chapter}' Section '{section}' say?"
    answer = row['English_Hadith']
    all_hadith.append([question, answer])
qa_df = pd.DataFrame(all_hadith, columns=['Question', 'Answer'])
qa_df.to_csv("qa_dataset.csv", index=False)

print("qa_dataset.csv created successfully!")
qa_df.head()
