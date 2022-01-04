from summarizer import summarize

# Dummy class
# TODO: Replace with db model later
class Article:
    def __init__(self,title,author,body,publisher,publish_date,link) -> None:
        self.title = title
        self.author = author
        self.body = body
        self.summarized_body = summarize(body)
        self.publisher = publisher
        self.publish_date = publish_date
        self.link = link
    