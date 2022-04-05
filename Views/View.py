class View:
    def __init__(self, parent):
        self.parentHeight, self.parentWidth = parent.getmaxyx()
        self.parentYpos, self.parentXpos = parent.getbegyx()