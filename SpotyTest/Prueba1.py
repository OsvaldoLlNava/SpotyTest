import spotipy
import spotipy.util as util

util.prompt_for_user_token('31hzoj7ckzb2dgudlq5zfbudzoia','user-library-read',client_id='005e25714bad49ab93e394adeabaaa96',client_secret=' 087a97142beb44a18e818424ae2b444c',redirect_uri='http://google.com/')
#util.prompt_for_user_token()
#birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify()

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])