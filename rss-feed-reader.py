import feedparser
import json

newsFeed = feedparser.parse("https://www.thehindu.com/opinion/feeder/default.rss")

entry = newsFeed.entries[0]
#print(entry.keys())

rss_feed_links_list = []

for entry in newsFeed.entries:
    outer_dict = {}
    inner_dict = {'summary':entry.summary, 'publishdate': entry.published}
    outer_dict[entry.link] = inner_dict
    #print(entry.link)
    #print(entry.summary)
    #print(entry.published)
    rss_feed_links_list.append(outer_dict)

rssdict = {}
rssdict['thehindu~opinion'] = rss_feed_links_list
json_data = json.dumps(rssdict)

with open("D:\Sudhanshu\my_files\development\python-test\myfiles\json_data.json","w") as f:
    f.write(json_data)

