import sys
try:
  from bs4 import BeautifulSoup
except:
  from BeautifulSoup import BeautifulSoup
try:
  from urllib.parse import urlparse
  from urllib.request import urlopen
except:
  from urlparse import urlparse
  from urllib2 import urlopen
from bottle import route, get, post, request, run, template, view

VALID_TAGS = [ 'p', 'br', 'ul', 'ol', 'li', 'a', 'img', 'table', 'tbody', 'tr', 'th', 'td' ]
TRANS_DICT = { 
  'div': 'p', 
  'b': 'strong',
  'i': 'em',
  'h1': 'h3',
  'h2': 'h3' }
TRANS_TAGS = TRANS_DICT.keys()

def clean(soup):
  rejected = { }
  for tag in soup.findAll(True):
    check_p = True
    del tag['class']
    if tag.name in TRANS_TAGS:
      tag.name = TRANS_DICT.get(tag.name, 'p')
    elif tag.name not in VALID_TAGS:
      rejected[tag.name] = True
      tag.replaceWithChildren() # tag.unwrap() in bs4
      check_p = False
    if check_p and tag.name == 'p' and tag.parent.name == 'p':
      tag.parent.replaceWithChildren() # tag.parent.unwrap() in bs4
  return rejected

@get('/')
@view('cleaner')
def index():
  source = ''
  cleaned = ''
  rejected = ''
  return dict(source=source, cleaned=cleaned, rejected=rejected)

@post('/')
@view('cleaner')
def show():
  source = request.forms.get('source').strip()
  soup = None
  o = urlparse(source)
  if o.scheme == 'http' or o.scheme == 'https':
    page = urlopen(source)
    soup = BeautifulSoup(page.read())
    div = soup.find('div', class_='file-library')
    if div:
      div = div.find('ul')
    else:
      div = soup.find('div', class_='ui-article')
    if div:
      soup = div
  else:
    soup = BeautifulSoup(source)
  rejected = ", ".join(clean(soup))
  cleaned = soup.prettify()
  return dict(source=source, cleaned=cleaned, rejected=rejected)

if __name__ == '__main__':
  run(host='0.0.0.0', port=8098)
