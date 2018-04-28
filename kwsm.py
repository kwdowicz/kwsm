class State:
    def __init__(self):
        self.state_machine = None

    def enter(self):
        pass

    def update(self):
        pass

    def exit(self):
        pass

    def validEnter(self, state):
        return False


class StateMachine:
    def __init__(self, states=[], start=False):
        self.states = states
        self.current = None
        for state in self.states:
            state.state_machine = self
        if start and len(states) > 0:
            self.enter(states[0])

    def enter(self, state):
        if self.current:
            self.current.exit()
            if self.current.validEnter(state):
                self.current = state
                self.current.enter()
        else:
            self.current = state
            self.current.enter()
    
    def update(self):
        if self.current:
            self.current.update()
