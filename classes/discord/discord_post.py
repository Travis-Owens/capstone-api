# Author: Travis-Owens
# Date: 2020-02-20
# Description: Used to post messages to discord

import json
import requests

import config

class discord_post(object):
    def __init__(self):
        self.headers = { "Authorization":"Bot {}".format(config.DISCORD_BOT_TOKEN),
                        "User-Agent":"KeshBotics (vahkesh.com, v2.1)",
                        "Content-Type":"application/json", }

    def post_message(self, message, discord_channel_ids):
        json_data = json.dumps(message)

        for channel_id in discord_channel_ids:
            discord_message_url = "https://discordapp.com/api/channels/{}/messages".format(channel_id)
            r = requests.post(discord_message_url, headers = self.headers, data = json_data)

    def prepare_message(self, twitch_username, twitch_thumbnail_url):
        twitch_channel_url = 'https://twitch.tv/' + twitch_username
        twitch_channel_preview_url = twitch_thumbnail_url.format(width=640,height=360)


        message = {
              "content": str(twitch_username + " is live on Twitch! " + twitch_channel_url),
              "embed": {
                "title": twitch_channel_url,
                "description": "",
                "url": twitch_channel_url,
                "color": 9442302,
                "timestamp": "",
                "footer": {
                  "icon_url": twitch_channel_preview_url,
                  "text": "KeshBotics"
                },
                "thumbnail": {
                  "url": "https://cdn.discordapp.com/avatars/368199725771390977/c9d101f88d0951730b482c5dcc45f075.png?size=256"
                },
                "image": {
                  "url": twitch_channel_preview_url
                },
                "author": {
                  "name": "KeshBotics",
                  "url": "https://discordapp.com",
                  "icon_url": "https://cdn.discordapp.com/avatars/368199725771390977/c9d101f88d0951730b482c5dcc45f075.png?size=256"
                },
                "fields": [
                          {
                            "name": "Twitch",
                            "value": str(twitch_username + " is live on Twitch!")
                          }
                        ]
              }
            }

        return(message)
