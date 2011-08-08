#!/usr/bin/python
#
# Bismillahi-r-Rahmani-r-Rahim
# Scraper for Guardian Open Platform

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from time import sleep
import json
import os
import codecs

# Change the following to the value of your Guardian API key:
guardian_key = open('/home/daoud/guardian_key').read().strip()

# Change this to a suitable location for saving the downloaded files
data_dir = '/home/daoud/Data/rte'

# Set this to the maximum number of pages you wish to download/50
max_pages = 10000

query = r'http://content.guardianapis.com/search?from-date=2004-01-01&page=1&page-size=50&order-by=oldest&format=json&show-fields=headline%2Cbody&show-redistributable-only=body&api-key=' + guardian_key


def save(dirname, page, headline, body):
    global data_dir
    f = codecs.open(os.path.join(dirname, str(page)), 'w', 'utf_8')
    f.write(headline + '\n')
    f.write(body)

def scrape(start_page=1):
    global query, max_pages, data_dir
    for n in xrange(start_page, max_pages):
        dirname = os.path.join(data_dir,str(n))
        if os.path.exists(dirname):
            continue
        print "Retrieving page set: ", n, "...",
        os.makedirs(dirname)
        url = query.replace('page=1','page=%d' % n)
        data = json.load(urlopen(url))
        i = 1
        for x in data['response']['results']:
            fields = x['fields']
            headline = fields['headline'].replace('\n','')
            raw_body = fields['body']
            body = BeautifulSoup(raw_body,smartQuotesTo=None).getText('\n')
            body_cleaned = body.split('\n\n\n\n\n')[0]
            save(dirname, i, headline, body_cleaned)
            i += 1
        print 'done.'
        sleep(1)

if __name__ == "__main__":
    scrape()
