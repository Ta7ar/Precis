from webscraping.summarizer import summarize

# Dummy class
# TODO: Replace with db model later
class Article:
    def __init__(self,title,body,publisher,publish_date,link) -> None:
        self.title = title
        self.body = summarize(body)
        self.publisher = publisher
        self.publish_date = publish_date
        self.link = link
    
    def __repr__(self) -> str:
        return f'''
        {self.title} | {self.publisher}

        on {self.publish_date}

        {self.body}

        Read more here: {self.link}
        '''