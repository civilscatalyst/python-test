## Json Structure layout
"""
{"NewsCategory":[
    "article_link1": {
        "ArticleSummary":"Summary",
        "ArticleContent":"Content".
        "ArticleImage":"Image"
    }
    "article_link2": {
        "ArticleSummary":"Summary",
        "ArticleContent":"Content".
        "ArticleImage":"Image"
    }
    "article_link3": {
        "ArticleSummary":"Summary",
        "ArticleContent":"Content".
        "ArticleImage":"Image"
    }
]}
"""


import json
import os
from NewspaperScraper import fetchArticle
from HTMLFormatter import formatContentForDisplayAsHTML

def retrieveLinksForScraping(rss_link_list):
    links_to_scrape = []
    for each_dict in rss_link_list:
        for key in each_dict:
            links_to_scrape.append(key)
    return links_to_scrape

def saveAsJsonFile(json_data_dict, file_name):
    json_str = json.dumps(json_data_dict)
    mode="x"
    if(os.path.exists("D:\Sudhanshu\my_files\development\python-test\myfiles\json_data_new"+file_name+".json")):
        mode="w"
    with open("D:\Sudhanshu\my_files\development\python-test\myfiles\json_data_new"+file_name+".json",mode) as f:
        f.write(json_str)

json_data_dict = {}
with open("D:\Sudhanshu\my_files\development\python-test\myfiles\json_data.json", "r") as json_file:
    json_data_dict = json.loads(json_file.read())



for key in json_data_dict:
    rss_link_list = json_data_dict[key]
    rss_link_list_new = []
    links_to_scrape_list = retrieveLinksForScraping(rss_link_list)

    for link in links_to_scrape_list:
        result_dict = fetchArticle(link)
        # formatContentForDisplayAsHTML(result_dict)
        #print(result_dict)
        rss_link_list_new.append(result_dict)

    json_data_dict[key] = rss_link_list_new
    saveAsJsonFile(json_data_dict, key)