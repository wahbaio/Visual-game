from room import Room
from character import Enemy
dead = False
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room, buzzing with flies")

ballroom = Room("Ballroom")
ballroom.set_description("A fancy ballroom")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A fancy dining hall")

# This links the kitchen to the dining hall
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dining_hall.set_character(dave)

dave.set_conversation("Hi my name is Dave, Id like to eat your brain.")
dave.set_weakness("cheese")
dave.set_inventory("cheese")
dave.steal("cheese")
print("What will fight with?")
fight_with = input("\n> ")
dave.fight(fight_with)


current_room = kitchen
while dead == False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Which direction would you like to go? North, east, south, west")
    command = input("\n> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                # What happens if you lose?
                print("Oh dear, you lost the fight.")
                dead = True
        else:
            print("There is no one here to fight with")
