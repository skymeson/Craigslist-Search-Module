import feedparser
import requests

class CraigsList(object):

    postList = {}
    formattedPostList = []

    def __init__(self, city, query):
        self.city = city
        self.query = query

    def search(self):

        for city in self.city:
            try:
            	r = requests.get('https://' + city + '.craigslist.org/search/sss?format=rss&query=' + self.query)
            	if r.status_code == 200:
            		feed = feedparser.parse(r.text)
            		for post in feed.entries:
            		    self.postList[post.title] = post.link

            except Exception as e:
            	return e

    def results(self):
    	for title, link in self.postList.iteritems():
    		self.formattedPostList.append('%s: %s' % (title, link))
        
        return self.formattedPostList
