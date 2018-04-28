import unittest
from kwsm import State, StateMachine


class GameStart(State):
    def validEnter(self, state):
        return isinstance(state, (GamePlay, GameEnd))


class GamePlay(State):
    def __init__(self):
        self.count = 0

    def validEnter(self, state):
        return isinstance(state, GameEnd)

    def update(self):
        self.count = 1


class GameEnd(State):
    def validEnter(self, state):
        return isinstance(state, GameStart)


class GameStateMachine(StateMachine):
    pass


gameStart = GameStart()
gamePlay = GamePlay()
gameEnd = GameEnd()


class TestStateAndStateMachine(unittest.TestCase):

    def test_create_state(self):
        game_start = GameStart()
        self.assertIsInstance(game_start, GameStart)

    def test_create_statemachine(self):
        sm = GameStateMachine()
        self.assertIsInstance(sm, GameStateMachine)

    def test_three_states(self):
        sm = GameStateMachine([gameStart, gamePlay, gameEnd])
        self.assertEqual(len(sm.states), 3)

    def test_game_state_start(self):
        sm = GameStateMachine([gameStart, gamePlay, gameEnd])
        sm.enter(gameStart)
        self.assertIsInstance(sm.current, GameStart)

    def test_game_state_start_automatically(self):
        sm = GameStateMachine([gameStart, gamePlay, gameEnd], start=True)
        self.assertIsInstance(sm.current, GameStart)

    def test_game_state_play(self):
        sm = GameStateMachine([gameStart, gamePlay, gameEnd])
        sm.enter(gameStart)
        sm.enter(gamePlay)
        self.assertIsInstance(sm.current, GamePlay)

    def test_game_state_play_update(self):
        sm = GameStateMachine([gameStart, gamePlay, gameEnd])
        sm.enter(gameStart)
        sm.enter(gamePlay)
        sm.update()
        self.assertEqual(sm.current.count, 1)

    def test_game_state_play_after_try_to_start(self):
        sm = GameStateMachine([gameStart, gamePlay, gameEnd])
        sm.enter(gameStart)
        sm.enter(gamePlay)
        sm.enter(gameStart)
        self.assertIsInstance(sm.current, GamePlay)

    def test_game_state_play_after_try_to_start_from_state(self):
        sm = GameStateMachine([gameStart, gamePlay, gameEnd])
        sm.enter(gameStart)
        sm.current.state_machine.enter(gamePlay)
        sm.enter(gameStart)
        self.assertIsInstance(sm.current, GamePlay)


if __name__ == '__main__':
    unittest.main()
