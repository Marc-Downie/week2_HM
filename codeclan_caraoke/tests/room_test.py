import unittest
from classes.guest import *
from classes.room import *
from classes.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Room_1", 4)
        self.room_2 = Room("Room_2", 2)

        rooms = [self.room_1, self.room_2]

    def test_room_has_guests(self):
        self.assertEqual("John", self.room_1.guests)

    # def test_remove_guests(self):
    #     self.assertEqual(0, self.room_1.size)

    # def add_song_to_room(self):
    #     self.assertEqual("Breath in space", self.song_1.song_name)

    
