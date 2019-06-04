##### STATE MODULE #####
class State:
    def __init__(self):
        self.exited = False

    def exit_application(self):
        self.exited = True


STATE = State()