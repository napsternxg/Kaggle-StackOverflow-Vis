import urllib2
import gzip
from StringIO import StringIO
import json
import random

_getSiteUrl = "https://api.stackexchange.com/2.1/sites?pagesize=21&filter=!)r4me2Ja.cmnk_RSozOe&order=desc&sort=popular"

_getTopTagUrlFormat = "https://api.stackexchange.com/2.1/tags?order=desc&sort=popular&site=%s&pagesize=5"

def fetchJSONResponse(url):

	request = urllib2.Request(url)
	request.add_header('Accept-encoding', 'gzip')
	response = urllib2.urlopen(request)
	if response.info().get('Content-Encoding') == 'gzip':
	    buf = StringIO( response.read())
	    f = gzip.GzipFile(fileobj=buf)
	    data = f.read()
	data = json.loads(data)["items"]
	return data

siteNames = fetchJSONResponse(_getSiteUrl)
siteNames = siteNames[1:]

siteTagList = []
colorList = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf"]

for site in siteNames:
	siteTags = dict()
	topTagCount = 5
	siteTags["name"] = site["name"]
	print "Fetching top %d tags from: %s" %(topTagCount, site["name"])
	topTagURL = _getTopTagUrlFormat %(site["api_site_parameter"])
	tagResponse = fetchJSONResponse(topTagURL)
	tagList = [{"name": x["name"], "colour": random.choice(colorList), "size": x["count"]} for x in tagResponse]
	siteTags["children"] = tagList
	siteTagList.append(siteTags)

finalData = {"name": "Stack Exchange"}
finalData["children"] = siteTagList

with open('treeMap.json', 'wb') as fp:
    json.dump(finalData, fp, indent=4)
 




