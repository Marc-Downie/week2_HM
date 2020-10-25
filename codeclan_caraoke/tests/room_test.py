import unittest
from classes.guest import *
from classes.room import *
from classes.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Room_1", 4)
        self.room_2 = Room("Room_2", 2)

        rooms = [self.room_1, self.room_2]

    def Test_room_has_guests(self):
        self.assertEqual(1, self.room.guests)

    def Test_remove_guest(self):
        self.assertEqual(0, self.room.guests)
