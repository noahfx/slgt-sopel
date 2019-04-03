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
    twit = get_text(bot, t_uid)
    if twit is not None:
        bot.say(get_text(bot, t_uid))

def get_text(bot, twit_uid):
    client = Twython(bot.config.twitter.public, bot.config.twitter.secret)
    try:
        twit = client.show_status(id=twit_uid, tweet_mode='extended')
        return twit.get('full_text')
    except:
        return None
    
@module.commands('tuiter')
@module.nickname_commands('tuiter')
@module.example('!tuiter pull tio_chema')
def pull(bot, trigger):
    action = trigger.group(3)
    user = trigger.group(4)
    index = trigger.group(5) or 0

    if action is None:
        bot.reply('Comando mal hecho, falta la accion, formato: tuiter pull tio_chema')
        return
    if user is None:
        bot.reply('Comando mal hecho, falta el usuario, formato: tuiter pull tio_chema')
        return

    client = Twython(bot.config.twitter.public, bot.config.twitter.secret)
    try:
        i = int(index)
        c = i + 1
        twit = client.get_user_timeline(screen_name=user, count=c)[i]
        bot.reply(twit.get('text'))
    except:
        bot.reply('No encontre twits para este usuario!')
