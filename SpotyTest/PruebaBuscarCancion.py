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


results = sp.current_user_playlists(limit=50)
pprint.pprint(results)