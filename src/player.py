# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name,current_room,gear):
        self.name = name
        self.current_room = current_room
        self.gear = gear
    def __str__(self):
        return f'Player Name: {self.name}, current_room: {self.current_room}'.format(self=self)
    
