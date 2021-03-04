import tweepy
from StreamListener import StreamListener
from getconfig import load_config


if __name__ == '__main__':
    # Load consumer_key, consumer_secret, access_token, and access_token_secret
    config = load_config('config.json')

    # Authenticate to twitter
    auth = tweepy.OAuthHandler(config["credentials"]["consumer_key"], config["credentials"]["consumer_secret"])
    auth.set_access_token(config["credentials"]["access_token"], config["credentials"]["access_token_secret"])

    # Instantiate api
    api = tweepy.API(auth_handler=auth, wait_on_rate_limit=False)

    # Get twitter users from their screen names
    users = api.lookup_users(screen_names=config["screen_names_to_follow"])

    # Add user IDs of users to array
    user_ids_to_follow = []
    for user in users:
        user_ids_to_follow.append(user.id_str)
        print(f"Following Twitter Account {user.name} ID: {user.id_str}")

    # init stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener, tweet_mode='extended')
    stream.filter(follow=user_ids_to_follow)
