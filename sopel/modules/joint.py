# coding=utf-8

"""
joint.py - Module to pass joint vibe as seen on
https://www.youtube.com/watch?v=cvYvxv2qRXU chat
Copyright 2019, Josue Ortega
"""

from sopel import module

PASS_JOINT = '%s le da el ultimo toque al porro y luego de llenar toda la sala de humo blanco se lo pasa a %s, %d porros han sido rolados en este canal'
SELF_JOINT = '%s prende un bate de la deliciosa hierbita. %d porros han sido encendidos en este canal'
COMMAND_NAME = 'porro'


def initialize_db(bot, channel, key):
    if bot.db.get_channel_value(channel, key) is None:
        bot.db.set_channel_value(channel, key, 1)
    return

def update_db(bot, channel, key):
    value = bot.db.get_channel_value(channel, key) or 0 #for some reason setup is not initialzint db
    new_val = value + 1
    bot.db.set_channel_value(channel, key, new_val)
    return new_val

def setup(bot):
    for c in bot.channels:
        for k in ['passed', 'lit']:
            initialize_db(bot=bot, channel=c, key=k)

@module.commands(COMMAND_NAME)
@module.nickname_commands(COMMAND_NAME)
def joint(bot, trigger):
    payload = trigger.group(2)
    if payload is None:
        joints = update_db(bot, trigger.sender, 'lit')
        bot.reply(SELF_JOINT % (trigger.nick, joints))
        return
    joints = update_db(bot, trigger.sender, 'passed')
    bot.say(PASS_JOINT % (trigger.nick, payload, joints))
    return
