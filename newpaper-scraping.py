
# Read more about usage on https://newspaper.readthedocs.io/en/latest/

from newspaper import Article
import nltk
#nltk.download('all')

url = 'https://www.thehindu.com/news/national/praying-at-the-altar-of-populism/article25863558.ece'
url2 = "https://www.livemint.com/Opinion/ahcmBVMo38uPryNOzVyEEJ/Opinion-An-attempt-to-understand-and-contextualise-farmer-s.html"
article = Article(url)

article.download()
article.parse()

# print(article.html)
f = open("myfiles/scrapedArticle.rst","w", encoding="utf-8")
f.write(str(article.text))
if not f.closed:
    f.close()


print('The title is - ', article.title)

# retrieves the top image link of the article
print(article.top_image)
print(article.authors) # didnt retrieve author name from thehindu properly

article.nlp()
print(article.summary)
print(article.text)