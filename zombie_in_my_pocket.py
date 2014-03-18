#-------------------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#bklbkkbkbkjbjk.
# Author:      kpm72
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
            card.user_rotate
