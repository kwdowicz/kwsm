## Installation

```
...
```

## Example

```python
from kwsm import State, StateMachine
import sys

# create 3 states:
class GameStart(State):
    # here you return True if you can enter to other state
    def validEnter(self, state):
        return isinstance(state, (GamePlay, GameEnd))

    # code executed when you enter the state
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

# create state machine
class GameStateMachine(StateMachine):
    pass

# initialize your states
gameStart = GameStart()
gamePlay = GamePlay()
gameEnd = GameEnd()

# run some fun
sm = GameStateMachine([gameStart, gamePlay, gameEnd], start=True)
sm.current.state_machine.enter(gamePlay)
print('before running update: ' + str(sm.current.count))
sm.update()
print('after running update: ' + str(sm.current.count))
sm.current.state_machine.enter(gameEnd)
```

```bash
# thats your output
$ python kwsm.example.py
GameStart enter
GameStart exit
GamePlay enter
before running update: 0
GamePlay update
after running update: 1
GamePlay exit
GameEnd enter
```
