# coding=utf-8

"""
twitter.py - API-key-less twitter module for Sopel
Copyright 2019, Josue Ortega
"""

import re

from twython import Twython
from sopel import module

twitter_regex = r'((http|https)://(twitter.com)/(([A-Za-z0-9_]{1,15})/status)/([\d]*))'
twitter_pattern = re.compile(twitter_regex)

def setup(bot):
    bot.register_url_callback(twitter_pattern, twit)

@module.rule(twitter_regex)
def twit(bot, trigger):
    groups = trigger.group(0)
    s_groups = groups.split('/')
    t_uid = s_groups[len(s_groups)-1:][0]
    bot.say(get_text(bot, t_uid))

def get_text(bot, twit_uid):
    client = Twython(bot.config.twitter.public, bot.config.twitter.secret)
    twit = client.show_status(id=twit_uid, tweet_mode='extended')
    return twit.get('full_text')
