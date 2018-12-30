from bs4 import BeautifulSoup
import requests

url = "https://www.thehindu.com/news/international/voting-in-tense-general-election-in-bangladesh-ends/article25865024.ece?homepage=true"

result = requests.get(url)
data = result.text

data2 = ""
with open("D:\Sudhanshu\my_files\development\python-test\myfiles\scrapedArticle2.html","r", encoding="utf-8") as f:
    for line in f:
        data2=data2+line
    
# print(data2)
print(result.encoding)

soup = BeautifulSoup(data2, 'html.parser')
# print(soup.prettify())

formattedResult = ""
for link in soup.find_all('p'):
    wordsInCurrentText = len(link.get_text().split())
    print(wordsInCurrentText)
    if wordsInCurrentText < 10:
        formattedResult = formattedResult + "<p><b>"+link.get_text()+"</b></p>"
    else:
        formattedResult = formattedResult + "<p>"+link.get_text()+"</p>"

with open("D:\Sudhanshu\my_files\development\python-test\myfiles\scrapedArticle_formatted.html", "w") as formattedFile:
    formattedFile.write(formattedResult)

