# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 17:42:32 2017

@author: romul
"""
from pymongo import MongoClient
from funcModule import *
import json
from pandas import to_datetime

config = {}
exec(open("./config.py").read(),config)

tweets = getFromMongo(config)

tweetAnalysis = dict()
lst = list()
count = 0
for tweet in tweets:
    count += 1
    tweet['sentiment'] = sentimentScore(tweet['text'])
    tweet['created_at'] = str(to_datetime(tweet['created_at']))
    print('Msg: {0} sentiment tuple {1}'.format(count,tweet['sentiment']))
    if tweet['sentiment'][0] == 0:
        continue
  
  lst.append(tweet)
    
write_tweets(lst, './files/'+config['db_name']+'.json')

print('Analysed {0} tweets and saved {1} tweets with sentiment on {2}.json.'.format(count,len(lst),config['db_name']))
