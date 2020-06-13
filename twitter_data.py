import json
import tweepy
import pandas as pd
from tweepy import OAuthHandler
from pandas.io.json import json_normalize
import io,sys

consumer_key = 'lPeOiUZkqnuBOVTYbl0PUT83D'
consumer_secret = '39CxtEl4E4jWaz3Fo7FhED7AuLP4aQviVebxoFLhycqpt7a1vV'
access_token = '450619780-lxEtsw3lAzocHGhj9fvuTCSuSRhhfZIdXkYRQ0xA'
access_token_secret = 'zGTAfvn38jCJiOUR9iLbFZ1cGZXIhIcR8JeudM8mbb44t'
# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth,wait_on_rate_limit=True)

def get_tweets(query, outloc, count):
    q=str(query)
    ol = str(outloc)
    fetched_tweets = api.search(q, count = count)

    dfflat = pd.DataFrame()
    df_user_replies = pd.DataFrame()

    for tweet in fetched_tweets:
        df_for_tweet = json_normalize(tweet._json)
        dfflat=dfflat.append(df_for_tweet,ignore_index=True,sort=True)

        tweet_id = tweet.user.id
        username = tweet.user.name

        replies = api.search(q='to:{}'.format(username),
                                since_id=tweet_id, tweet_mode='extended')
        for i in replies:
            rep_tweet = json_normalize(i._json)
            df_user_replies=df_user_replies.append(rep_tweet,ignore_index=True,sort=True)
        dfflat.to_csv(ol+'\\user_tweet.csv', header=True, index=False, sep='|')
    df_user_replies.to_csv(ol+'\\user_tweet_replies.csv', header=True, index=False, sep='|')


    return "Sucess"


if __name__ == "__main__":
    twitter_topic = sys.argv[1]
    output_location = sys.argv[2]
    tweets = get_tweets(query =twitter_topic, outloc=output_location, count = 2000)