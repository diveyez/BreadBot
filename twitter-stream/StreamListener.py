import tweepy
import sys

from TweetData import TweetData
from getconfig import load_config
from sendToDiscord import send_message_to_discord

config = load_config('config.json')


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.id_str)

        # Construct link to tweet
        tweet_link = f"https://twitter.com/{status.user.screen_name}/status/{status.id_str}"

        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

        # check if text has been truncated
        if hasattr(status, "extended_tweet"):
            text = status.extended_tweet["full_text"]
        else:
            text = status.text

        # check if this is a quote tweet.
        is_quote = hasattr(status, "quoted_status")
        quoted_text = ""
        if is_quote:
            # check if quoted tweet's text has been truncated before recording it
            if hasattr(status.quoted_status, "extended_tweet"):
                quoted_text = status.quoted_status.extended_tweet["full_text"]
            else:
                quoted_text = status.quoted_status.text

        # remove characters that might cause problems with csv encoding
        remove_characters = [",", "\n"]
        for c in remove_characters:
            text.replace(c, " ")
            quoted_text.replace(c, " ")

        tweet = TweetData(status.created_at, tweet_link, status.user.screen_name, is_retweet, is_quote, text,
                          quoted_text)

        send_message_to_discord(tweet)

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
        else:
            # returning non-False reconnects the stream, with backoff.
            return True
