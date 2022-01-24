# Precis

Precis scrapes news articles from news sites and summarizes them based on Latent Semantic Analysis. 

## Technical Stuff
* News articles are scraped using Python `BeautifulSoup4`
* Text preprocessing is done through Python `NLTK` where stop words and punctuations are removed and words are stemmed.
* Latent Semantic Analysis/ Indexing is carried out by first computing TF-IDF matrix from the corpus and then performing truncated SVD (Singular Value Decomposition) on the matrix.
Both TF-IDF and SVD computations are done through `Scikit-Learn`.
* Top sentences are selected through 'Cross Method.'
* The backend uses a `Flask` server with `MongoDB` that serves a `React` frontend.
