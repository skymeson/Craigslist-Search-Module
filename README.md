# Craigslist-Search-Module
Python module to search craigslist, requires feedparser.

pip install feedparser


***Usage***

from CraigsList Import CraigsList

searchObject = CraigsList(["Cincinnati", "Louisville", "Dayton"], "Volkswagen")

searchObject.search()

for post in searchObject.results():
	print post + "\n"
