#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Data store for player data, matches and more.

@author: Christian Wichmann
"""

import json
import os

class Match(object):
    """Contains a single match with all necessary information."""
    def __init__(self, player1, player2, points1, points2, serveplayer, time):
        self.player1 = player1
        self.player2 = player2
        self.points1 = points1
        self.points2 = points2
        self.serveplayer = serveplayer
        self.time = time

    def __str__(self):
        return ("%s\t%i:%i\t%s - %r %s" % (self.player1, self.points1, self.points2, self.player2, self.serveplayer, self.time))


class Player(object):
    # TODO: is player_id necessary?! Or just use name?
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id

    def __str__(self):
        return ("%i\t%s" % (self.player_id, self.name))


class Season(object):
    def __init__(self):
        self.players = []
        self.matches = []

    def __str__(self):
        ret = ""
        ret += "Players:\n"
        for p in self.players:
            ret += p.__str__() + "\n"
        ret += "\nMatches:\n"
        for m in self.matches:
            ret += m.__str__() + "\n"
        return ret

    def nextPlayerID(self):
        # TODO: also look for removed ids, so they don't grow endless
        player_ids = []
        for p in self.players:
            player_ids.append(p.player_id)
        ret = 0
        try:
            ret = max(player_ids) + 1
        except:
            pass
        return ret

    def addPlayer(self, player_name):
        """add new player to list"""
        new_player = Player(player_name, self.nextPlayerID())
        self.players.append(new_player)
        # sort list of players by id
        self.players = sorted(self.players, key=lambda x: x.player_id)
        
    def removePlayer(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)

    def addMatch(self, player1, player2, points1, points2, serveplayer, time):
        # check if player are in list of players
        #if self.player.
        
        # check if point are plausible
        if not (points1 == 11 or points2 == 11 or (points1 >= 10 and points2 > 10 and abs(points1 - points2) > 1)):
            return -1
        
        # save match in list
        match = Match(player1, player2, points1, points2, serveplayer, time)
        self.matches.append(match)
        print("Match added.")

    def dataToJSON(self):
        JSONdata = {"players": [], "matches": []}
        for player in self.players:
            JSONdata["players"].append(player.__dict__)
        for match in self.matches:
            JSONdata["matches"].append(match.__dict__)
        return JSONdata

    def JSONToData(self, data):
        self.players = []
        self.matches = []

        for player in data["players"]:
            self.players.append(Player(player["name"], player["player_id"]))
        for match in data["matches"]:
            self.matches.append(Match(match["player1"], match["player2"], match["points1"], match["points2"], match["serveplayer"], match["time"]))

    def saveData(self, filename):
        season_file = open(filename, "w")
        temp = self.dataToJSON()
        print(temp)
        json.dump(temp, season_file, indent=4)
        season_file.close()

    def loadData(self, filename):
        if os.path.exists(filename):
            season_file = open(filename, "r")
            data = json.load(season_file)
            self.JSONToData(data)
            season_file.close()
            # TODO check what last used player id is, to set id for next added player

if __name__ == '__main__':
    # Test for data classes
    p1 = Player("Martin", 0)
    p2 = Player("Markus", 1)
    print(p1)

    m = Match(p1, p2, 12, 14, True, "time")
    print(m)

    s = Season()
    s.addPlayer("Martin")
    s.addPlayer("Markus")
    s.addMatch("Martin", "Markus", 12, 11, True, "time")
    print(s)

