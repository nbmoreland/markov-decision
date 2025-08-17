# Nicholas Moreland
import numpy as np
import csv

# Dictionary of movements
movements = {
    "Up": "^",
    "Down": "v",
    "Left": "<",
    "Right": ">",
}

# Check if state is valid
def isValid(data, s):
    return 0 <= s[0] < len(data) and 0 <= s[1] < len(data[0]) and data[s[0]][s[1]] != "X"

# Return reward for state
def R(data, state, non_terminal_reward):
    value = data[state[0]][state[1]]
    return non_terminal_reward if value == "." else 0 if value == "X" else float(value)

# Find the max value of a state
def findMax(data, state, U, N, move):
    return sum(moveState(data, (i, j), state, move) * U[i][j] for i in range(N[0]) for j in range(N[1]))

# Find the value of a move
def moveState(data, sprime, state, move):
    def update_temp_state(move_delta):
        temp_state = (state[0] + move_delta[0], state[1] + move_delta[1])
        if not isValid(data, temp_state):
            temp_state = state
        return temp_state

    value = 0
    if move == "Up":
        value += 0.8 if update_temp_state((-1, 0)) == sprime else 0
        value += 0.1 if update_temp_state((0, -1)) == sprime else 0
        value += 0.1 if update_temp_state((0, 1)) == sprime else 0
    elif move == "Down":
        value += 0.8 if update_temp_state((1, 0)) == sprime else 0
        value += 0.1 if update_temp_state((0, -1)) == sprime else 0
        value += 0.1 if update_temp_state((0, 1)) == sprime else 0
    elif move == "Left":
        value += 0.8 if update_temp_state((0, -1)) == sprime else 0
        value += 0.1 if update_temp_state((-1, 0)) == sprime else 0
        value += 0.1 if update_temp_state((1, 0)) == sprime else 0
    elif move == "Right":
        value += 0.8 if update_temp_state((0, 1)) == sprime else 0
        value += 0.1 if update_temp_state((-1, 0)) == sprime else 0
        value += 0.1 if update_temp_state((1, 0)) == sprime else 0

    return value


# TODO: Implement value iteration algorithm here
def value_iteration(environment_file, non_terminal_reward, gamma, K):
    # Load csv file into data
    data = []
    with open(environment_file) as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            data.append(row)

    N = len(data), len(data[0])
    pi = np.chararray(N, unicode=True)
    Uprime = np.zeros(N)

    # Iterate through K times
    for loop in range(K):
        U = Uprime.copy()
        for i in range(N[0]):
            for j in range(N[1]):
                if data[i][j] == "X":
                    Uprime[i][j] = 0
                    pi[i][j] = "x"
                elif data[i][j] != ".":
                    Uprime[i][j] = float(data[i][j])
                    pi[i][j] = "o"
                else:
                    maxValue = 0
                    for move in movements:
                        value = findMax(data, (i, j), U, N, move)
                        maxValue = max(value, maxValue)

                        if value == maxValue:
                            pi[i][j] = movements[move]
                    Uprime[i][j] = R(data, (i, j), non_terminal_reward) + gamma * maxValue

    # Print utilities
    print("utilities:")
    for i in range(len(U)):
        for j in range(len(U[0])):
            print("{:6.3f}".format(U[i][j]), end=' ')
        print()

    # Print policy
    print("\npolicy:")
    for i in range(len(pi)):
        for j in range(len(pi[0])):
            print("{:6s}".format(pi[i][j]), end=' ')
        print()