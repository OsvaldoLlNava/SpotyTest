import spotipy
import spotipy.util as util
import pprint

username = '31hzoj7ckzb2dgudlq5zfbudzoia'
scopes= 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read '
clientId='005e25714bad49ab93e394adeabaaa96'
clientSecret='087a97142beb44a18e818424ae2b444c'

token = util.prompt_for_user_token(username,scope=scopes,client_id=clientId,client_secret=clientSecret,redirect_uri='http://google.com/')
sp = spotipy.Spotify(auth=token)
playlist_id = '1AjVQ5uoae04O8bqsvjCMI'
tracks_ids = '7KhsUnH6UelT8Sw6Uu29m7'
results = sp.user_playlist_add_tracks(username, playlist_id, tracks_ids)
sp.user_playlist_add_tracks()
print(results)
#results = sp.current_user_playlists()

#ID playlist = 1AjVQ5uoae04O8bqsvjCMI

#ID cancion afrodita = 7KhsUnH6UelT8Sw6Uu29m7
#username id = 31hzoj7ckzb2dgudlq5zfbudzoia