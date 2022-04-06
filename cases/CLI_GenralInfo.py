from InfoScrap import general_info
from math import *
import CLI
import curses
import sys

sys.path.append('..')


def listPakage(stdscr):
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    height, width = stdscr.getmaxyx()

    start_y = int((height // 3) - 2)

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
    box = curses.newwin(max_row + 2, 50, start_y + 3, (width // 2) - 25)
    box.box()

    AllPakageInfoTab = general_info.getAllPakage()

    title = "All Packages installed:"[:width-1]
    statusbarstr = "Press 'q' to go back"

    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height-1, 0, statusbarstr)
    stdscr.addstr(height-1, len(statusbarstr), " " *
                  (width - len(statusbarstr) - 1))
    stdscr.attroff(curses.color_pair(3))

    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)

    

    stdscr.addstr(start_y, start_x_title, title)

    pages = int(ceil(len(AllPakageInfoTab) / max_row))
    position = 1
    page = 1

    for i in range(1, max_row + 1):
        if len(AllPakageInfoTab) == 0:
            box.addstr(1, 1, "There aren't any strings", highlightText)
        else:

            box.addstr(i, 2, str(i) + " - " + AllPakageInfoTab[i - 1])

            if i == len(AllPakageInfoTab):
                break

    screen.refresh()
    box.refresh()

    x = screen.getch()

    while True:

        if x == curses.KEY_LEFT:
            if page > 1:
                page = page - 1

        if x == curses.KEY_RIGHT:
            if page < pages:
                page = page + 1

        box.erase()
        screen.border(0)
        box.border(0)

        for i in range(1 + (max_row * (page - 1)), max_row + 1 + (max_row * (page - 1))):
            if len(AllPakageInfoTab) == 0:
                box.addstr(1, 1, "There aren't any strings",  highlightText)
            else:

                box.addstr(i - (max_row * (page - 1)), 2, str(i) +
                           " - " + AllPakageInfoTab[i - 1], normalText)

                if i == len(AllPakageInfoTab):
                    break
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " *
                      (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        screen.refresh()
        box.refresh()
        x = screen.getch()

        c = stdscr.getkey()

        if c == "q":
            curses.wrapper(mainPage)


def mainPage(stdscr):
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    screen.keypad(1)
    screen.border(0)
    curses.curs_set(0)

    height, width = stdscr.getmaxyx()

    while True:
        DiskInfoTab = general_info.getDiskInfo()
        RAMTab = general_info.getRAMInfo()

        title = "General Information"[:width-1]
        statusbarstr = "Press the number to make your selection and 'q' to go back"
        OSversion = f"Operation system version: {general_info.getOSversion()}"
        OS = f'Operating system: {general_info.getOS()}'
        uptime = f"Uptime: {general_info.uptime()}"
        kernelInfo = f"Kernel version: {general_info.getKernelVersion()}"
        CPU = f"CPU: {general_info.getCPUInfo()}"
        RAM = f"Memory: total: {RAMTab[0]}   used: {RAMTab[1]}   free: {RAMTab[2]}"
        DiskInfo = f"Total capacity: {DiskInfoTab[0]}Go | free: {DiskInfoTab[1]}Go | used: {DiskInfoTab[2]}Go"
        openFileLimit = f"Open files limit: {general_info.getOpenFileLimit()}"
        openProsLimit = f"Open processes limit: {general_info.getOpenProsLimit()}"

        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_middle = int(
            (width // 2) - (len(OSversion) // 2) - len(OSversion) % 2)

        start_y = int((height // 3) - 2)

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " *
                      (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        stdscr.addstr(start_y, start_x_title, title)

        stdscr.addstr(start_y + 3, start_x_middle, OSversion)
        stdscr.addstr(start_y + 4, start_x_middle, OS)
        stdscr.addstr(start_y + 5, start_x_middle, uptime)
        stdscr.addstr(start_y + 6, start_x_middle, kernelInfo)
        stdscr.addstr(start_y + 7, start_x_middle, CPU)
        stdscr.addstr(start_y + 8, start_x_middle, RAM)
        stdscr.addstr(start_y + 9, start_x_middle, DiskInfo)
        stdscr.addstr(start_y + 10, start_x_middle, openFileLimit)
        stdscr.addstr(start_y + 11, start_x_middle, openProsLimit)

        stdscr.addstr(start_y + 13, start_x_middle,
                      "Installed packages list:")
        stdscr.addstr(start_y + 14, start_x_middle,
                      "   press '1' to see the list")

        stdscr.move(height-1, 0)

        stdscr.refresh()

        c = stdscr.getkey()

        if c == "q":
            curses.wrapper(CLI.menu)
        if c == "1":
            curses.wrapper(listPakage)
