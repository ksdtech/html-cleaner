#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# /usr/bin/python

import sys

try:
  from bs4 import BeautifulSoup
  def unwrap(tag):
    tag.unwrap()

  def find_tag_with_class(soup, tagname, classname):
    return soup.find(tagname, class_=classname)
except:
  from BeautifulSoup import BeautifulSoup
  def unwrap(tag):
    tag.replaceWithChildren()

  def find_tag_with_class(soup, tagname, classname):
    return soup.find(tagname, { 'class': classname })

try:
  from urllib.parse import urlparse
  from urllib.request import urlopen
except:
  from urlparse import urlparse
  from urllib2 import urlopen

from bottle import route, get, post, request, run, template, view

RUN_AS_CGI = True
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
      unwrap(tag)
      check_p = False
    if check_p and tag.name == 'p' and tag.parent.name == 'p':
      unwrap(tag.parent)
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
    div = find_tag_with_class(soup, 'div', 'file-library')
    if div:
      div = div.find('ul')
    else:
      div = find_tag_with_class(soup, 'div', 'ui-article')
    if div:
      soup = div
  else:
    soup = BeautifulSoup(source)
  rejected = ", ".join(clean(soup))
  cleaned = soup.prettify()
  return dict(source=source, cleaned=cleaned, rejected=rejected)

if RUN_AS_CGI:
  run(server='cgi')
elif __name__ == '__main__':
  run(host='0.0.0.0', port=8098)

  
