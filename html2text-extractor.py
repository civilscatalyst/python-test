import html2text
import requests
#Make the proxy settings, if your access is through a proxy server
# proxies={http:10.10.80.11:3128,https:10.10.80.11:3128}
url = "https://www.livemint.com/Opinion/ahcmBVMo38uPryNOzVyEEJ/Opinion-An-attempt-to-understand-and-contextualise-farmer-s.html"
# res = requests.get(url, proxies = proxies, timeout=5.0 )
res = requests.get(url, timeout=5.0 )
html = res.text
# extract the text from the html version
text = html2text.html2text(html)
print(text)

with open("D:\Sudhanshu\my_files\development\python-test\myfiles\AnotherFile.html","x", encoding="utf-8") as f:
    f.write(html)

if not f.closed:
    f.close()