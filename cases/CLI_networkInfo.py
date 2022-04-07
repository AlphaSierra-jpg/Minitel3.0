from ast import In
from re import I
from InfoScrap import network_info
from math import *
import CLI
import curses
import sys

sys.path.append('..')

def mainPage(stdscr):
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)

    CYAN_Txt = curses.color_pair(5)
    titleColor = curses.color_pair(4)
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    screen.keypad(1)
    screen.border(0)
    curses.curs_set(0)

    height, width = stdscr.getmaxyx()

    y = 0

    while True:
        

        Interfaces = network_info.getInterfaces()
        TrafficInterface = network_info.getTrafficInterface()
        Routes = network_info.getRoutes()
        
        title = "Network Information:"[:width-1]
        statusbarstr = "Press the number to make your selection and 'q' to go back"
        IP = f"IP adress :"
        IPInt = f'  └─ Intern: {network_info.getIpExtAdress()}'
        IPExt = f"  └─ Extern: {network_info.getIpInternAdress()}"
        IpForward = f"Forward packages: "
        Interface = f"Network interfaces list:"
        

        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_middle = start_x_title - 10

        start_y = int((height // 4) - 2)

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " *
                      (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        stdscr.addstr(start_y, start_x_title, title, titleColor | curses.A_BOLD)

        stdscr.addstr(start_y + 3, start_x_middle, IP, CYAN_Txt | curses.A_BOLD)
        stdscr.addstr(start_y + 4, start_x_middle, IPInt)
        stdscr.addstr(start_y + 5, start_x_middle, IPExt)
        stdscr.addstr(start_y + 6, start_x_middle, IpForward, CYAN_Txt | curses.A_BOLD)
        stdscr.addstr( str(network_info.getIpForward()))
        stdscr.addstr(start_y + 7, start_x_middle, Interface, CYAN_Txt | curses.A_BOLD)

        for i in range( len(Interfaces)):
            y = (start_y + 7) + (i + 1)
            stdscr.addstr( y, start_x_middle, f"  └─ {Interfaces[i]}")

        stdscr.addstr( y + 1, start_x_middle, "Traffic Interface:", CYAN_Txt | curses.A_BOLD)
        y += 2
        for i in range(len(TrafficInterface)):
            y = y + i
            stdscr.addstr( y, start_x_middle, f"  └─ Name: {TrafficInterface[i][0]} | Received: {TrafficInterface[i][1]} | Sent: {TrafficInterface[i][2]}")

        stdscr.addstr( y + 1, start_x_middle, "Routes:", CYAN_Txt | curses.A_BOLD)

        y += 2
        for i in range( len(Routes)):
            stdscr.addstr( y + i, start_x_middle, f"  └─ {Routes[1]}")

        stdscr.move(height-1, 0)

        stdscr.refresh()

        c = stdscr.getkey()

        if c == "q":
            curses.wrapper(CLI.menu)
