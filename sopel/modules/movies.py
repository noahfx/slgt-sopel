# coding=utf-8

"""
imdb.py - IMDB module for Sopel
Copyright 2019, Josue Ortega
"""

from imdb import IMDb
from sopel import module


MOVIE_NOT_FOUND = 'No encontré la pelicula %s'
FAILED_MOVIE_SEARCH = 'Algo salio mal'
ACTION_IS_NONE = 'Comando mal hecho falta palabra clave `search` @imdb search pelicula'
MOVIE_IS_NONE = 'Comando mal hecho falta nombre de la pelicula `` @imdb pelicula'
ACTION_NOT_SUPPORTED = 'Accion %s no soportada'

@module.commands('imdb')
@module.nickname_commands('imdb')
def imdb(bot, trigger):
    payload = trigger.group(2)
    if payload is None:
        bot.reply(MOVIE_IS_NONE)
        return
    try:
        ia = IMDb()
        bot.reply(search(ia, payload))
    except:
        bot.reply(FAILED_MOVIE_SEARCH)

def search(ia, payload):
    movies = ia.search_movie(payload)
    if movies is None:
        return MOVIE_NOT_FOUND % payload
    if len(movies) == 0:
        return MOVIE_NOT_FOUND % payload
    _id = movies[0].getID()
    movie = ia.get_movie(str(_id))
    if movie is None:
        return MOVIE_NOT_FOUND % payload
    return '%(year)s %(title)s %(plot outline)s - Rating: %(rating)s' % movie
