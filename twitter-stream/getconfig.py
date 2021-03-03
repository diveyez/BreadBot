import json


def get_twitter_ids(usernames):
    print(usernames)


def load_config(config_file):
    with open(config_file) as json_file:
        data = json.load(json_file)

    get_twitter_ids(data["usernames_to_follow"])
    return data
