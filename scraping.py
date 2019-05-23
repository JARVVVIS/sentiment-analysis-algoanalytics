import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from textblob import TextBlob  
import matplotlib.pyplot as plt
import numpy as np  
plt.style.use('fivethirtyeight')
review_url = []
reviews = []
polarity = []
for i in range(1,4):
    url = 'https://autoportal.com/newcars/ford/ecosport/reviews/page/'+str(i)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page,'html.parser')
    for div in soup.find_all('div',attrs={'class':'model-reviews__item'}):
        review_url.append('https://autoportal.com' + div.find('a')['href'])
    
    for rev in review_url:
        page_ = urllib2.urlopen(rev)
        soup = BeautifulSoup(page_,'html.parser')
        result = str(soup.find('div',attrs={'class':'reviews-description'}))
        reviews.append(result)
        analysis = TextBlob(result)
        print(len(reviews))
        polarity.append(analysis.sentiment.polarity)
    print(i)
    
print(len(reviews))
plt.plot(polarity)
plt.xticks(np.arange(1,len(reviews),step=1))
plt.show()