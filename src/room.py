# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return self.name + self.description
    def get_room_name(self):
        return self.name
    def get_room_description(self):
        return self.description
    