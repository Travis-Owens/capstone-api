# Author: @Travis-Owens
# Date: 2020-01-24
# Description: General public facing API. Twitch, discord, etc

import falcon
import json
from wsgiref import simple_server

# middleware
from middleware.request_logging import request_logging
from middleware.print_x_real_ip import print_x_real_ip

# routes
from routes.twitch.add      import twitch_add
from routes.twitch.delete   import twitch_delete
from routes.twitch.callback import twitch_callback
import routes.twitch.metrics as metrics

class public_facing_api(object):
    def __init__(self):

        self.middleware = [
            {'class': print_x_real_ip()}
        ]

        self.routes = [
            {'route':'/test',                   'class': test()},
            {'route':'/twitch/manage/add',      'class': twitch_add()},
            {'route':'/twitch/manage/delete',   'class': twitch_delete()},
            {'route':'/twitch/callback',        'class': twitch_callback()},
            {'route':'/twitch/callback/{twitch_user_id}', 'class': twitch_callback()},
            {'route':'/twitch/metrics/{twitch_username}', 'class': metrics.twitch_metrics_username()},
            {'route':'/twitch/metrics/id/{twitch_user_id}', 'class': metrics.twitch_metrics_id()},
        ]

        self.app = falcon.API(middleware=[request_logging(), print_x_real_ip()])
        self.setup_routes()
        self.start()

    def setup_middleware(self):
        for middleware in self.middleware:
            self.app.add_middleware(middleware['class'])

    def setup_routes(self):
        for route in self.routes:
            self.app.add_route(route['route'], route['class'])

    def start(self):
        self.httpd = simple_server.make_server('127.0.0.1', 8444, self.app)
        self.httpd.serve_forever()


public_facing_api()
