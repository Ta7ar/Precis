from bs4 import BeautifulSoup
from urllib import request
from article import Article

def scrape_cnbc():
    source = request.urlopen("https://www.cnbc.com/").read()
    soup = BeautifulSoup(source,'lxml')

    # Get list of article links from front page
    thumbnail_tags = soup.find('div',attrs={'id':'homepage-riverPlus'}).find_all('div',attrs={'class':'RiverHeadline-headline RiverHeadline-hasThumbnail'})
    links = [thumbnail.find('a').attrs['href'] for thumbnail in thumbnail_tags]
    links = [link for link in links if link != '/pro/']

    # Parse the article from each link
    articles = []
    for link in links:
        try:
            source = request.urlopen(link).read()
            soup = BeautifulSoup(source,'lxml')
            article_p_tags = soup.find('div',attrs={'class':'ArticleBody-articleBody'}).find_all('p')
            article_text = ''.join([tag.get_text() for tag in article_p_tags])

            article = Article("t","wack",article_text,"CNBC","2022",link)

            articles.append(article)
        except Exception:
            print("Could not parse link: ",link)
    return articles
        




scrape_cnbc()

