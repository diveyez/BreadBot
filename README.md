<p align="center"><a href="https://github.com/deebops/BreadBot" target="_blank"><img src="https://cdn.discordapp.com/avatars/708340506773553173/f8fe7241e415e3fdd4351382bd1a1c5c.png?size=256"></a></p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/python-3.8-blue.svg?style=plastic" alt="Python version"></a>
    <a href="https://github.com/deebops/BreadBot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/deebops/BreadBot?style=plastic" alt="GitHub license"></a>
    <a href="https://github.com/deebops/BreadBot/issues"><img src="https://img.shields.io/github/issues/deebops/BreadBot?style=plastic" alt="GitHub issues"></a>
    <a href="https://github.com/deebops/BreadBot/pulls"><img src="https://img.shields.io/github/issues-pr/deebops/BreadBot?style=plastic" alt="GitHub pull requests"></a>
    <br /><a href="https://github.com/deebops/BreadBot/stargazers"><img src="https://img.shields.io/github/stars/deebops/BreadBot?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/deebops/BreadBot/network/members"><img src="https://img.shields.io/github/forks/deebops/BreadBot?style=social" alt="GitHub forks"></a>
    <a href="https://github.com/deebops/BreadBot"><img src="https://img.shields.io/github/watchers/deebops/BreadBot?style=social" alt="GitHub watchers"></a>
</p>

# About

BreadBot is an all in one trading discord bot used in the Breadstackers and Breadstackers Crypto discord servers. 

# Features
- Finviz Data scrapping using the [finviz](https://github.com/mariostoev/finviz) python library.
- ShortSqueeze Data retrieval.
- Live twitter feed using the [tweepy](https://github.com/tweepy/tweepy) libary.
> 💡 Got a feature idea? Open an [issue](https://github.com/deebops/BreadBot/issues/new)


# Usage 

## Finviz API

- Command `.{tickername}`

  Example:
  ![image](https://user-images.githubusercontent.com/11996230/109452043-7c672080-7a14-11eb-8320-f4c320e99adf.png)

## ShortSqueeze Scrapper

### Retrieves data from shortsqueeze.com

- Command `.ss {tickername}`

  Example:
  ![image](https://i.ibb.co/GFq9VXm/image.png)

## Twitter Stream

** In Progress **


# Setup

Rename `config.py` to `config.py` and populate with your configuration

```
token = "<discord bot token>"
channel = ["<channelName>","<secondchannelname>"] # Channels in here will be used by BreadBot to respond. Example: ['breadbot','breadbottest']
```

Install Python dependencies and run

```
pip3 install -r requirements.txt
python3 breadbot.py
```

# Developer? Feel free to contribute!

All kinds of contributions are welcome. 

`⭐️ star` this project to show your support or feel free to raise an [`🐞 issue`](https://github.com/deebops/BreadBot/issues/new)