class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.size = 0
        self.guests = []
        self.playlist = []

    def add_guest_in_room(self, guest):
        self.guests.append(guest)

    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)
        
    def add_song_to_room(self, song):
        self.playlist.append(song)

    def remove_song_from_room(self, song):
        self.playlist.remove(song)
