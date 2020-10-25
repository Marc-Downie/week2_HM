import unittest
from classes.guest import *
from classes.room import *
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Enter Shikari", "Breath in space")
        self.song_2 = Song("Oasis", "Wonderwall")
        self.song_3 = Song("Daft Punk", "Around the world")
        self.song_4 = Song("A-Ha", "Take on me")
        self.song_5 = Song("DevilWearsPrada", "Des moines")

        songs = [self.song_1, self.song_2, self.song_3, self.song_4,self.song_5]


        