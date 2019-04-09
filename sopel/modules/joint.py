# coding=utf-8

"""
joint.py - Module to pass joint vibe as seen on
https://www.youtube.com/watch?v=cvYvxv2qRXU chat
Copyright 2019, Josue Ortega
"""

from sopel import module

PASS_JOINT = '%s le da el ultimo toque al porro y se lo pasa a %s, %d han sido rolados en este canal'
SELF_JOINT = '%s prende un bate. %d han sido encendidos en este canal'
COMMAND_NAME = 'porro'

def setup(bot):
    if 'joint' not in bot.memory:
        bot.memory = {'lighted': 0, 'passed': 0}

@module.commands(COMMAND_NAME)
@module.nickname_commands(COMMAND_NAME)
def joint(bot, trigger):
    payload = trigger.group(2)
    if payload is None:
        bot.memory['joint']['lighted'] += 1 
        joints = bot.memory.get('joint', {}).get('lighted', 1)
        bot.reply(SELF_JOINT % (bot.nick, int(joints)))
        return
    bot.memory['joint']['passed'] += 1 
    joints = bot.memory.get('joint', {}).get('passed', 1)
    bot.reply(PASS_JOINT % (bot.nick, payload, int(joints)))
    return
