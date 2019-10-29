
class Track():

    def __init__(self,uri_track, name, artist, album, duration):
        self.uri_track = uri_track
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        if self.uri_track != None:
            return str(f"El track es:"+"\n"+f"Name -> {self.name}"
                       +"\n"+f"Artist -> {self.tags}"+
                       "\n"+f"Album -> {self.album}"+"\n")
        else:
            return str(f"El track es:" + "\n" + f"Name -> {self.name}"
                       + "\n" + f"Artist -> {self.tags}" +
                       "\n" + f"Album -> {self.album}" + "\n")

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