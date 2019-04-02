# coding=utf-8

"""
twitter.py - API-key-less Instagram module for Sopel
Copyright 2019, Josue Ortega
"""

import re

from twython import Twython

twitter_regex = r'((http|https)://(twitter.com)/(([A-Za-z0-9_]{1,15})/status)/([\d]*))'
twitter_pattern = re.compile(twitter_regex)

def setup(bot):
    bot.register_url_callback(instagram_pattern, twit)

@module.rule(twitter_regex)
def twit(bot, trigger):
    groups = trigger.group(0)
    t_uid = groups[-1]
    bot.say(get_text(twit_uid))

def get_text(twit_uid):
    client = Twython(bot.config.twitter.public, bot.config.twitter.secret)
    twit = client.show_status(id=twit_uid, tweet_mode='extended')
    return twit.get('full_text')
