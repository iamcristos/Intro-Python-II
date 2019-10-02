# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,room):
        self.room = room
    def current_room(self):
        return self.room
    def set_room(self,new_room):
        self.room = new_room
        return self.room
