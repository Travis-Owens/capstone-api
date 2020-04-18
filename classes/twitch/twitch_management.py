# Author: @Travis-Owens
# Date:   2020-02-16
# Description: used for adding/deleting twitch channels from the db

import falcon
import json
import requests

import config
from classes.data_handler import data_handler

class twitch_management(object):
    def __init__(self, twitch_username, discord_channel_id):
        self.db     = data_handler()
        self.twitch = twitch_handler()

        self.twitch_username    = twitch_username
        self.discord_channel_id = discord_channel_id
        self.twitch_user_id     = self.twitch.get_twitch_user_id(twitch_username)


    def add(self):
        if(self.twitch_user_id == None):
            return("Twitch username is invalid!")

        if(len(self.db.defined_select('unique_twitch_notification', [self.twitch_username, self.discord_channel_id])) != 0):
            return("Notification already exist!")

        subscribe_status = self.twitch.subscribe(self.twitch_user_id)

        if(subscribe_status == True):
            db_status        = self.db.defined_insert('add_twitch_notification', [self.twitch_username, self.twitch_user_id, self.discord_channel_id])
        else:
            return("Error subscribing to twitch service!")

        if(db_status == True):
            return("Notification successfully added!")
        else:
            return("Error saving notifiaction to database!")


    def delete(self):
        if(self.twitch_user_id == None):
            return("Twitch username is invalid!")

        db_status = self.db.defined_delete('delete_twitch_notification', [self.twitch_username, self.twitch_user_id, self.discord_channel_id])

        if(db_status == True):
            return("Notification successfully removed!")
        else:
            return("Error removing notifiaction!")
