from room import Room
from player import Player
import random
# Declare all the rooms

potential = ["knife","chestplate","gold","skull"]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.",f'{random.choice(potential)}'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",f'{random.choice(potential)}'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",f'{random.choice(potential)}'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",f'{random.choice(potential)}'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",f'{random.choice(potential)}'),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
Player_one = Player("Joshua",room['outside'],)
# print(Player_one.gear)
# print(Player_one.current_room.item)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print(Player_one.current_room)
while True:
    print("N,S,W,E for movement. I for inventory. Q to quit.")
    cmd = input("-> ").lower()
    if cmd in ["n", "s", "e", "w"]:
        # Move to that room
        Player_one.travel(cmd)
    elif cmd in ["take"]:
        Player_one.take_item(Player_one.current_room.item)
        # stores item in player inv.removes from room.
        print(f"current inventory: {Player_one.gear}")
        print(Player_one.current_room)
    elif cmd in ["drop"]:
        Player_one.drop_item(Player_one.gear)
        print(f"current inventory: {Player_one.gear}")
        print(Player_one.current_room)
        # drops item from player inv.drops in room.
    elif cmd in ["i"]:
        print(f"current inventory: {Player_one.gear}")
    elif cmd == "q":
        print("Goodbye!")
        exit()
    else:
        print("I did not understand that command.")
    
    
    
    




