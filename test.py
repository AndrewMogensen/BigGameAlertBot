#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = "ISU: 35, OKST: 34"

credentials = {}

with open("App.config") as config:
    for line in config:
        (key, val) = line.strip().split('=')
        credentials[key] = val

api = Twython(credentials['apiKey'], credentials['apiSecret'], credentials['accessToken'],
              credentials['accessTokenSecret'])

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
