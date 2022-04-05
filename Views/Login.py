import curses

from .View import View

class LoginView(View):
    def __init__(self, stdscr):
        View.__init__(self, stdscr)
        self.STARTPOS = 14
        self.ENDPOS   = 15
        self.maxInput = self.STARTPOS + self.ENDPOS

        curses.curs_set(1)
        curses.noraw()
        self.height = 10
        self.width = 50
        self.ypos = (self.parentHeight - self.height) // 2
        self.xpos = (self.parentWidth - self.width) // 2

        self.win = curses.newwin(self.height, self.width, self.ypos, self.xpos)

        self.win.keypad(1)
        strHeader =   ' Welcome to Login Form '
        strUserName = 'User name:'
        strPassword = 'Password:'
        self.win.box()
        self.win.addstr(1, (self.width - len(strHeader)) // 2,
                        strHeader, curses.A_REVERSE)
        self.win.addstr(3, 2,
                        strUserName, curses.A_NORMAL)
        self.win.addstr(5, 2,
                        strPassword, curses.A_NORMAL)

        # Buttons
        self.win.addstr(8, 2, ' [CTRL-B] - Back ', curses.A_REVERSE)
        self.win.addstr(8, 30, ' [CTRL-L] - Login ', curses.A_REVERSE)
        self.win.refresh()
        stdscr.refresh()
        
    def getch(self, flag, end):
        container = ''
        y, x = self.win.getyx()
        movingX = x
        rightX = self.STARTPOS

        while True:
            if end:
                curses.raw()
                curses.noecho()
                self.win.keypad(1)
                curses.curs_set(0)

                ch = self.win.getch()
                kname = curses.keyname(ch)
                if kname == '^L':
                    return kname

            elif not end:
                curses.raw()
                curses.noecho()
                self.win.keypad(1)

                ch = self.win.getch()
                kname = curses.keyname(ch)

                if ch == 2: # If user hits CTRL-B
                    container = ''
                    return 2

                elif kname == '^L':
                    return kname

                elif ch == curses.KEY_BACKSPACE: # Backspace
                    if rightX > self.STARTPOS: # If cursor is bigger then start position.
                        container = container[:-1] # Delete the last character.
                        y, x = self.win.getyx()
                        x -= 1                    # --+
                        rightX -= 1               #   |--> Keep track of pointers
                        movingX -= 1              # --+
                        self.win.addch(y, x, ' ') # Remove last char fom screen.
                        self.win.move(y, x)       # Move back the cursor
                        self.win.refresh()
                    else:
                        self.warning()

                elif ch == 9: # TAB ('^I') for Gnome-terminal
                    return ch

                elif ch == curses.KEY_BTAB: # SHIFT+TAB for Gnome-terminal
                    return ch

                elif ch == curses.KEY_HOME:
                    self.win.move(y, self.STARTPOS)
                    movingX = self.STARTPOS

                elif ch == curses.KEY_END:
                    self.win.move(y, self.STARTPOS + len(container))
                    movingX = self.STARTPOS + len(container)
                    x = self.STARTPOS + len(container)

                elif ch == 10:          # If user hits the enter,
                    if container != '': # if we have something in container and
                        return container
                    else:
                        return 10       # or we don't.

                elif ch == curses.KEY_LEFT:
                    y, x = self.win.getyx()
                    movingX = x # probably movingX has to be a static variable
                    if movingX > self.STARTPOS:
                        movingX -= 1 # Tracking the X position
                        self.win.move(y, movingX)
                    else:
                        self.win.move(y, self.STARTPOS)
                        self.warning()

                elif ch == curses.KEY_RIGHT:
                    y, x = self.win.getyx()
                    movingX = x
                    if movingX < self.maxInput and movingX < rightX:
                        movingX += 1 # Tracking the X position
                        self.win.move(y, movingX)
                    else:
                        if movingX == self.maxInput:
                            self.win.move(y, self.maxInput)
                            curses.beep()
                            curses.flash()
                        elif movingX == rightX:
                            self.win.move(y, rightX)
                            self.warning()

                elif ch in range(65, 91) or \
                     ch in range(97, 123) or \
                     ch in range(49, 58) or \
                     ch == ord('_'):

                    curses.noraw()

                    if not flag and movingX == rightX: # If we arn't in the password
                        if rightX < self.maxInput: # max right position
                            self.win.addch(ch) # field and no arrow key used yet.
                            container += chr(ch)
                            movingX += 1
                            rightX += 1
                        else:
                            self.warning()

                    # Creating illusion of input on screen...
                    elif not flag and movingX < rightX: # If we moved with arrow keys
                        if rightX < self.maxInput: # max right position
                            containerLeft = container[:movingX-self.STARTPOS]
                            containerRight = container[movingX-self.STARTPOS:]
                            container = containerLeft
                            container += chr(ch)
                            container += containerRight
                            movingX += 1
                            rightX += 1
                            self.win.addstr(y, self.STARTPOS, container)
                            self.win.move(y, movingX)
                            self.win.refresh()
                        else:
                            self.warning()

                    elif flag: # If we are in the password field
                        if rightX < self.maxInput: # max right position
                            curses.echo()
                            container += chr(ch)
                            self.win.addch(curses.ACS_DIAMOND)
                            movingX += 1
                            rightX += 1
                        else:
                            self.warning()


    def getstr(self):
        return self.win.getstr()

    def getmaxyx(self):
        return self.win.getmaxyx()

    def getbegyx(self):
        return self.win.getbegyx()

    def move(self, y, x):
        self.win.move(y, x)

    def refresh(self):
        self.win.refresh()

    def touchwin(self):
        self.win.touchwin()

    def clrtoeol(self):
        self.win.clrtoeol()

    def box(self):
        self.win.box()

    def warning(self):
        curses.beep()
        curses.flash()

    def destroy(self):
        self.win.touchwin()
        self.win.refresh()
        del self.win