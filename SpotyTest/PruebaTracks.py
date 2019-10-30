import spotipy
import spotipy.util as util
import pprint


class Track():

    def __init__(self,uri_track, name, artist, album, duration):
        self.uri_track = uri_track
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        if self.uri_track != None:
            return  'El track es: {} \nArtista: {} \nAlbum: {}'.format(self.name,self.artist,self.album)
        else:
            return 'El track es: {} \nArtista: {} \nAlbum: {}'.format(self.name,self.artist,self.album)

    def __eq__(self, trackS):
        if trackS.uri_track != self.uri_track:
            return False

        if trackS.name != self.name:
            return False

        if trackS.artist != self.artist:
            return False

        if trackS.album != self.album:
            return False

        if trackS.duration != self.duration:
            return False
        return True

username = '31hzoj7ckzb2dgudlq5zfbudzoia'
scopes= 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read '
clientId='005e25714bad49ab93e394adeabaaa96'
clientSecret='087a97142beb44a18e818424ae2b444c'

token = util.prompt_for_user_token(username,scope=scopes,client_id=clientId,client_secret=clientSecret,redirect_uri='http://google.com/')
sp = spotipy.Spotify(auth=token)

class Spoty():
    def Get_Track(self, nombre, artista):
        if token:
            sp.trace = False
            results = sp.search(q='artist:' + artista + ' track:' +nombre)
            for track in results['tracks']['items']:

                id_track = track['id']
                name = track['name']
                artist = track['artists'][0]['name']
                album = track['album']['name']
                duration = track['duration_ms']
            objectTrack = Track(id_track,name,artist,album,duration)
            return objectTrack
        else:
            print("Can't get token for", token)

    def Get_Track_Id(self,nombre,artista):
        if token:
            sp.trace = False
            results = sp.search(q='artist:' + artista + ' track:' + nombre)
            for track in results['tracks']['items']:
                print(track['name'] + ' - ' + track['artists'][0]['name'])
            return track['id']
        else:
            print("Can't get token for", token)

    def Add_Tracks(self, lista_tracks):
        if token:
            sp.trace = False
            results = sp.current_user_saved_tracks_add(lista_tracks)
            print('Las canciones \n {} \nFueron agregadas'.format(lista_tracks))
        else:
            print("Can't get token for", token)

    def Delete_Tracks(self, lista_tracks):
        if token:
            sp.trace= False
            results = sp.current_user_saved_tracks_delete(lista_tracks)
            print('Las canciones \n {} \nFueron eliminadas'.format(lista_tracks))



if __name__ == '__main__':
    spo = Spoty()

    so = 'the clouds rain'
    ar = 'kheta khan'
    cancioncita = spo.Get_Track(so,ar)
    cancioncita_id = cancioncita.uri_track

    print(cancioncita)
    print('--------------------------------')
    print('ID de la cancion: ',cancioncita_id)

    lista = []
    lista.append(cancioncita_id)
    
    #agregar
    #spo.Add_Tracks(lista)

    #eliminar
    #spo.Delete_Tracks(lista)