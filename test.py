import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from textblob import TextBlob  
import tokenizer

url = 'https://autoportal.com/newcars/ford/ecosport/reviews/headlight-issue-26232.html'
review_url = []
reviews = []
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,'html.parser')
test = soup.find('div',attrs={'class':'reviews-description'})