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

def process_document(doc: str):
    # Convert to all lowercase
    doc = doc.lower()

    # Remove apostrophes
    doc = doc.replace("'",'')
    
    # Remove punctuations
    for punctuation in SYMBOLS:
        doc = doc.replace(punctuation,' ')

    tokens = word_tokenize(doc)

    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]

    # Stemming
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    return " ".join(stemmed_tokens)

def pre_process(documents_list: List[str]) -> List[str]:
    corpus = []
    for document in documents_list:
        corpus.append(process_document(document))
    return corpus

def select_top_docs(vt: np.ndarray,n: int=5) -> List[int]:
    '''
    Select top n documents based on "cross method" as defined in

    "Ozsoy, Makbule & Alpaslan, Ferda & Cicekli, Ilyas. (2011). 
    Text summarization using Latent Semantic Analysis. J. 
    Information Science. 37. 405-417. 10.1177/0165551511408848."

    "https://www.researchgate.net/publication/220195824_Text_summarization_using_Latent_Semantic_Analysis"
    '''
    # Number of sentences to select cannot be more than the number of sentences available
    n = min(n,vt.shape[1])
    n = min(n,vt.shape[1] // 2)

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

def gen_vt_matrix(corpus: List[str],k: int=2):
    k = min(k,len(corpus)-1)
    vectorizer = TfidfVectorizer()
    tf_idf = vectorizer.fit_transform(corpus)
    svd = TruncatedSVD(k)
    svd.fit_transform(tf_idf.transpose())
    vt = svd.components_
    return vt

def summarize(text: str) -> str:
    documents_list = sent_tokenize(text)
    corpus = pre_process(documents_list)
    vt = gen_vt_matrix(corpus)
    selected_sentences = select_top_docs(vt)
    summary = [documents_list[i] for i in sorted(selected_sentences)]
    return ''.join(summary)
