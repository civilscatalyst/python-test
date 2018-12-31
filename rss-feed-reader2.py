import feedparser
import json

newsFeed = feedparser.parse("https://www.thehindu.com/opinion/feeder/default.rss")

#entry = newsFeed.entries[0]
#print(entry.keys())

rss_feed_links_list = []

rss_list = []
for entry in newsFeed.entries:
    print(entry)
    inner_dict = {'link':entry.link, 'summary':entry.summary, 'publishdate': entry.published, 'category':'opinion', 'newspaper':'thehindu'}
    rss_list.append(inner_dict)

json_data = json.dumps(rss_list)

""" with open("D:\Sudhanshu\my_files\development\python-test\myfiles\json_data.json","w") as f:
    f.write(json_data)
 """

print(rss_list)