
# Read more about usage on https://newspaper.readthedocs.io/en/latest/

from newspaper import Article
import nltk
import time 

#nltk.download('all')

def fetchArticle(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    inner_dict = {'ArticleSummary':article.summary,'ArticleContent':article.text,'ArticleImage':article.top_image}
    retrieved_data_dict = {url:inner_dict}
    time.sleep(3)
    return retrieved_data_dict
