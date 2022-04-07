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
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)

    titleColor = curses.color_pair(5)
    RED_AN_BLACK = curses.color_pair(4)
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    screen.keypad( 1 )
    screen.border( 0 )
    curses.curs_set( 0 )

    height, width = stdscr.getmaxyx()

    while True:
        
        title1 = " __    __     _                            _                    _       _ _       _   _____  _ "[:width-1]
        title2 = "/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___    _ __ ___ (_)_ __ (_) |_ ___| | |___ / / |"[:width-1]
        title3 = "\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | '_ ` _ \| | '_ \| | __/ _ \ |   |_ \ | |"[:width-1]
        title4 = " \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | | | | | | | | | | ||  __/ |  ___) || |"[:width-1]
        title5 = "  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_| |_| |_|_|_| |_|_|\__\___|_| |____(_)_|"[:width-1]
    
        subtitle = "Choose the option"[:width-1]
        case1 = "[1]"
        textCase1 = " - General Information"[:width-1]
        case2 = "[2]"
        textCase2 = " - Network Information"[:width-1]
        case3 = "[3]"
        textCase3 = " - Process Information"[:width-1]
        statusbarstr = "Press the number for make your selection and q to quit"

        start_x_title1 = int((width // 2) - (len(title1) // 2) - len(title1) % 2)
        start_x_title2 = int((width // 2) - (len(title2) // 2) - len(title2) % 2)
        start_x_title3 = int((width // 2) - (len(title3) // 2) - len(title3) % 2)
        start_x_title4 = int((width // 2) - (len(title4) // 2) - len(title4) % 2)
        start_x_title5 = int((width // 2) - (len(title5) // 2) - len(title5) % 2)
        start_x_subtitle = int(
            (width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_case1 = int((width // 2) - (len(case1 + textCase1) // 2) - len(case1 + textCase1) % 2)
        start_x_case2 = int((width // 2) - (len(case2 + textCase2) // 2) - len(case2 + textCase2) % 2)
        start_x_case3 = int((width // 2) - (len(case3 + textCase3) // 2) - len(case3 + textCase3) % 2)
        start_y = int((height // 3) - 2)

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " *
                      (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        stdscr.addstr(start_y, start_x_title1, title1, titleColor | curses.A_BOLD)
        stdscr.addstr(start_y + 1, start_x_title2, title2, titleColor | curses.A_BOLD)
        stdscr.addstr(start_y + 2, start_x_title3, title3, titleColor | curses.A_BOLD)
        stdscr.addstr(start_y + 3, start_x_title4, title4, titleColor | curses.A_BOLD)
        stdscr.addstr(start_y + 4, start_x_title5, title5, titleColor | curses.A_BOLD)
        stdscr.addstr(start_y + 6, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 8, start_x_case1, case1, RED_AN_BLACK)
        stdscr.addstr(textCase1)
        stdscr.addstr(start_y + 9, start_x_case2, case2, RED_AN_BLACK)
        stdscr.addstr(textCase2)
        stdscr.addstr(start_y + 10, start_x_case3, case3, RED_AN_BLACK)
        stdscr.addstr(textCase3)

        stdscr.move(height-1, 0)

        stdscr.refresh()

        c = stdscr.getkey()

        if c == "1":
            curses.wrapper(cases.CLI_GenralInfo.mainPage)
        elif c == "2":
            curses.wrapper(cases.CLI_networkInfo.mainPage)
        elif c == "3":
            curses.wrapper(cases.CLI_processInfo.mainPage)
        elif c == "q":
            exit()


def main():
    curses.wrapper(menu)


if __name__ == "__main__":
    main()
