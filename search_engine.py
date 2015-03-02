import requests
from bs4 import BeautifulSoup
def downloadUrl(url):
	r = requests.get(url)
	if r.status_code != 200:
		raise Exception("Bad Status code:{} ".format(r.status_code))

	return r

def parseText(html):
	bs = BeautifulSoup(html.text)
	return bs.select('div.usertext-body')[1].text


