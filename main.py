from webscraping.summarizer import summarize

if __name__ == "__main__":
    sample_text_file = open('./sample_passage.txt','r')
    sample_text = sample_text_file.read()
    summary = summarize(sample_text)
    print(summary)