from webscraping.summarizer import summarize

class Article:
    def __init__(self,title,body,publisher,link) -> None:
        self.title = title
        self.body = summarize(body)
        self.publisher = publisher
        self.link = link
    
    def __repr__(self) -> str:
        return f'''
        {self.title} | {self.publisher}

        on {self.publish_date}

        {self.body}

        Read more here: {self.link}
        '''