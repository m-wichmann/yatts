#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Data stores for player data, matches and more.

@author: Christian Wichmann
"""

import json
import os

class Match(object):
    def __init__(self, player1, player2, points1, points2, serveplayer, time):
        self.player1 = player1
        self.player2 = player2
        self.points1 = points1
        self.points2 = points2
        self.serveplayer = serveplayer
        self.time = time


class Player(object):
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
    def __str__(self):
        return str(self.name)


class Season(object):
    def __init__(self):
        self.player = []
        self.matches = []
        self.next_player_id = 1

    def addPlayer(self, player_name):
        """add new player to list"""
        new_player = Player(player_name, self.next_player_id)
        self.next_player_id += 1
        self.player.append(new_player)
        self.player.sort()
        return new_player


    def addMatch(self, player1, player2, points1, points2, serveplayer, time):
        # check if player are in list of players
        #if self.player.
        
        # check if point are plausible
        if not (points1 == 15 or points2 == 15 or (points1 > 14 and points2 > 14 and abs(points1 - points2) > 1)):
            return -1
        
        # save match in list
        match = Match(player1, player2, points1, points2, serveplayer, time)
        self.matches.append(match)

    def dataToJSON(self):
        JSONdata = {"player": [], "matches": []}
        for player in self.player:
            JSONdata["player"].append(player.__dict__)
        for match in self.matches:
            JSONdata["matches"].append(match.__dict__)
        return JSONdata


    def JSONToData(self, data):
        self.player = []
        self.matches = []

        for player in data["player"]:
            self.player.append(Player(player["name"], player["player_id"]))
        for match in data["matches"]:
            self.matches.append(Match(match["playerid1"], match["playerid2"], match["points1"], match["points2"], match["serveplayer"], match["time"]))

    def saveData(self, filename):
        if os.path.exists(filename):
            season_file = open(filename, "wb")
            temp = self.dataToJSON()
            json.dump(temp, season_file, indent=4)
            season_file.close()


    def loadData(self, filename):
        if os.path.exists(filename):
            season_file = open(filename, "rb")
            data = json.load(season_file)
            self.JSONToData(data)
            season_file.close()
