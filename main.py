#!/usr/bin/env python

import curses
import logging
import timing
import matchdb

class GUIMain():
    def __init__ ( self ):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad ( 1 )

    def __del__ ( self ):
        self.stdscr.keypad ( 0 )
        curses.nocbreak()
        curses.echo()
        curses.endwin()

class RASScoreboard(GUIMain):
    pass

if __name__ == "__main__":
    theapp = GUIMain()
    theapp.stdscr.getch()
    del theapp
