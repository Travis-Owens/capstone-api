#Author: @Travis-Owens
#Date: 2020-3-22

class twitch_handler(object):
    def __init__(self):
        pass

    def get_twitch_user_id(self, twitch_username):
        # Using twitch helix api: convert twitch_username into twitch_user_id
        url = 'https://api.twitch.tv/helix/users?login=' + twitch_username
        resp = requests.get(url, headers={'client-id':config.TWITCH_CLIENT_ID})

        # Check http status code and ensure data is recieved
        if(resp.status_code == 200 and len(resp.json()['data']) > 0):
            return(resp.json()['data'][0]['id'])

        return None

    def update_subscription(self, mode, twitch_user_id):
        if(mode.lower() == 'subscribe' or mode.lower() == 'unsubscribe'):

            headers = {'Content-Type' : 'application/json', 'Client-ID' : config.TWITCH_API_TOKEN}
            data = {"hub.mode":mode.lower(),
                "hub.topic":str("https://api.twitch.tv/helix/streams?user_id=" + twitch_user_id),
                "hub.callback":str(config.WEBHOOK_CALLBACK + "/" + twitch_user_id),
                "hub.lease_seconds":"864000",
                "hub.secret":"top_secret",}

            r = requests.post('https://api.twitch.tv/helix/webhooks/hub', data=json.dumps(data), headers=headers)

            if(r.status_code == 202):
                return(True)
            else:
                return(False)

    def subscribe(self, twitch_user_id):
        return(self.update_subscription('subscribe', twitch_user_id))
