import requests
import spotipy.util as util

username ='31hzoj7ckzb2dgudlq5zfbudzoia'
scopes ='playlist-read-private user-read-private'
clientId ='005e25714bad49ab93e394adeabaaa96'
clientSecret='087a97142beb44a18e818424ae2b444c'
redirect='http://google.com/'


#username ID =31hzoj7ckzb2dgudlq5zfbudzoia
token = util.prompt_for_user_token(username,scope=scopes,client_id=clientId,client_secret=clientSecret,redirect_uri=redirect)

id ='11dFghVXANMlKmJXsNCbNl' #cut the feeling
response = requests.get('https://api.spotify.com/v1/tracks/{id}',token)

print(response)
