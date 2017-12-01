# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:28:11 2017

@author: romul
"""

import tweepy
from pymongo import MongoClient
import sys
import time
from funcModule import *

#==============================================================================
# Parameters of search
#==============================================================================
config = {}
exec(open("./config.py").read(),config)

latitude = config['latitude']	# geographical centre of search
longitude = config['longitude'] # geographical centre of search
max_range = config['max_range'] # search range in kilometres
maxTweets = config['num_results'] # minimum results to obtain

oauth =  tweepy.OAuthHandler(config['CONSUMER_KEY'], config['CONSUMER_SECRET'])

#==============================================================================
# Initiate the connection to Twitter REST API
#==============================================================================

api = tweepy.API(oauth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

searchQuery = config['hashtag']
db_name = config['db_name']

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

print('Reading tweets with {}.'.format(searchQuery))

#==============================================================================
# Criando cliente do MongoDB e database
#==============================================================================
client = MongoClient()
try:
    client.drop_database(db_name)
    print("Creating {} database.".format(db_name))
except:
    print("Creating {} database.".format(db_name))
db = client[db_name]    
collection = db.tweets
print("Saving tweets on database.")

#==============================================================================
# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
#==============================================================================
sinceId = get_tweet_id(api, date='', days_ago=3, query='a')
#sinceId = None
#==============================================================================
# # If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
#==============================================================================  
max_id = get_tweet_id(api, date='', days_ago=0, query='a')

#==============================================================================
# perform a search based on latitude and longitude
# twitter API docs: https://dev.twitter.com/rest/reference/get/search/tweets 
#==============================================================================
loop = 0
tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
while tweetCount < maxTweets:
    
    try:
        loop += 1
        if (max_id <= 0):
            if (not sinceId):
                new_tweets = api.search(q=searchQuery,  
                               geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), 
                                                        count = 100, lang='en') 
            else:
                new_tweets = api.search(q=searchQuery,  
                               geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), 
                                                        count = 100, lang='en',
                                                        since_id=sinceId)
        else:
            if (not sinceId):
                new_tweets = api.search(q=searchQuery,  
                               geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), 
                                                        count = 100, lang='en',
                                                        max_id=str(max_id - 1))
            else:
                new_tweets = api.search(q=searchQuery,  
                               geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), 
                                                        count = 100, lang='en',
                                                        max_id=str(max_id - 1),
                                                                  since_id=sinceId)
        
        if not new_tweets:
#            if max_id > sinceId:                
#                print("No more tweets found, waiting 15 minutes")            
#                print('(until:', dt.datetime.now()+dt.timedelta(minutes=15), ')')
#                time.sleep(15*60)
#                continue
#            else:
             print("No more tweets found")
             break
        
        #==============================================================================
        # only process a result if it has a geolocation    
        #==============================================================================
        for result in new_tweets:    
            if result.geo:
                tweet = dict()
                tweet['user'] = result.user.screen_name
                tweet['text'] = result.text
                tweet['latitude'] = result.geo['coordinates'][0]
                tweet['longitude'] = result.geo['coordinates'][1]
                tweet['created_at'] = result.created_at        
                tweet['id'] = result.id
                tweet['location'] = result.user.location
                tweet['place'] = result.place.country_code
                #==============================================================================
                #  now write this on MongoDB database         
                #==============================================================================
                collection.insert_one(tweet)
                tweetCount += 1
                print("Downloaded {0} tweets loop {2} [last created at: {1}].".format(tweetCount,result.created_at,loop))
        max_id =  new_tweets[-1].id
                
        
        
    except tweepy.TweepError as e:
        # Just exit if any error
        print('exception raised, waiting 15 minutes')
        print('(until:', dt.datetime.now()+dt.timedelta(minutes=15), ')')
        time.sleep(15*60)

print ("\nDownloaded {0} tweets [saved to {1} database]".format(tweetCount, db_name))    