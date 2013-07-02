#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Graphical user interface for YATTS.

@author: Christian Wichmann
"""

# todo
# - 
# - 
# - 

from PyQt4 import QtGui, uic, QtCore
import sys
import yatts.data


class YattsStarter(QtGui.QMainWindow):  
    """Main window for JATTS"""
    
    def __init__(self):
        """initialize starter dialog for JATTS"""
        QtGui.QMainWindow.__init__(self)
        self.contentWidget = QtGui.QWidget()
        self.titleLabel = QtGui.QLabel(APP_NAME)
        
        self.manage_player_button = QtGui.QPushButton("Player Management")
        self.manage_player_button.clicked.connect(self.handle_manage)
        
        self.edit_games_button = QtGui.QPushButton("Edit Games")
        self.edit_games_button.clicked.connect(self.handle_edit)
        
        self.view_statistics_button = QtGui.QPushButton("View Statistics")
        self.view_statistics_button.clicked.connect(self.handle_view)

        starter_layout = QtGui.QGridLayout()
        starter_layout.addWidget(self.titleLabel, 0, 0)
        starter_layout.addWidget(self.manage_player_button, 1, 0)
        starter_layout.addWidget(self.edit_games_button, 2, 0)
        starter_layout.addWidget(self.view_statistics_button, 3, 0)
          
        self.contentWidget.setLayout(starter_layout)
        self.setWindowTitle(APP_NAME)
        self.setWidgetFonts()
        
        self.setCentralWidget(self.contentWidget)
        
    def setWidgetFonts(self):
        """sets font for all widgets in main window"""
        font = QtGui.QFont("Ubuntu", 20)
        self.titleLabel.setFont(font)
        font.setPointSize(14)
        self.manage_player_button.setFont(font)
        self.edit_games_button.setFont(font)
        self.view_statistics_button.setFont(font)
        
    def handle_manage(self):
        """show dialog to add and remove player"""
        PLAYER_DIALOG.show()
        
    def handle_view(self):
        """show dialog with statistical information"""
        STATISTICS_DIALOG.show()
        
    def handle_edit(self):
        """show dialog to edit game data"""
        MATCHES_DIALOG.show()


def buildPlayerManagementDialog(dialog):
    dialog.close_button.clicked.connect(dialog.close)
    for player in MANAGER.players:
        print(player.name)
        #player_item = QtGui.QListWidgetItem(player.name)
        #dialog.player_list.add_item(player_item)

def buildEditMatchesDialog(dialog):
    dialog.add_new_match_button.clicked.connect(handle_add_match)
    dialog.player2_combo.clear()
    #items = [QtCore.QString()]
    for player in MANAGER.players:
        dialog.player2_combo.addItem("ddd")
    #dialog.player2_combo.addItems(items)

def handle_add_match():
    pass

def buildViewStatisticsDialog(dialog):
    #view_match_table
    pass

if __name__ == "__main__":
    APP_NAME = "Yet Another Table Tennis Statistic"
    DATA_FILE = "tabletennis2013.dat"

    # load player names, game data from json file    
    MANAGER = yatts.data.Season()
    #MANAGER.loadData(DATA_FILE)
    MANAGER.addPlayer(yatts.data.Player("Christian", 1))
    MANAGER.addPlayer(yatts.data.Player("Martin", 2))
    
    APP = QtGui.QApplication(sys.argv)
      
    ### load ui files for dialogs
    PLAYER_DIALOG = uic.loadUi("player_management.ui")
    MATCHES_DIALOG = uic.loadUi("show_matches.ui")
    STATISTICS_DIALOG = uic.loadUi("view_statistics.ui")
    buildPlayerManagementDialog(PLAYER_DIALOG)
    buildEditMatchesDialog(MATCHES_DIALOG)
    buildViewStatisticsDialog(STATISTICS_DIALOG)
    
    STARTER_WIDGET = YattsStarter()  
    STARTER_WIDGET.show()
    
    # save all data back to file
    MANAGER.saveData(DATA_FILE)
      
    sys.exit(APP.exec_())

