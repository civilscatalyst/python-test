
# Read more about usage on https://newspaper.readthedocs.io/en/latest/

from newspaper import Article

url = 'https://www.thehindu.com/news/national/norway-goes-green-in-delhi/article25860444.ece?homepage=true'

article = Article(url)

article.download()
article.parse()
print('The title is - ', article.title)
print(article.text)