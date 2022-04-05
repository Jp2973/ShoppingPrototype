import curses, sys

from Views.Welcome import WelcomeView

def handleWelcome(stdscr):
    welcomeView = WelcomeView(stdscr)
    choice = welcomeView.choice()

    welcomeView.destroy()
    del welcomeView

    stdscr.touchwin()
    stdscr.refresh()

    return choice

def cursesTest():
    stdscr = curses.initscr()

    curses.start_color()
    curses.use_default_colors()

    while True:
        while True:
            choice = handleWelcome(stdscr)
            if choice == ord('l'):
                #loginView = LoginView(stdscr)
                while True:
                    break
            elif choice == ord('r'):
                pass
            elif choice == ord('x'):
                sys.exit(0)

if __name__ == "__main__":
    cursesTest()