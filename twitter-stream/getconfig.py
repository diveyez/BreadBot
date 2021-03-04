import json
import sys


def load_config(config_file):
    with open(config_file) as json_file:
        data = json.load(json_file)

    return data

# load_config("config.json")
