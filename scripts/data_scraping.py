import tweepy
import numpy as np
import pandas as pd
import json

consumer_key = CCgRHmMGyvDFuMF696T1tzwAK
consumer_secret = bj6UZN6RbeJRx4BwfIqHqRXUxSSGhdIE0DG3dIog9PwqWXM59h

access_token = 2763428823-XKtSLFg6MRzMWaU6i6uhjjTtcFeFSXpDpBZu4cu
access_token_secret = sxV9k4fCaRXYsoL8QTMSUHaWVlxDpzste34G2RzLVJ7zT

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


hashtags = ['#NHL', '#NJDevils', '#NYR', '#Isles', '#CBJ', '#LetsGoFlyers',
    '#LetsGoPens', '#ALLCAPS', '#CauseChaos', '#NHLBruins', '#LetsGoBuffalo',
    '#GoHabsGo', '#GoBolts', '#TimeToHunt', '#LGRW', '#GoSensGo',
    '#LeafsForever', '#Blackhawks', '#TexasHockey', '#Preds', '#STLPreds',
    '#GoAvsGo', '#mnwild', '#Yotes', '#GoJetsGo', '#LetsGoOilers',
    '#Flames', '#Canucks', '#SeaKraken', '#VegasBorn', '#SJSharks',
    '#GoKingsGo', '#FlyTogether']
start_date = '2023-10-01'
end_date = '2024-08-31'
query = ' OR '.join(hashtags)

# Collect tweets
tweets = tweepy.Cursor(api.search, q=query, since=start_date, until=end_date, tweet_mode='extended').items()

# Save tweets to file
with open('tweets.json', 'w') as f:
    for tweet in tweets:
        f.write(json.dumps(tweet._json) + '\n')