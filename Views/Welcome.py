import curses


from Views.View import View

class WelcomeView(View):
    def __init__(self, parentView):
        View.__init__(self, parentView)
        curses.noecho()
        curses.curs_set(0)
        curses.raw()
        self.height = 9
        self.width = 50
        self.ypos = (self.parentHeight - self.height) // 2
        self.xpos = (self.parentWidth - self.width) // 2

        self.win = curses.newwin(self.height, self.width, self.ypos, self.xpos)

        #self.win.attron(curses.color_pair(1))
        self.win.keypad(1)
        strHeader =   ' Welcome to Movie and Book Depot '
        strLogin =    '[l]      - Login'
        strRegester = '[r]      - Registration'
        strQuit =     '[x]      - Exit'
        self.win.box()
        self.win.addstr(1, (self.width-len(strHeader))//2,
                        strHeader, curses.A_REVERSE)
        self.win.addstr(3, 5, strLogin, curses.A_NORMAL)
        self.win.addstr(4, 5, strRegester, curses.A_NORMAL)
        self.win.addstr(5, 5, strQuit, curses.A_NORMAL)
        self.win.refresh()

    def choice(self):
        while True:
            choice = self.win.getch()
            
            if choice == ord('l'):
                break
            elif choice == ord('r'):
                break
            elif choice == ord('x'):
                break

        return choice
        
    def destroy(self):
        self.win.touchwin()
        self.win.refresh()
        del self.win