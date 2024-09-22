import time
import random
import threading

class Game:
    def __init__(self):
        self.inventory = {}  # Inventory as a dictionary now
        self.game_over = False
        self.current_location = self.entrance
        self.player_input = None

    def display_inventory(self):
        if self.inventory:
            inventory_items = [f"{item} ({count})" for item, count in self.inventory.items()]
            print("\nYour inventory: " + ", ".join(inventory_items))
        else:
            print("\nYour inventory is empty.")

    def add_to_inventory(self, item, count=1):
        if item in self.inventory:
            self.inventory[item] += count
        else:
            self.inventory[item] = count

    def remove_from_inventory(self, item, count=1):
        if item in self.inventory:
            self.inventory[item] -= count
            if self.inventory[item] <= 0:
                del self.inventory[item]

    def has_item(self, item):
        return item in self.inventory and self.inventory[item] > 0

    def entrance(self):
        while True:
            print("\nYou are at the entrance of a mysterious castle.")
            print("To the west is the forest, to the east is the courtyard, and to the north is a small village.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "west":
                return self.forest
            elif choice == "east":
                return self.courtyard
            elif choice == "north":
                return self.village
            else:
                print("I don't understand this choice.")

    def village(self):
        while True:
            print("\nYou have arrived at a peaceful village.")
            print("To the south is the entrance of the castle.")
            print("You can explore the 'market' or visit the 'tavern'.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "south":
                return self.entrance
            elif choice == "market":
                return self.market
            elif choice == "tavern":
                return self.tavern
            else:
                print("I don't understand this choice.")

    def market(self):
        while True:
            print("\nYou are at the bustling village market.")
            print("You can 'buy' items or go 'back' to the village.")
            print("Available items for purchase: 'map' (100 gold), 'sword' (20 gold).")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "back":
                return self.village
            elif choice == "buy":
                item = str.lower(input("Which item would you like to buy? "))
                if item == "map":
                    if self.has_item("map"):
                        print("You already have a map.")
                    else:
                        if self.has_item("gold") and self.inventory["gold"] >= 100:
                            self.remove_from_inventory("gold", 100)
                            self.add_to_inventory("map")
                            print("You bought a map.")
                        else:
                            print("You don't have enough gold.")
                elif item == "sword":
                    if self.has_item("sword"):
                        print("You already have a sword.")
                    else:
                        if self.has_item("gold") and self.inventory["gold"] >= 20:
                            self.remove_from_inventory("gold", 20)
                            self.add_to_inventory("sword")
                            print("You bought a sword.")
                        else:
                            print("You don't have enough gold.")
                else:
                    print("That item is not available.")
            else:
                print("I don't understand this choice.")

    def tavern(self):
        while True:
            print("\nYou are in the lively tavern.")
            print("You can 'talk' to the bartender, 'play' a game of chance, or go 'back' to the village.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "back":
                return self.village
            elif choice == "talk":
                if self.has_item("blessing") and not self.has_item("boat_pass"):
                    print("Bartender: I see you have been blessed by the wizard. Here, take this boat pass.")
                    self.add_to_inventory("boat_pass")
                else:
                    print("Bartender: Beware of the dangers that lie ahead. The map can guide you.")
            elif choice == "play":
                print("You play a game of chance.")
                if random.randint(1, 2) == 1:
                    print("You won 10 gold!")
                    self.add_to_inventory("gold", 10)
                else:
                    print("You lost the game. The bartender takes 5 gold as consolation.")
                    self.remove_from_inventory("gold", 5)
            else:
                print("I don't understand this choice.")

    def forest(self):
        while True:
            print("\nYou are in a dark forest.")
            print("To the east is the entrance of the castle.")
            print("You hear rustling in the bushes.")
            print("You can 'search' for items or 'explore' the forest.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "search":
                if self.has_item("key"):
                    print("There's nothing else to find here.")
                else:
                    print("You found a shiny key on the ground.")
                    self.add_to_inventory("key")
            elif choice == "east":
                return self.entrance
            elif choice == "explore":
                if self.has_item("sword"):
                    print("A wild wolf appears! You use your sword to scare it away.")
                    print("You found many gold on the ground.")
                    self.add_to_inventory("gold", 50)
                else:
                    print("A wild wolf appears! Without a weapon, you cannot defend yourself.")
                    print("The wolf attacks you. You are dead.")
                    self.game_over = True
                    return None
            else:
                print("I don't understand this choice.")

    def courtyard(self):
        while True:
            print("\nYou are in a large courtyard.")
            print("To the west is the entrance of the castle, and to the east is the castle's gate.")
            print("There is a guard in front of the gate.")
            print("You notice a strange 'statue' here.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "west":
                return self.entrance
            elif choice == "statue":
                print("The statue has an inscription: 'Only those who solve my riddle may proceed.'")
                riddle_answer = str.lower(input("What has keys but can't open locks? "))
                if riddle_answer == "piano":
                    print("The statue moves aside, revealing a hidden passage.")
                    return self.hidden_passage
                else:
                    print("That's not the correct answer.")
            elif choice == "talk":
                print("Guard: To enter the castle, you need the key.")
            elif choice == "east":
                if self.has_item("key"):
                    print("You show the key to the guard and he lets you pass.")
                    return self.gate
                else:
                    print("The guard stops you. You need the key to proceed.")
            else:
                print("I don't understand this choice.")

    def hidden_passage(self):
        while True:
            print("\nYou are in a hidden passage beneath the courtyard.")
            print("It's dark and eerie.")
            print("You can go 'forward' or go 'back' to the courtyard.")
            self.display_inventory()

            if self.has_item("map"):
                print("Your map shows a safe path through the passage.")

            choice = str.lower(input("What would you like to do? "))

            if choice == "back":
                return self.courtyard
            elif choice == "forward":
                print("You encounter a sleeping dragon!")
                if self.has_item("sword"):
                    return self.dragon_fight()  # Initiate dragon fight if player has sword
                else:
                    print("Without a weapon, you cannot defeat the dragon.")
                    print("The dragon wakes up and burns you to ashes.")
                    self.game_over = True
                    return None
            else:
                print("I don't understand this choice.")

    def _get_input(self):
        self.player_input = input().lower()

    def dragon_fight(self):
        print("You have woken the dragon! It roars and prepares to attack.")
        keys = ['f', 'g', 'h', 'j', 'k']  # Keys the player will have to press
        fight_rounds = 5  # Number of rounds to fight the dragon
        succ_words = ['You dodge the dragon\'s attack!', 
                      'You strike the dragon!', 
                      'You block the dragon\'s attack!',
                      'You counter the dragon\'s attack!',
                      'You get a critical hit on the dragon!']

        for round_number in range(fight_rounds):
            required_key = random.choice(keys)
            print(f"\nRound {round_number + 1}: You must press '{required_key}' in 5 seconds!")

            self.player_input = None
            input_thread = threading.Thread(target=self._get_input)
            input_thread.start()

            # Countdown loop
            for remaining_time in range(5, 0, -1):
                print(f"Time left: {remaining_time} seconds", end="\r", flush=True)
                time.sleep(1)

                # If the player has inputted a key, break the countdown loop
                if self.player_input is not None:
                    break

            input_thread.join(timeout=0)  # Ensure input thread is finished

            # Check if player input is correct and within the time limit
            if self.player_input == required_key:
                print(succ_words[random.randint(0, 4)])
            else:
                print("\nYou failed to hit the dragon. The dragon burns you to ashes!")
                self.game_over = True
                return None  # Player dies, exit the fight

        # If player survives all rounds
        print("You have defeated the dragon! You found a treasure chest filled with gold.")
        self.add_to_inventory("gold", 5000)
        return self.treasure_room

    def treasure_room(self):
        print("\nYou have found the hidden treasure room filled with gold and jewels.")
        print("You are now the richest person in the land. You win!")
        self.display_inventory()
        print("Thank you for playing!")
        self.game_over = True
        return None

    def gate(self):
        while True:
            print("\nYou are in front of the castle's gate.")
            print("To the west is the courtyard, and to the north is the river.")
            print("You can also try to 'enter' the castle if you have the key.")
            print("There is a 'tower' to the south.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "west":
                return self.courtyard
            elif choice == "north":
                return self.river
            elif choice == "enter":
                if self.has_item("key"):
                    print("You use the key to open the gate and enter the castle.")
                    return self.castle
                else:
                    print("The gate is locked. You need a key to enter.")
            elif choice == "south":
                return self.tower
            else:
                print("I don't understand this choice.")

    def tower(self):
        while True:
            print("\nYou are at the base of a tall tower.")
            print("You can 'climb' the tower or go 'back' to the gate.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "back":
                return self.gate
            elif choice == "climb":
                print("You climb the tower and find a wizard at the top.")
                print("Wizard: I can 'teleport' you to any location or give you a 'blessing'.")
                choice = str.lower(input("What would you like to do? "))
                if choice == "teleport":
                    location = str.lower(input("Where would you like to go? ('castle', 'river', 'forest') "))
                    if location == "castle":
                        return self.castle
                    elif location == "river":
                        return self.river
                    elif location == "forest":
                        return self.forest
                    else:
                        print("The wizard doesn't know that place.")
                elif choice == "blessing":
                    if self.has_item("blessing"):
                        print("Wizard: You already have my blessing.")
                    else:
                        print("The wizard grants you a blessing, increasing your luck.")
                        self.add_to_inventory("blessing")
                    return self.tower
                else:
                    print("I don't understand this choice.")
            else:
                print("I don't understand this choice.")

    def river(self):
        while True:
            print("\nYou are at the river and see many fish in the water.")
            print("To the south is the gate.")
            print("There is a boat here that can take you 'across' the river.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "south":
                return self.gate
            elif choice == "fishing":
                print("You fished many fish and you are full now.")
                print("But the fish are poisoned and you are dead.")
                self.game_over = True
                return None
            elif choice == "across":
                if self.has_item("boat_pass"):
                    print("You use your pass and cross the river.")
                    return self.other_side
                else:
                    print("You need a pass to use the boat.")
            else:
                print("I don't understand this choice.")

    def other_side(self):
        while True:
            print("\nYou have crossed the river.")
            print("There is a dark cave ahead.")
            print("To the south is the river bank.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "south":
                return self.river
            elif choice == "cave":
                return self.cave
            else:
                print("I don't understand this choice.")

    def cave(self):
        while True:
            print("\nYou are in a dark cave.")
            print("You can go 'deeper' into the cave or go 'back' to the river bank.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "back":
                return self.other_side
            elif choice == "deeper":
                print("You venture deeper into the cave and find a mysterious artifact.")
                print("As you touch it, you are teleported back to the entrance of the castle.")
                return self.entrance
            else:
                print("I don't understand this choice.")

    def castle(self):
        while True:
            print("\nYou are inside the grand castle.")
            print("You can explore the 'hall', go to the 'library', or go 'back' outside.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "back":
                return self.gate
            elif choice == "hall":
                return self.hall
            elif choice == "library":
                return self.library
            else:
                print("I don't understand this choice.")

    def hall(self):
        while True:
            print("\nYou are in the castle's main hall.")
            print("There is a grand throne here.")
            print("You can 'sit' on the throne or go 'back' to the castle entrance.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "back":
                return self.castle
            elif choice == "sit":
                print("As you sit on the throne, guards rush in and arrest you for trespassing.")
                print("You are thrown into the dungeon.")
                return self.dungeon
            else:
                print("I don't understand this choice.")

    def dungeon(self):
        while True:
            print("\nYou are in the dark dungeon under the castle.")
            print("You can try to 'escape' or 'wait' for help.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "escape":
                if self.has_item("lockpick"):
                    print("You use the lockpick to unlock the cell door.")
                    print("You sneak out of the dungeon and find yourself back at the castle entrance.")
                    return self.castle
                else:
                    print("You don't have anything to pick the lock with.")
                    print("You remain trapped.")
                    return self.dungeon
            elif choice == "wait":
                print("No one comes to help. You eventually die in the dungeon.")
                self.game_over = True
                return None
            else:
                print("I don't understand this choice.")

    def library(self):
        while True:
            print("\nYou are in the castle's vast library.")
            print("Shelves filled with ancient books surround you.")
            print("You can 'search' the shelves or go 'back' to the castle entrance.")
            self.display_inventory()

            choice = str.lower(input("What would you like to do? "))

            if choice == "back":
                return self.castle
            elif choice == "search":
                if self.has_item("lockpick"):
                    print("You don't find anything else of interest.")
                else:
                    print("You find a hidden compartment containing a lockpick.")
                    self.add_to_inventory("lockpick")
            else:
                print("I don't understand this choice.")

    def start_game(self):
        self.current_location = self.entrance  # Start at the entrance
        while not self.game_over:
            self.current_location = self.current_location()  # Call the current location function
            if self.current_location is None:
                break  # End the game if no next location is returned

        if self.game_over:
            print("Game Over!")

# if this game is start with parameter -c, it will start the game with cheat mode
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "-c":
        game = Game()
        game.add_to_inventory("gold", 100)
        game.add_to_inventory("sword")
        game.add_to_inventory("key")
        game.add_to_inventory("lockpick")
        game.add_to_inventory("blessing")
        game.add_to_inventory("boat_pass")
        game.start_game()
    else:
        game = Game()
        game.start_game()
