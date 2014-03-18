#-------------------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kpm72
# im not actyually lame
# Created:     04/03/2014
# Copyright:   (c) kpm72 2014
# Licence:     <your licence>
#---------------------------------------------------------------------------------------------------
import random
import cmd

class Game:
    def __init__(self, time = 2100, current_level = 1, current_player = None, players = [], tile_cards = [], dev_cards = [], current_tiles = []): #current turn stores the players name whose turn it is
        self.time = time
        self.current_level = current_level
        self.current_player = current_player
        self.players = players
        self.tile_cards = tile_cards
        self.dev_cards = dev_cards
        self.current_tiles = current_tiles

    def get_current_tiles(self):
        return self.current_tiles

    def get_current_player(self):
        return self.current_player

    def add_current_tile(self, tile):
        self.current_tiles.append(tile)

    def get_players(self):
        return self.players

    def add_player(self, player):
        self.players.append(player)

    def add_card(self, card):
        if type(card) is Tile_Card:
            self.tile_cards.append(card)
        elif type(card) is Dev_Card:
            self.dev_cards.append(card)

    def get_tile_card_by_coords(self, x, y):
        for i in self.current_tiles:
            if (i.get_x() == x and i.get_y() == y):
                return i
        return False

    def discard_card(self, card):
        if type(card) is Tile_Card:
            self.tile_cards.remove(card)
        elif type(card) is Dev_Card:
            self.dev_cards.remove(card)

    def draw_tile_card(self):
        if len(self.tile_cards) > 0:
            card = self.tile_cards[random.randrange(0, len(self.tile_cards))]
            card.user_rotate()
            self.current_tiles.append(card)
            self.discard_card(card)
            return card
        else:
            return False

    def draw_dev_card(self):
        if len(self.dev_cards) > 0:
            card = self.dev_cards[random.randrange(0, len(self.cards))]
            self.discard_card(card)
            return card
        else:
            return False

    def get_tile_cards(self):
        return self.tile_cards

    def get_dev_cards(self):
        return self.dev_cards

    def change_turn(self):
        if (self.current_player != None):
            index = self.players.index(self.current_player)
            if (len(self.players) - 1 > index):#if the last player doesn't have his turn currently
                self.current_player = self.players[index + 1]#go to the next player
            else:#else if the last player does have his turn
                self.current_player = self.players[0]#go back to the first player
        else:
            self.current_player = self.players[0]
        return self.current_player

    def get_all_players_scores(self):
        result = ""
        players = self.get_players()
        for i in players:
            result += i.get_name() + " got " + str(i.get_score()) + " points!\n"
        return result

    def get_effect_for_time(self, dev_card):
        if  2100 <= self.time() < 2200:
            action = dev_card.get_nine_effect()
        elif self.time() < 2300:
            action = dev_card.get_ten_effect()
        else:
            action = dev_card.get_eleven_effect()
        return action

    def do_dev_card_action(self, dev_card):
        effect = get_effect_for_time()
        if effect == 'Z':
            print("ZOMBIES! AAHHHHHH")
        elif effect == 'D':
            self.current_player().take_dmg(1)
            print("You take one dmg, hp now " + str(self.current_player.get_health()))
        elif effect == 'I':
            print("Ooh a juicy item!")
        else:
            pass

    def get_all_current_tiles(self):
        for i in self.current_tiles:
            print(i.get_desc() + "\n")

    def are_tile_cards_left(self):
        if len(self.tile_cards) > 0:
            return True
        else:
            return False

the_game = Game()
class Player:
    def __init__(self, x = 0, y = 0, score = 0, name = "Player 1", attack = 1, health = 6, game = None, tile_card = None, items = [], has_totem = False):
        self.score = score
        self.x = x
        self.y = y
        self.name = name
        self.game = game
        self.tile_card = tile_card
        self.items = items
        self.attack = attack
        self.health = health
        self.has_totem = has_totem
        game.add_player(self)

    def add_score(self, score):
        self.score += int(score)

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def set_tile_card(self, card):
        self.tile_card = card

    def get_tile_card(self):
        return self.tile_card

    def get_health(self):
        return self.health

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def pick_up_totem(self):
        self.has_totem = True

    def remove_first_item(self):
        self.items.remove(items[0])

    def add_item(self, item):
        if self.items <= 2:
            self.items.append(item)
        else:
            self.remove_first_item()
            self.items.append(item)

    def take_dmg(self, damage):
        self.health -= damage

    def get_player_details(self):
        return self.name + "\nCurrent Position: (" + str(self.x) + ", " + str(self.y)+ ")"

class Card:
     def __init__(self, name, effect, game):
        self.name = name
        self.effect = effect
        the_game.add_card(self)

     def get_desc(self):
        return self.name + "\nEffect: " + self.effect

class Tile_Card(Card):
    def __init__(self, x = 0, y = 0, name = "", effect = "", doors = [], game = None):
        Card.__init__(self, name, effect, game)
        self.x = x
        self.y = y
        self.doors = doors

    def get_name(self):
        return self.name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_door(self, direction):
        door_ref = {"n": 0, "e": 1, "s": 2, "w": 3}.get(direction)
        return self.doors[door_ref]

    def get_doors_string(self):
        return "North = " + str(self.doors[0]) + ", East = " + str(self.doors[1]) + ", South = " + str(self.doors[2]) + ", and West = " + str(self.doors[3])


    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, num_quarter_turns = 1):
        for i in range(0, int(num_quarter_turns)):
            n = self.doors[0] + 0
            e = self.doors[1] + 0
            s = self.doors[2] + 0
            w = self.doors[3] + 0
            self.doors[0] = w
            self.doors[1] = n
            self.doors[2] = e
            self.doors[3] = s

    def user_rotate(self):
        try:
            num = input("How many times would you like to rotate the " + self.name + " tile? " + "\nCurrent Doors: " + self.get_doors_string())
            self.rotate(num)
        except ValueError:
            print("Please enter a number")
            self.user_rotate()

    def get_desc(self):
        return self.name + " at (" + str(self.x) + ", " + str(self.y) + ")"

class Dev_Card(Card):
    def __init__(self, name, effect, item, nine_effect, ten_effect, eleven_effect, num_zombies, game):
        #key for effects is Z = Zombies, D = take 1 dmg, I = Get Item
        Card.__init__(self, name, effect, game)
        self.item = item

    def get_desc(self):
        return self.name + "\nItem: " + self.item.get_desc()

    def get_nine_effect(self):
        return self.nine_effect

    def get_ten_effect(self):
        return self.ten_effect

    def get_eleven_effect(self):
        return self.eleven_effect

    def add_item(self, item):
        self.item = item

class Item:
    def __init__(self, name, attack, dev_card):
        self.name = name
        self.attack = attack
        dev_card.add_item(self)

    def get_desc(self):
        return self.name + " with an attack of " + str(self.attack)

def add_player(the_game):
        the_name = input("What username would you like to use?")
        new_player = Player(name = the_name, game = the_game)
        print("Welcome to the Game " + new_player.get_player_details())
        return new_player

def rotate_card_loop(oppo_direction, the_card):
    while True:
        if the_card.get_door(oppo_direction):
            return True
            break
        else:
            the_card.user_rotate()

def move_to_card(player, direction, x, y):
    oppo_direction = {"n" : "s", "e" : "w", "s" : "n", "w" : "e"}.get(direction, 0)
    if the_game.get_tile_card_by_coords(x, y):
        the_card = the_game.get_tile_card_by_coords(x, y)
        player.set_tile_card(the_card)
        player.set_coords(x, y)
    else:
        the_card = the_game.draw_tile_card()
        the_card.set_coords(x, y)
        if (rotate_card_loop(oppo_direction, the_card)):
            player.set_tile_card(the_card)
            player.set_coords(x, y)

def play_turn(direction):
    direction = direction.lower()
    current_player = the_game.get_current_player()
    x = current_player.get_x() + {"e": 1, "w": -1}.setdefault(direction, 0)
    y = current_player.get_y() + {"n": 1, "s": -1}.setdefault(direction, 0)
    if the_game.are_tile_cards_left() or the_game.get_tile_card_by_coords(x, y):
        if direction in "nesw" and current_player.get_tile_card().get_door(direction):
            move_to_card(current_player, direction, x, y)
        else:
            print("You can't move that way!")
    else:
        print("No tile cards left! Please move to an existing square")
    print(current_player.get_tile_card().get_desc())
    print(current_player.get_tile_card().get_doors_string())

def add_tile_cards():
    Tile_Card(0, 0, "Kitchen", "Does Nothing", [False, False, True, False], the_game)
    Tile_Card(0, 0, "Dining Room", "Does Nothing", [True, True, False, True], the_game)
    Tile_Card(0, 0, "Bedroom", "Does Nothing", [True, True, False, True], the_game)
    Tile_Card(0, 0, "Patio", "Does Nothing", [True, True, True, True], the_game)
    Tile_Card(0, 0, "Basement", "Does Nothing", [True, True, True, True], the_game)
    Tile_Card(0, 0, "Bathroom", "Does Nothing", [True, True, True, True], the_game)

def add_dev_cards():
    for i in range(0, 4):
        the_card = Dev_Card("Dev Card " + str(i), "Does Nothing", "Chainsaw", "Z", "D", "I", 4, the_game)
        Item("Chainsaw", 3, the_card)

def start_game():
    the_player = add_player(the_game)
    add_tile_cards()
    add_dev_cards()
    card = Tile_Card(0, 0, "Foyer", "Does Nothing", [True, False, False, False], the_game)
    the_player.set_tile_card(card)
    the_game.add_current_tile(card)
    the_game.discard_card(card)
    for i in the_game.get_tile_cards():
        print(i.get_desc())
    for i in the_game.get_dev_cards():
        print(i.get_desc())
    the_game.change_turn()

class Program(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>> "

    def do_start(self, arg1):
        start_game()

    def do_go(self, direction):
        """
Choose a direction to go from the current room.
Syntax: go [direction] where direction is either \'n\' (for north), \'e\' (for east), \'s\' (for south), \'w\' (for west)
        """
        try:
            play_turn(direction)
        except TypeError as err:
            print("Please enter a direction")

    def do_quit(self, arg):
        print("Goodbye")
        return True

def main():
    try:
        the_program = Program()
        the_program.cmdloop()
    except KeyboardInterrupt:
        print("Goodbye")
        exit

if __name__ == '__main__':
    main()
