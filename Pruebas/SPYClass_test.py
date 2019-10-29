import unittest
from spotipy import util
import spotipy
import spotify
from SPYClass import APISFY

class testSpotipy(unittest.TestCase):

    def test_SearchTracks(self):
        track = 'Nada'
        artist = 'Siddhartha'
        res = APISFY.searchTracks(self,track, artist)
        self.assertEqual(res,'5ibjmrFTZDmjMvD3rACrCX')


if __name__ == '__main__':
    unittest.main()