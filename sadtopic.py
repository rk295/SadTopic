#!/usr/bin/env python
import twitter
from hypchat import HypChat
import os

consumer_key=os.environ['CONSUMER_KEY']
consumer_secret=os.environ['CONSUMER_SECRET']
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']

hc_room_id=os.environ['HC_ROOM_ID']
hc_token=os.environ['HC_TOKEN']
hc_server=os.environ['HC_SERVER']

twitter_user=os.environ['TWITTER_USER']

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

statuses = api.GetUserTimeline(screen_name=twitter_user)
latest_status = statuses[0].text

print "Latest tweet=%s" % latest_status

hc = HypChat(hc_token, endpoint=hc_server)
room = hc.get_room(hc_room_id)
topic = room['topic']

print "Current topic=%s" % topic

if topic != latest_status:
    print "Topic doesn't match, setting to: %s" % latest_status
    room.topic(latest_status)
else:
    print "Topic is already set to latest tweet, ignoring"
    pass
