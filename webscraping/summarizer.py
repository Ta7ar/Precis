from typing import List
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

nltk.download('punkt')
nltk.download('stopwords')

SYMBOLS = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n,"

stop_words = set(stopwords.words("english"))
stemmer = SnowballStemmer("english")

def pre_process(doc: str):
    # Convert to all lowercase
    doc = doc.lower()

    # Remove apostrophes
    doc = doc.replace("'",'')
    
    # Remove punctuations
    for punctuation in SYMBOLS:
        doc = doc.replace(punctuation,' ')

    tokens = word_tokenize(doc)

    # Removing stop words
    tokens = [token for token in tokens if token not in stop_words]

    # Stemming
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    return " ".join(stemmed_tokens)

def select_top_sentences(vt: np.ndarray,n: int=5) -> List[int]:
    '''
    Select top n documents based on "cross method" as defined in

    "Ozsoy, Makbule & Alpaslan, Ferda & Cicekli, Ilyas. (2011). 
    Text summarization using Latent Semantic Analysis. J. 
    Information Science. 37. 405-417. 10.1177/0165551511408848."

    "https://www.researchgate.net/publication/220195824_Text_summarization_using_Latent_Semantic_Analysis"
    '''
    # Number of sentences to select cannot be more than the number of sentences available
    n = min(n,vt.shape[1])

    for row in vt:
        row_avg = np.mean(row)
        row[row <= row_avg] = 0
    length_scores: np.ndarray = vt.sum(axis=0)
    selected_sent_indices = []
    for _ in range(n):
        sent_index = np.argmax(length_scores)
        selected_sent_indices.append(sent_index)
        length_scores[sent_index] = float('-inf')
    return selected_sent_indices

def summarize(text: str) -> str:
    corpus = sent_tokenize(text)

    vectorizer = TfidfVectorizer(preprocessor=pre_process)
    tf_idf = vectorizer.fit_transform(corpus)

    n_components = min(4,len(corpus)-1)
    svd = TruncatedSVD(n_components)
    svd.fit_transform(tf_idf.transpose())
    vt = svd.components_

    selected_sentences = select_top_sentences(vt)

    summary = [corpus[i] for i in sorted(selected_sentences)]
    return ''.join(summary)
