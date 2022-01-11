from bs4 import BeautifulSoup
from urllib import request
from webscraping.article import Article
from db import get_article_links_by_publisher, save_articles

class Scraper:
    def __init__(self,url) -> None:
        self.publisher = self.__class__.__name__
        self.homepage = Scraper._generate_soup(url)
    
    @staticmethod
    def _generate_soup(url):
        source = request.urlopen(url).read()
        soup = BeautifulSoup(source,'lxml')
        return soup

    def get_links(self):
        raise NotImplementedError()

    def parse_link(self,link) -> Article:
        raise NotImplementedError()

class CNBC(Scraper):
    def get_links(self):
        thumbnail_tags = self.homepage.find('div',attrs={'id':'homepage-riverPlus'}).find_all('div',attrs={'class':'RiverHeadline-headline RiverHeadline-hasThumbnail'})
        links = [thumbnail.find('a').attrs['href'] for thumbnail in thumbnail_tags]
        links = [link for link in links if link != '/pro/']
        return links

    def parse_link(self, link) -> Article:
        soup = Scraper._generate_soup(link)

        title = soup.title.get_text()

        article_p_tags = soup.find('div',attrs={'class':'ArticleBody-articleBody'}).find_all('p')
        body = ''.join([tag.get_text() for tag in article_p_tags])

        return Article(title,body,self.publisher,link)

class CBSNews(Scraper):
    def get_links(self):
        a_tags = self.homepage.find_all('a')
        links = [tag.attrs['href'] for tag in a_tags if "https://www.cbsnews.com/news" in tag.attrs['href']]
        return links

    def parse_link(self, link) -> Article:
        soup = Scraper._generate_soup(link)
        content_body = soup.find('section',attrs={'class':'content__body'})

        contributed_by_ap_tag = content_body.find('em')
        app_upsell_tag = content_body.find('p',attrs={'class': 'item__dek'})

        if contributed_by_ap_tag is not None:
            contributed_by_ap_tag.decompose()
        if app_upsell_tag is not None:
            app_upsell_tag.decompose()
        
        body = ''.join([tag.get_text() for tag in content_body.find_all('p')])
        title = soup.find('h1',attrs={'class':'content__title'}).get_text()

        return Article(title,body,self.publisher,link)
        
        
def run():
    # scrapers = [CNBC("CNBC","https://www.cnbc.com/"), CBSNews("CBS", "https://www.cbsnews.com")]
    scrapers = [CNBC("https://www.cnbc.com/")]
    for scraper in scrapers:
        # Get list of previously parsed articles already present in the db
        saved_links = get_article_links_by_publisher(scraper.publisher)

        # Get list of articles in the frontpage
        links = scraper.get_links()

        # Parse links that are not already in the db
        links = [link for link in links if link not in saved_links]

        articles = []
        for link in links:
            try:
                articles.append(scraper.parse_link(link))
            except Exception as e:
                print("Could not parse link: ",link)
                print(e)

        save_articles(articles)
