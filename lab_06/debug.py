import contractions
import string
import nltk
from nltk.corpus import stopwords
import pandas as pd

ds = pd.read_csv('spam.csv', encoding='ISO-8859-1')

# Load NLTK stop words
stop_words = set(stopwords.words('english'))
# print(stop_words)
row=10
processed_words=[]
for word in ds.loc[row, 'message'].split():
    expanded_words = contractions.fix(word)
    word_without_punct = expanded_words.translate(str.maketrans('', '', string.punctuation))
    word_lowercase = word_without_punct.lower()
    for single_word in word_lowercase.split():
        if single_word not in stop_words:
            processed_words.append(single_word)  
ds.loc[row, 'message'] = ' '.join(processed_words)

print(ds.loc[row, 'message'])
