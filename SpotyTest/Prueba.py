import spotipy
import spotipy.util as util
"""
spotify = spotipy.Spotify()
util.prompt_for_user_token('31hzoj7ckzb2dgudlq5zfbudzoia','user-library-read',client_id='005e25714bad49ab93e394adeabaaa96',client_secret=' 087a97142beb44a18e818424ae2b444c',redirect_uri='http://google.com/')
results = spotify.search(q='artist:' + 'Radiohead', type='artist')
print(results)
"""
#Aqui le meti todos los scopes permitidos para evitar jaleo
scopes= 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read '
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
token = util.prompt_for_user_token('31hzoj7ckzb2dgudlq5zfbudzoia',scope=scopes,client_id='005e25714bad49ab93e394adeabaaa96',client_secret='087a97142beb44a18e818424ae2b444c',redirect_uri='http://google.com/')
spotify = spotipy.Spotify(auth=token)
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url']) 
    print('cover art: ' + track['album']['images'][0]['url']) 
    print()

print('---------------------------')
print(results['tracks'][1]['name'])
print(results['tracks'][1]['id'])
print(results['tracks'][3]['external_urls'])