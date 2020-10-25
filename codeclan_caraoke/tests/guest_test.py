import unittest
from classes.guest import *
from classes.room import *
from classes.song import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John", "Wonderwall", 20)
        self.guest_2 = Guest("Marc", "Breath on space", 50)
        self.guest_3 = Guest("Linzi", "Around the world", 25)
        self.guest_4 = Guest("Becca", "Take on me", 15)

        guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]

    def Test_guest_has_name(self):
        self.assertEqual("John", self.guest_1.name)

