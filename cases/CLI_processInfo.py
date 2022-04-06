import CLI
import curses
import sys
from InfoScrap import process_info
from math import *

sys.path.append('..')

def mainPage(stdscr):
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    height, width = stdscr.getmaxyx()

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    screen.keypad(1)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    highlightText = curses.color_pair(1)
    normalText = curses.A_NORMAL
    screen.border(0)
    curses.curs_set(0)
    max_row = 10
    start_y = int((height // 4) - 2)
    box = curses.newwin(max_row + 2, 50, start_y + 3, (width // 2) - 25)
    box.box()

    AllProcessTab = process_info.getProcess()

    title = "All Packages installed:"[:width-1]
    subtitle = "Select with the arrows and press enter for information."[:width-1]
    statusbarstr = "Press the number to make your selection and 'q' to go back. del stop and f force Stop"

    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height-1, 0, statusbarstr)
    stdscr.addstr(height-1, len(statusbarstr), " " *
                  (width - len(statusbarstr) - 1))
    stdscr.attroff(curses.color_pair(3))

    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)



    stdscr.addstr(start_y, start_x_title, title)
    stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)

    pages = int(ceil(len(AllProcessTab) / max_row))
    position = 1
    page = 1

    for i in range(1, max_row + 1):
        if len(AllProcessTab) == 0:
            box.addstr(1, 1, "There aren't strings", highlightText)
        else:

            box.addstr(i, 2, f"{str( i )} - {AllProcessTab[i - 1][1]}", highlightText if i == position else normalText )

            if i == len(AllProcessTab):
                break

    screen.refresh()
    box.refresh()

    x = screen.getch()

    while True:

        if x == curses.KEY_DOWN:
            if page == 1:
                if position < i:
                    position = position + 1
                else:
                    if pages > 1:
                        page = page + 1
                        position = 1 + ( max_row * ( page - 1 ) )
            elif page == pages:
                if position < len(AllProcessTab):
                    position = position + 1
            else:
                if position < max_row + ( max_row * ( page - 1 ) ):
                    position = position + 1
                else:
                    page = page + 1
                    position = 1 + ( max_row * ( page - 1 ) )
        if x == curses.KEY_UP:
            if page == 1:
                if position > 1:
                    position = position - 1
            else:
                if position > ( 1 + ( max_row * ( page - 1 ) ) ):
                    position = position - 1
                else:
                    page = page - 1
                    position = max_row + ( max_row * ( page - 1 ) )
        if x == curses.KEY_LEFT:
            if page > 1:
                page = page - 1
                position = 1 + (max_row * (page - 1))

        if x == curses.KEY_RIGHT:
            if page < pages:
                page = page + 1
                position = (1 + (max_row * (page - 1)))
        if x == ord( "\n" ) and len(AllProcessTab) != 0:
            screen.erase()
            screen.border( 0 )
            screen.addstr( start_y + 6 + max_row, (width // 2) - 35, f" pid: {AllProcessTab[ position - 1 ][0]} - name: { AllProcessTab[ position - 1 ][1]} - status: { AllProcessTab[ position - 1 ][2]} - ppid: { AllProcessTab[ position - 1 ][3]} - cmdline: { AllProcessTab[ position - 1 ][4]}" )
        if x == 263: #del
            screen.addstr( start_y + 8 + max_row, (width // 2) - 35, process_info.isSoftStopProcess(AllProcessTab[ position - 1 ][0], True))
            
        if x == 102: #f
            screen.addstr( start_y + 8 + max_row, (width // 2) - 35, process_info.isSoftStopProcess(AllProcessTab[ position - 1 ][0], False))
            

        box.erase()
        screen.border(0)
        box.border(0)

        for i in range(1 + (max_row * (page - 1)), max_row + 1 + (max_row * (page - 1))):
            if len(AllProcessTab) == 0:
                box.addstr(1, 1, "There aren't strings",  highlightText)
            else:

                box.addstr(i - (max_row * (page - 1)), 2, f"{str( i )} - {AllProcessTab[i - 1][1]}", highlightText if i == position else normalText)
                if i == len(AllProcessTab):
                    break
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " *
                      (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        stdscr.addstr(start_y, start_x_title, title)
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)

        screen.refresh()
        box.refresh()
        x = screen.getch()

        c = stdscr.getkey()

        if c == "q":
            curses.wrapper(CLI.menu)