# Create the Character class
from item import *


class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.inventory = []

    # Describe the character
    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)
    # Set what this character will say when talked to

    def name(self):
        print(self.name)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_inventory(self, inventory):
        self.inventory += inventory

    def show_inventory(self):
        if self.inventory:
            print(f"{self.name}'s inventory:")
            for item in self.inventory:
                print(item.name)  # Print the name of each item
        else:
            print(f"{self.name} has no items in their inventory.")

    # Talk to the character
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")
    # Fight the eenemy

    def fight(self, combat_item):
        print(f"{self.name} does not want to fight you.")
        return True


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.char_weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off, using {combat_item}.")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    def steal(self, item):
        if item in self.inventory:
            print(f"You steal from {self.name}")
            self.inventory -= item


class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(f"{self.name} hugs you back!")

    # What other methods could your Friend class have?
