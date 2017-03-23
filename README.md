# Craigslist-Search-Module
Python module to search craigslist
Requires feedparser

pip install feedparser


***Usage***

Import CraigsList

searchObject = CraigsList(["Cincinnati", "Louisville", "Dayton"], "Volkswagen")

searchObject.search()

for post in searchObject.results():
	print post + "\n"
