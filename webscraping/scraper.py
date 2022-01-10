from bs4 import BeautifulSoup
from urllib import request
from webscraping.article import Article

class Scraper:
    def __init__(self,url) -> None:
        self.soup = Scraper._generate_soup(url)
    
    @staticmethod
    def _generate_soup(url):
        source = request.urlopen(url).read()
        soup = BeautifulSoup(source,'lxml')
        return soup

    def _get_links(self):
        raise NotImplementedError()

    def _parse_link(self,link) -> Article:
        raise NotImplementedError()

    def __call__(self):
        links = self._get_links()
        articles = []
        for link in links:
            try:
                articles.append(self._parse_link(link))
            except Exception as e:
                print("Could not parse link: ",link)
                print(e)

        return articles

class CNBC(Scraper):
    def _get_links(self):
        thumbnail_tags = self.soup.find('div',attrs={'id':'homepage-riverPlus'}).find_all('div',attrs={'class':'RiverHeadline-headline RiverHeadline-hasThumbnail'})
        links = [thumbnail.find('a').attrs['href'] for thumbnail in thumbnail_tags]
        links = [link for link in links if link != '/pro/']
        return links

    def _parse_link(self, link) -> Article:
        soup = Scraper._generate_soup(link)

        title = soup.title.get_text()

        publish_date = soup.find('time',attrs={'itemprop':'datePublished'}).attrs['datetime']

        article_p_tags = soup.find('div',attrs={'class':'ArticleBody-articleBody'}).find_all('p')
        body = ''.join([tag.get_text() for tag in article_p_tags])

        return Article(title,body,"CNBC",publish_date,link)

class CBSNews(Scraper):
    def _get_links(self):
        a_tags = self.soup.find_all('a')
        links = [tag.attrs['href'] for tag in a_tags if "https://www.cbsnews.com/news" in tag.attrs['href']]
        return links

    def _parse_link(self, link) -> Article:
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
        publish_date = soup.find('header', attrs={'class':'content__header'}).find('time').attrs['datetime']

        return Article(title,body,"CBS News",publish_date, link)
        
        
def run():
    scrapers = [CNBC("https://www.cnbc.com/"), CBSNews("https://www.cbsnews.com")]
    articles = []
    for scraper in scrapers:
        articles.extend(scraper())
    return articles
