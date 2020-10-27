import unittest
from classes.guest import *
from classes.room import *
from classes.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Room_1")
        self.room_2 = Room("Room_2")
        self.guest_1 = Guest("John", "Wonderwall", 20)
        self.guest_2 = Guest("Marc", "Breath in space", 50)
        self.guest_3 = Guest("Linzi", "Around the world", 25)
        self.guest_4 = Guest("Becca", "Take on me", 15)
        self.song = Song("Enter Shikari", "Breath in space")

        # rooms = [self.room_1, self.room_2]

    def test_room_add_guests(self):
        self.room_1.add_guest_in_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guests))

    def test_remove_guests(self):
        self.room_1.add_guest_in_room(self.guest_1)
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEqual([], self.room_1.guests)

    def test_adding_song_to_room(self):
        self.room_1.add_song_to_room(self.song)
        self.assertEqual(1, len(self.room_1.playlist))

    def test_removing_song_from_room(self):
        self.room_1.add_song_to_room(self.song)
        self.room_1.remove_song_from_room(self.song)
        self.assertEqual([], self.room_1.playlist)
