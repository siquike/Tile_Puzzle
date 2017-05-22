#!/usr/bin/env python3

import numpy as np
import itertools
from heapdict import heapdict
from copy import deepcopy
import pdb

def main():
    # This is a sample main function that shows examples and expected
    # outputs of calling the heuristic and astar functions.
    #
    # It is called in the conditional at the bottom if this file
    # if the main file your interpreter is running on and it is
    # not called when this file is used as a module for our grading.
    # You do not have to delete this function before submitting
    # the file for grading.

    initState = (2, 8, 3, 1, 0, 5, 4, 7, 6)
    print('=== heuristic_misplaced')
    print(' + Expected value: {}'.format(7))
    print(' +     Your value: {}'.format(heuristic_misplaced(initState)))
    print('=== heuristic_manhattan')
    print(' + Expected value: {}'.format(8))
    print(' +     Your value: {}'.format(heuristic_manhattan(initState)))
    print('=== astar_misplaced')
    expectedPath = 'ulddrurd'
    expectedStates = [
        (2, 8, 3, 1, 0, 5, 4, 7, 6),
        (2, 8, 3, 1, 5, 0, 4, 7, 6),
        (2, 8, 3, 1, 5, 6, 4, 7, 0),
        (2, 0, 3, 1, 8, 5, 4, 7, 6),
        (0, 2, 3, 1, 8, 5, 4, 7, 6),
        (1, 2, 3, 0, 8, 5, 4, 7, 6),
        (1, 2, 3, 4, 8, 5, 0, 7, 6),
        (1, 2, 3, 4, 8, 5, 7, 0, 6),
        (1, 2, 3, 4, 0, 5, 7, 8, 6),
        (1, 2, 3, 4, 5, 0, 7, 8, 6),
        (1, 2, 3, 4, 5, 6, 7, 8, 0)
    ]
    path, states = astar(initState, heuristic_misplaced)
    print(' + Expected path: {}'.format(expectedPath))
    print(' +     Your path: {}'.format(path))
    print(' + Expected states:')
    for i in range(len(expectedStates)):
        print('   + {}'.format(expectedStates[i]))
    print(' + Your states:')
    for i in range(len(states)):
        print('   + {}'.format(states[i]))

    print('=== astar_manhattan')
    expectedPath = 'ulddrurd'
    expectedStates = [
        (2, 8, 3, 1, 0, 5, 4, 7, 6),
        (2, 0, 3, 1, 8, 5, 4, 7, 6),
        (0, 2, 3, 1, 8, 5, 4, 7, 6),
        (1, 2, 3, 0, 8, 5, 4, 7, 6),
        (1, 2, 3, 4, 8, 5, 0, 7, 6),
        (1, 2, 3, 4, 8, 5, 7, 0, 6),
        (1, 2, 3, 4, 0, 5, 7, 8, 6),
        (1, 2, 3, 4, 5, 0, 7, 8, 6),
        (1, 2, 3, 4, 5, 6, 7, 8, 0)
    ]
    path, states = astar(initState, heuristic_manhattan)
    print(' + Expected path: {}'.format(expectedPath))
    print(' +     Your path: {}'.format(path))
    print(' + Expected states:')
    for i in range(len(expectedStates)):
        print('   + {}'.format(expectedStates[i]))
    print(' + Your states:')
    for i in range(len(states)):
        print ('    + {}'.format(states[i ]))


def heuristic_misplaced(state):
    """
    The number of misplaced tiles.
    The blank space is not tile and should
    not be included in your misplaced tile count.

     :param state: A tuple of the flattened board.
    :return: The number of misplaced tiles.
    """
    count = 0
    finalstate = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    # [TODO: Your implementation here]
    for number in range(len(state)):
        if state[number] != finalstate[number] and state[number] != 0:
            count = count + 1
    return count

def heuristic_manhattan(state):
    """
    The sum of the Manhattan distances from the
    misplaced tiles to their correct positions.*

    :param state: A tuple of the flattened board.
    :return: The summed manhattan distances.
    """
    total = 0
    finalstate = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    for i in range(len(state)):
        if state[i] != finalstate[i] and state[i] != 0:
            idx_finalstate = finalstate.index(state[i])
            staten = np.reshape(state,(3,3))
            finalstaten = np.reshape(finalstate,(3,3))
            idx_state = np.unravel_index(i,staten.shape)
            idx_finalstate = np.unravel_index(idx_finalstate,finalstaten.shape)
            total = total + abs(idx_state[0] - idx_finalstate[0]) + abs(idx_state[1] - idx_finalstate[1])
    return total


def neighbors(current):
    neighbors = []
    index = current.index(0)
    subind = np.unravel_index(index,(3,3))
    subindList = list(subind)
    subneighbors = [subindList[0]-1, subindList[0]+1, subindList[1]-1, subindList[1]+1]
    currentSub = np.reshape(current,(3,3))
    if subneighbors[0] > -1:
        n1 = deepcopy(currentSub)
        n1[subindList[0],subindList[1]] = currentSub[subneighbors[0],subindList[1]]
        n1[subneighbors[0],subindList[1]] = currentSub[subindList[0],subindList[1]]
        n1 = (tuple(n1.ravel()),'u')
        neighbors.append(n1)
    if subneighbors[1] < 3:
        n2 = deepcopy(currentSub)
        n2[subindList[0],subindList[1]] = currentSub[subneighbors[1],subindList[1]]
        n2[subneighbors[1],subindList[1]] = currentSub[subindList[0],subindList[1]]
        n2 = (tuple(n2.ravel()),'d')
        neighbors.append(n2)
    if subneighbors[2] > -1:
        n3 = deepcopy(currentSub)
        n3[subindList[0],subindList[1]] = currentSub[subindList[0],subneighbors[2]]
        n3[subindList[0],subneighbors[2]] = currentSub[subindList[0],subindList[1]]
        n3 = (tuple(n3.ravel()),'l')
        neighbors.append(n3)
    if subneighbors[3] < 3:
        n4 = deepcopy(currentSub)
        n4[subindList[0],subindList[1]] = currentSub[subindList[0],subneighbors[3]]
        n4[subindList[0],subneighbors[3]] = currentSub[subindList[0],subindList[1]]
        n4 = (tuple(n4.ravel()),'r')
        neighbors.append(n4)
    return neighbors


def reconstruct_path(cameFrom, current):
    path = str()
    while current in cameFrom.keys():
        current = cameFrom[current]
        path = current[1] + path
        current = current[0]
    return path


def astar(init_state, heuristic):
    """
    A^* implementation.

    :param init_state: A tuple of the flattened board.
    :param heuristic: The heuristic function
    :return: A tuple where:
        The first element is a string representing the optimal path.
            Use the characters 'r', 'l', 'u', and 'd' for
            'right', 'left', 'up', and 'down' directions, respectively.
        The second element is a list that contains states in the
            in order they were visited by your algorithm.
    """
    states_visited = []
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    gScore = 0
    fScore = heuristic(init_state) + gScore
    cameFrom = {}
    closedSet = {}
    openSet = heapdict()
    openSet[init_state] = (fScore,init_state,gScore,'')
    """
    Followed pseudo code in wikipedia: https://en.wikipedia.org/wiki/A*_search_algorithm
    """
    while openSet != ():
        current = openSet.popitem()
        states_visited.append(current[0])
        if current[0] == goal:
            return reconstruct_path(cameFrom, current[1][1]), states_visited
        closedSet[current[0]] = current[1]

        for neighbor in neighbors(current[0]):
            if neighbor[0] in closedSet:
                continue
            if neighbor[0] not in openSet:
                # State from which came from and direction
                cameFrom[neighbor[0]] = (current[0],neighbor[1])
                gScore = current[1][2] + 1
                fScore = gScore + heuristic(neighbor[0])
                openSet[neighbor[0]] = (fScore,neighbor[0],gScore,neighbor[1])
    return 'failure'


if __name__=='__main__':
    main()
