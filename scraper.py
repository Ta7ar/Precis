from bs4 import BeautifulSoup
from urllib import request
from article import Article
from datetime import datetime, timezone

class Scraper:
    def __init__(self,url) -> None:
        self.publisher = self.__class__.__name__
        self.url = url
    
    @staticmethod
    def _generate_soup(url):
        source = request.urlopen(url).read()
        soup = BeautifulSoup(source,'lxml')
        return soup

    def get_links(self):
        raise NotImplementedError()

    def parse_link(self,link) -> Article:
        raise NotImplementedError()

    def run(self, saved_links):
        links = self.get_links()
        links = [link for link in links if link not in saved_links]
        links = links[:15] if len(links) > 15 else links

        articles = []
        for link in links:
            try:
                print("Parsing link: ",link)
                articles.append(self.parse_link(link))
            except Exception as e:
                print("Could not parse link: ",link)
                print(e)
        return articles

class CNBC(Scraper):
    def get_links(self):
        homepage = Scraper._generate_soup(self.url)
        thumbnail_tags = homepage.find('div',attrs={'id':'homepage-riverPlus'}).find_all('div',attrs={'class':'RiverHeadline-headline RiverHeadline-hasThumbnail'})
        links = [thumbnail.find('a').attrs['href'] for thumbnail in thumbnail_tags]
        links = [link for link in links if link != '/pro/']
        return links

    def parse_link(self, link) -> Article:
        soup = Scraper._generate_soup(link)

        title = soup.title.get_text()

        article_p_tags = soup.find('div',attrs={'class':'ArticleBody-articleBody'}).find_all('p')
        body = ''.join([tag.get_text() for tag in article_p_tags])

        return Article(title,body,self.publisher,link)

class CBS(Scraper):
    def get_links(self):
        homepage = Scraper._generate_soup(self.url)
        a_tags = homepage.find_all('a')
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

def scrape_articles():
    scrapers = [CNBC("https://www.cnbc.com/"), CBS("https://www.cbsnews.com")]

    current_datetime = datetime.now(timezone.utc)
    elapsed_time, last_insert_date = Article.get_last_insert_et_and_date(current_datetime)

    if last_insert_date is None or last_insert_date < current_datetime.date():
        # If articles were scraped on a previous day, delete all old articles
        Article.delete_all()

    elif elapsed_time is not None and elapsed_time < 6:
        # Scrape no more than once every 6 hours
        return
    
    articles = []
    for scraper in scrapers:
        saved_links = Article.get_links_by_publisher(scraper.publisher)
        articles.extend(scraper.run(saved_links))
    
    Article.save(articles)

    '''
    MULTIPROCESS IMPLEMENTATION

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = []
        articles = []
        for scraper in scrapers:
            saved_links = Article.get_links_by_publisher(scraper.publisher)
            future = executor.submit(scraper.run,saved_links)
            results.append(future)
        for future in concurrent.futures.as_completed(results):
            articles.extend(future.result())
        Article.save(articles)
    '''