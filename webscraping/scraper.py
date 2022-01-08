from bs4 import BeautifulSoup
from urllib import request
from article import Article

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

        article_title = soup.title.get_text()

        article_publish_date = soup.find('time',attrs={'itemprop':'datePublished'}).attrs['datetime']

        article_p_tags = soup.find('div',attrs={'class':'ArticleBody-articleBody'}).find_all('p')
        article_text = ''.join([tag.get_text() for tag in article_p_tags])

        return Article(article_title,article_text,"CNBC",article_publish_date,link)
        
def run():
    scrapers = [CNBC("https://www.cnbc.com/")]
    articles = []
    for scraper in scrapers:
        articles.extend(scraper())
    return articles

print(run()[0])


