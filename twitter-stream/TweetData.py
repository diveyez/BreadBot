class TweetData:
    def __init__(self, timestamp, linkToTweet, screenName, reTweeted, quoted, content, quotedText):
        self.timestamp = timestamp
        self.linkToTweet = linkToTweet
        self.screenName = screenName
        self.reTweeted = reTweeted
        self.quoted = quoted
        self.content = content
        self.quotedText = quotedText

    def to_string(self):
        return {
            'Timestamp': self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'Link': str(self.linkToTweet),
            'screenName': str(self.screenName),
            'reTweeted': str(self.reTweeted),
            'quoted': str(self.quoted),
            'content': str(self.content),
            'quotedText': str(self.quotedText)
        }

    # Make a pretty discord message
    def prettify(self):
        return "{}\nTweeted By: {}\nLink: {}\n".format(self.content, self.screenName, self.linkToTweet)
