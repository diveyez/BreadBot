from getconfig import load_config
from discord import Webhook, RequestsWebhookAdapter


# Send message to Discord
def send_message_to_discord(message):
    config = load_config('config.json')

    if message.screenName in config["screen_names_to_follow"]:
        webhook = Webhook.from_url(config["discord_webhook"], adapter=RequestsWebhookAdapter())
        webhook.send(message.prettify(), username=message.screenName)
    else:
        pass
