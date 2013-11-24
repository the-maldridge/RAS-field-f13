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
        self.focus = self

    def getInput ( self ):
        inputKey = self.win.getkey()
        self.focus.parseInput ( inputKey )
    
    def update ( self ):
        self.focus.update()

    def parseInput ( self ):
        pass

    def __getattr__ ( self, attr ):
        getattr ( self.screen, attr )


class RASScoreboard(GUIMain):
    pass

if __name__ == "__main__":
    theapp = GUIMain()
