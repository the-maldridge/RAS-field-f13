#!/usr/bin/env python

import curses
import logging
import timing
import matchdb

class GUIMain():
    def __init__ ( self ):
        curses.wrapper ( self.main )

    def main ( self, screen ):
        self.screen = screen
        self.screen.getch()
        self.screen.timeout ( 10 )
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
        if inputKey[ 0 ] == "F":
            self.setFocus ( window[ int ( inputKey[ 1: ] ) ] )
        elif inputKey == "KEY_HOME":
            exit ( 0 )
        else:
            self.focus.parseInput ( inputKey )
    
    def update ( self ):
        if self.focus != self:
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
