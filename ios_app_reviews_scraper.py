#$ sudo pip3 install Request

from urllib.request import urlopen
import requests
import json
import time
import csv

list_of_row = []

def getJson(url):
    r = requests.get(url)
    if r.status_code == 200:
        r_payload_dict = r.json()
    return r.json()

def getReviews(appID, page=1):
    if page < 5:
        url = 'https://itunes.apple.com/rss/customerreviews/id=%s/page=%d/sortby=mostrecent/json' % (appID, page)
        data = getJson(url).get('feed')
        if data.get('entry') == None:
            getReviews(appID, page+1)
            return

        for entry in data.get('entry'):

            review_id = entry.get('id').get('label')
            title = entry.get('title').get('label')
            author = entry.get('author').get('name').get('label')
            author_url = entry.get('author').get('uri').get('label')
            version = entry.get('im:version').get('label')
            rating = entry.get('im:rating').get('label')
            review = entry.get('content').get('label')
            vote_count = entry.get('im:voteCount').get('label')

            csvData = [review_id, title.replace('"', '""'), author, author_url, version, rating, review.replace('"', '""'), vote_count]
            list_of_row.append(csvData)

            print ('"'+'","'.join(csvData)+'"')

        getReviews(appID, page+1)


csvTitles = ['review_id', 'title', 'author', 'author_url', 'version', 'rating', 'review', 'vote_count']
print (','.join(csvTitles))

with open('reviews.csv','w') as f:
    getReviews("replace here by appID") #input the appID
    f_csv = csv.writer(f)
    f_csv.writerow(csvTitles)
    f_csv.writerows(list_of_row)
