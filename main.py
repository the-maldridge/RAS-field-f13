#!/usr/bin/env python

import curses
import logging
import timing
import matchdb

import mainWin
import rankWin

class GUIMain():
    def __init__ ( self ):
        curses.wrapper ( self.main )

    def main ( self, screen ):
        self.screen = screen
        self.screen.timeout ( 10 )

        self.window = []
        self.window.append ( mainWin.MainWindow() )
        self.window.append ( rankWin.RankWindow() )
        self.focus = self

        while True:
            self.update()
            self.getInput()

    def getInput ( self ):
        inputKey = "ERR"
        try:
            inputKey = self.screen.getkey()
        except curses.error:
            pass
        if inputKey[ 0:5 ] == "KEY_F":
            switch_win = int ( inputKey[ 6:-1 ] ) - 1
            if switch_win < len ( self.window ):
                self.setFocus ( self.window[ switch_win ] )
        elif inputKey == "KEY_HOME":
            exit ( 0 )
        else:
            self.focus.parseInput ( inputKey )
    
    def update ( self ):
        if self.focus != self:
            self.focus.clear()
            self.focus.update()
        else:
            self.screen.refresh()

    def setFocus ( self, focus ):
        if self.focus is not self:
            self.focus.isfocused = False
        self.focus = focus
        self.focus.isfocused = True

    def parseInput ( self, value ):
        pass

    def __getattr__ ( self, attr ):
        getattr ( self.screen, attr )


class RASScoreboard(GUIMain):
    pass

if __name__ == "__main__":
    theapp = GUIMain()
