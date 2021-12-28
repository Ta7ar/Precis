from typing import List, Set, Tuple
from collections import Counter
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

def get_word_tokens(corpus):
    word_tokens = set()
    for doc in corpus:
        word_tokens.update(doc)
    return list(word_tokens)

def generate_tf_idf_matrix(word_tokens,corpus):

    m,n = len(word_tokens),len(corpus)
    # Calculate df (Document Frequency) for each word token
    # Defined as "Number of documents where the said word token exists"

    doc_frequencies = {}
    for word in word_tokens:
        doc_frequencies[word] = 0
        for doc in corpus:
            if word in doc:
                doc_frequencies[word] += 1
    
    tf_idf = np.zeros(shape=(m,n))

    for doc_i in range(len(corpus)):
        doc = corpus[doc_i]
        word_counter = Counter(doc)
        for word_i in range(len(word_tokens)):
            word = word_tokens[word_i]
            if word not in word_counter:
                continue
            df = doc_frequencies[word]
            tf = word_counter[word] / len(doc)
            idf = np.log(n/(1+df))
            tf_idf[word_i,doc_i] = tf*idf

    return tf_idf

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

    return stemmed_tokens

def process_corpus(corpus: str) -> Tuple[List[str], List[List[str]]]:
    '''
        Processes corpus to form list of sets.

        Parameters
        ----------
        corpus: str
            Corpus/text to process.
        
        Returns
        -------
        documents_list: List[str]
            Tokenized sentences of the corpus.
        processed_corpus: List[List[str]]
            List of lists representing word tokens for each tokenized sentence.
    '''
    documents_list = sent_tokenize(corpus)

    processed_corpus = []
    for document in documents_list:
        processed_corpus.append(process_document(document))

    return documents_list,processed_corpus



def summarize(text: str) -> str:
    doc_list,corpus = process_corpus(text)
    word_tokens = get_word_tokens(corpus)
    tf_idf_matrix = generate_tf_idf_matrix(word_tokens,corpus)
    print(tf_idf_matrix)

# A = np.random.normal(size=[3,2])
# u,s,vh = np.linalg.svd(A,full_matrices=False)
# A_prime = u @ np.diag(s) @ vh
