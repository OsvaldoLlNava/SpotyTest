import os
import spotipy
import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

#Get username from terminal
username ='31hzoj7ckzb2dgudlq5zfbudzoia'
scopes ='playlist-modify-private playlist-read-private playlist-modify-public'
clientId ='005e25714bad49ab93e394adeabaaa96'
clientSecret='087a97142beb44a18e818424ae2b444c'
redirect='http://google.com/'


#username ID =31hzoj7ckzb2dgudlq5zfbudzoia
token = util.prompt_for_user_token(username,scope=scopes,client_id=clientId,client_secret=clientSecret,redirect_uri=redirect)



sp = spotipy.Spotify(auth=token)

user = sp.current_user()
print(json.dumps(user, sort_keys=True, indent=4))

