# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name,description,item):
        self.name = name
        self.description = description
        self.item = item
    def __str__(self):
        return f'{self.name}, {self.description}, {self.item}'.format(self=self)
        