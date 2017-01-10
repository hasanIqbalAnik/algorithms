import operator
import copy
import math


class State:
    def __init__(self, rowid, colid):
        self.row = rowid
        self.col = colid

    def __str__(self):
        return str(self.row) + " " + str(self.col)


def get_value_from_state(state):
    return state_values[state.row][state.col]


def get_reward_from_state(state):
    return reward_values[state.row][state.col]


def move_to_new_state(state, action):
    if action == 'left':  # state will only change columnwise
        if state.col == 0 or (state.col == 2 and state.row == 1):  # then we can't move left
            return copy.deepcopy(state)
        else:
            return State(state.row, (state.col - 1))
    if action == 'right':  # state will only change columnwise
        if state.col == 3 or (
                        state.col == 0 and state.row == 1):  # can't move right when on the right boundary or at the first column
            return copy.deepcopy(state)
        else:
            return State(state.row, (state.col + 1))
    if action == 'up':
        if state.row == 0 or (state.row == 2 and state.col == 1):
            return copy.deepcopy(state)
        else:
            return State(state.row - 1, state.col)
    if action == 'down':
        if state.row == 2 or (state.row == 0 and state.col == 1):
            return copy.deepcopy(state)
        else:
            return State(state.row + 1, state.col)


def moveWithProbabilites(state, action):
    if action == 'left' or action == 'right':
        thisstate = move_to_new_state(state, action)
        upstate = move_to_new_state(state, 'up')
        downstate = move_to_new_state(state, 'down')
        return {thisstate: .8, upstate: .1, downstate: .1}

    elif action == 'up' or action == 'down':
        thisstate = move_to_new_state(state, action)
        leftstate = move_to_new_state(state, 'left')
        rightstate = move_to_new_state(state, 'right')
        return {thisstate: .8, leftstate: .1, rightstate: .1}


state_values = [
    [0, 0, 0, 1],
    [0, -100, 0, -1],  # -100 means we can't go this way
    [0, 0, 0, 0]
]
reward_values = [  # in each state, the agent gets a reward of -.03
    [-.03, -.03, -.03, -.03],
    [-.03, -.03, -.03, -.03],
    [-.03, -.03, -.03, -.03]
]
gamma = 1

states = [
    State(0, 0),
    State(0, 1),
    State(0, 2),
    State(1, 0),
    State(1, 2),
    State(2, 0),
    State(2, 1),
    State(2, 2),
    State(2, 3),
]
actions = ['left', 'right', 'up', 'down']

prev = state_values[0][0]

if __name__ == "__main__":
    while True:
        for s in states:
            mx = -9999999
            for a in actions:
                dic = moveWithProbabilites(s, a)
                tempSum = get_reward_from_state(s)  # to be added to the values later

                tempSum += gamma * dic.items()[0][1] * get_value_from_state(dic.items()[0][0])  # .9 * .1 * v(s)
                tempSum += gamma * dic.items()[1][1] * get_value_from_state(dic.items()[1][0])
                tempSum += gamma * dic.items()[2][1] * get_value_from_state(dic.items()[2][0])

                if tempSum > mx:
                    mx = tempSum

            state_values[s.row][s.col] = mx

        if abs(state_values[0][0] - prev) < .00003:
            break
        prev = state_values[0][0]

print state_values
