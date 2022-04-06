import curses
import cases.CLI_GenralInfo
import cases.CLI_networkInfo
import cases.CLI_processInfo

def menu(stdscr):

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
    screen.keypad( 1 )
    screen.border( 0 )
    curses.curs_set( 0 )

    height, width = stdscr.getmaxyx()

    while True:

        title = "Welcome to Minitel 3.1"[:width-1]
        subtitle = "Choose the option"[:width-1]
        case1 = "[1] - General Information"[:width-1]
        case2 = "[2] - Network Information"[:width-1]
        case3 = "[3] - Process Information"[:width-1]
        statusbarstr = "Press the number for make your selection"

        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int(
            (width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_case1 = int((width // 2) - (len(case1) // 2) - len(case1) % 2)
        start_x_case2 = int((width // 2) - (len(case2) // 2) - len(case2) % 2)
        start_x_case3 = int((width // 2) - (len(case3) // 2) - len(case3) % 2)
        start_y = int((height // 3) - 2)

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " *
                      (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        stdscr.addstr(start_y, start_x_title, title)
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, start_x_case1, case1)
        stdscr.addstr(start_y + 4, start_x_case2, case2)
        stdscr.addstr(start_y + 5, start_x_case3, case3)

        stdscr.move(height-1, 0)

        stdscr.refresh()

        c = stdscr.getkey()

        if c == "1":
            curses.wrapper(cases.CLI_GenralInfo.mainPage)
        elif c == "2":
            curses.wrapper(cases.CLI_networkInfo.mainPage)
        elif c == "3":
            curses.wrapper(cases.CLI_processInfo.mainPage)


def main():
    curses.wrapper(menu)


if __name__ == "__main__":
    main()
