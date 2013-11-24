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

    def __getattr__ ( self, attr ):
        getattr ( self.screen, attr )


class RASScoreboard(GUIMain):
    pass

if __name__ == "__main__":
    theapp = GUIMain()
