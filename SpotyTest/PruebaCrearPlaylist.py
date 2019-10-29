# Creates a playlist for a user
"""
import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util


if len(sys.argv) > 2:
    username = sys.argv[1]
    playlist_name = sys.argv[2]
    playlist_description = sys.argv[3]
else:
    print("Usage: %s username playlist-name playlist-description" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name, playlist_description)
    pprint.pprint(playlists)
else:
    print("Can't get token for", username)

"""


import spotipy
import spotipy.util as util
import pprint

username = '31hzoj7ckzb2dgudlq5zfbudzoia'
scopes= 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read '
clientId='005e25714bad49ab93e394adeabaaa96'
clientSecret='087a97142beb44a18e818424ae2b444c'

token = util.prompt_for_user_token(username,scope=scopes,client_id=clientId,client_secret=clientSecret,redirect_uri='http://google.com/')
sp = spotipy.Spotify(auth=token)
sp.trace = False

playlist_name = input('nombre de la playlist a crear: ')
playlist_description = input('descripcion: ')
playlists = sp.user_playlist_create(username,playlist_name,public=True)
pprint.pprint(playlists)