import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys

# add your twitter app details
def load_api():
    ''' Function that loads the twitter API after authorizing
        the user. '''

    CONSUMER_KEY = "q19KDEViDMNsBh1wjUjD3TNvF"
    CONSUMER_SECRET = "W14UMa3DU1H2HIcv96dpA7gOQOkJYtYPL1fywNkJMl5rnMwT7v"
    ACCESS_TOKEN = "115216526-hphcEh4FwJZ9x1wuhRfe1Osl7d5i6aFVCuhkPlQc"
    ACCESS_TOKEN_SECRET = "iMw6aJbBpJGQZm72CsCZiAOrNQUAtBMW2XqKdmBzauhgZ"
    # app auth
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # load the twitter API via tweepy
    return tweepy.API(auth)

def tweet_search(api, query, max_tweets, max_id, since_id, geocode):
    ''' Function that takes in a search string 'query', the maximum
        number of tweets 'max_tweets', and the minimum (i.e., starting)
        tweet id. It returns a list of tweepy.models.Status objects. '''

    searched_tweets = []
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=remaining_tweets,
                                    since_id=str(since_id),
                                    max_id=str(max_id-1))
#                                    geocode=geocode)
            print('found',len(new_tweets),'tweets')
            if not new_tweets:
                print('no tweets found')
                break
            searched_tweets.extend(new_tweets)
            max_id = new_tweets[-1].id
        except tweepy.TweepError:
            print('exception raised, waiting 15 minutes')
            print('(until:', dt.datetime.now()+dt.timedelta(minutes=15), ')')
            time.sleep(15*60)
            break # stop the loop
    return searched_tweets, max_id


# get tweets from previous tweets
def get_tweet_id(api, date='', days_ago=9, query='a'):
    ''' Function that gets the ID of a tweet. This ID can
        then be used as a 'starting point' from which to
        search. The query is required and has been set to
        a commonly used word by default. The variable
        'days_ago' has been initialized to the maximum amount
        we are able to search back in time (9).'''

    if date: # return an ID from the start of the given day
        td = date + dt.timedelta(days=1)
        tweet_date = '{0}-{1:0&amp;gt;2}-{2:0&amp;gt;2}'.format(td.year, td.month, td.day)
        tweet = api.search(q=query, count=1, until=tweet_date)
    else:
        # return an ID from __ days ago
        td = dt.datetime.now() - dt.timedelta(days=days_ago)
        tweet_date = '{0}-{1:0&amp;gt;2}-{2:0&amp;gt;2}'.format(td.year, td.month, td.day)
        # get list of up to 10 tweets
        tweet = api.search(q=query, count=10, until=tweet_date)
        print('search limit (start/stop):',tweet[0].created_at)
        # return the id of the first tweet in the list
        return tweet[0].id


# Save result to JSON
def write_tweets(tweets, filename):
    ''' Function that appends tweets to a file. '''

    with open(filename, 'a') as f:
        for tweet in tweets:
            json.dump(tweet._json, f)
            f.write('\n')
###############################################################
load_api()


# get user data
#user = api.me()

#print('Name: ' + user.name)
#print('Location: ' + user.location)
#print('Friends: ' + str(user.friends_count))
