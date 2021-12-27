from typing import List
import numpy as np
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

nltk.download('punkt')
nltk.download('stopwords')

SYMBOLS = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n,"

stop_words = set(stopwords.words("english"))
stemmer = SnowballStemmer("english")

def preprocess(text: str) -> List[str]:

    # Convert to all lowercase
    text = text.lower()

    # Remove punctuations
    for punctuation in SYMBOLS:
        text = text.replace(punctuation,' ')
    
    # Remove apostrophes
    text = text.replace("'",'')

    tokens = word_tokenize(text)

    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]

    # Stemming
    stemmed_tokens = {stemmer.stem(token) for token in tokens}

    return stemmed_tokens



def summarize(text: str) -> str:
    sentences = sent_tokenize(text)
    tokens = preprocess(text)
    print(tokens)

# A = np.random.normal(size=[3,2])
# u,s,vh = np.linalg.svd(A,full_matrices=False)
# A_prime = u @ np.diag(s) @ vh

