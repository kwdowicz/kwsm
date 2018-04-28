from kwsm import State, StateMachine
import sys


class GameStart(State):
    def validEnter(self, state):
        return isinstance(state, (GamePlay, GameEnd))

    def enter(self):
        print(self.__class__.__name__ + ' ' + sys._getframe().f_code.co_name)

    def exit(self):
        print(self.__class__.__name__ + ' ' + sys._getframe().f_code.co_name)


class GamePlay(State):
    def __init__(self):
        self.count = 0

    def validEnter(self, state):
        return isinstance(state, GameEnd)

    def update(self):
        print(self.__class__.__name__ + ' ' + sys._getframe().f_code.co_name)
        self.count += 1

    def enter(self):
        print(self.__class__.__name__ + ' ' + sys._getframe().f_code.co_name)

    def exit(self):
        print(self.__class__.__name__ + ' ' + sys._getframe().f_code.co_name)


class GameEnd(State):
    def validEnter(self, state):
        return isinstance(state, GameStart)

    def enter(self):
        print(self.__class__.__name__ + ' ' + sys._getframe().f_code.co_name)

    def exit(self):
        print(self.__class__.__name__ + ' ' + sys._getframe().f_code.co_name)


class GameStateMachine(StateMachine):
    pass


gameStart = GameStart()
gamePlay = GamePlay()
gameEnd = GameEnd()

sm = GameStateMachine([gameStart, gamePlay, gameEnd], start=True)
sm.current.state_machine.enter(gamePlay)
print('before running update: ' + str(sm.current.count))
sm.update()
print('after running update: ' + str(sm.current.count))
sm.current.state_machine.enter(gameEnd)
