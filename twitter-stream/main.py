import tweepy
from StreamListener import StreamListener
import json
from getconfig import load_config

# def load_config(config_file):
#     with open(config_file) as json_file:
#         data = json.load(json_file)
#     return data


if __name__ == '__main__':
    config = load_config('config.json')
    # Authorize and init api
    auth = tweepy.OAuthHandler(config["credentials"]["consumer_key"], config["credentials"]["consumer_secret"])
    auth.set_access_token(config["credentials"]["access_token"], config["credentials"]["access_token_secret"])
    api = tweepy.API(auth_handler=auth, wait_on_rate_limit=False)

    # init stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener, tweet_mode='extended')
    stream.filter(follow=config["twitter_ids_to_follow"])
