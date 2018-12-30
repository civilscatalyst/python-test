from bs4 import BeautifulSoup
import requests

def formatContentForDisplayAsHTML(result_dict):
    #print(result_dict)
    for key in result_dict:
        print(result_dict[key])
        article_content = result_dict[key]['ArticleContent']
        print('Article COntent is ' ,article_content)
        soup = BeautifulSoup(article_content, 'html.parser')

        formatted_content = ""
        for link in soup.find_all('p'):
            wordsInCurrentText = len(link.get_text().split())
            print(wordsInCurrentText)
            if wordsInCurrentText < 10:
                formatted_content = formatted_content + "<p><b>"+link.get_text()+"</b></p>"
            else:
                formatted_content = formatted_content + "<p>"+link.get_text()+"</p>"
        
        result_dict[key]['ArticleContent'] = formatted_content
        #print(result_dict)