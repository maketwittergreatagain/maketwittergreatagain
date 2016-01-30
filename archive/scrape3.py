import urllib2
from bs4 import BeautifulSoup

url="https://www.google.com/search?tbm=isch&q=%s"

def search(query):
  new_url = url % query
  request = urllib2.urlopen(new_url)
  result = request.read()
  soup = BeautifulSoup(result)
  letters = soup.find_all("span", class_="sq")
  lobbying = {}
  for element in letters:
    lobbying[element.a.get_text()] = {}
    letters[0].a["href"]

  for category in letters:

    print "Category: %s/n" % category

search("music")
