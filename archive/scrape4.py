from bs4 import BeautifulSoup
import urllib2

url="https://www.google.com/search?tbm=isch&q=%s"

def search(query):
  new_url = url % query
  html = urllib2.urlopen(new_url).read()
  soup = BeautifulSoup(html, "lxml")
  categories = soup.findAll("a", "sq").string
  #winner = [a.string for h2 in soup.findAll("h2", "boc1")]
  #runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
  for category in categories:
      print category

  return #{"category": category}

search("music")
