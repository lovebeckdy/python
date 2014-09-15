import urllib
import urlparse
from bs4 import BeautifulSoup

url = "http://espn.com"

urls = [url]
visited = [url]

videos = []
images = []
links = []

while len(urls)>0:
	try:
		cur_url = urls[-1]
		html = urllib.urlopen(cur_url).read()
	except:
		print cur_url

	soup = BeautifulSoup(html)
	urls.pop()
	print len(urls)

	#print soup.title
	#print soup.title.name
	#print soup.title.string

	for tag in soup.findAll('img', src= True):
		images.append(tag['src'])

	for tag in soup.findAll('video', src=True):
		videos.append(tag['video'])

	for tag in soup.findAll('a', href=True):
		tag['href'] = urlparse.urljoin(cur_url,tag['href'])
		if cur_url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

print images
print videos