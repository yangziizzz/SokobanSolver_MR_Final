from time import time
from copy import deepcopy
from custom_fifo import MyQueue

'''
Executes breadth-first search
uses MyQueue to keep track of frontier
'''


def print_results(board, gen, rep, fri, expl, dur):
    print("\n1. Breadth-first search")
    print("Solution: " + board.getDirections())
    print("Nodes generated: " + str(gen))
    print("Nodes repeated: " + str(rep))
    print("Fringe nodes: " + str(fri))
    print("Explored nodes: " + str(expl))
    print('Duration: ' + str(dur) + ' secs')


def search(board):
    start = time()
    curr_time = start
    nodes_generated = 0
    nodes_repeated = 0
    if board.is_win():
        end = time()
        print_results(board, 1, 0, 0, 1, end - start)
        return board, 1, 0, 0, 1, end - start, "Solved"
    node = deepcopy(board)
    nodes_generated += 1
    frontier = MyQueue()
    frontier.push(node)
    explored = set()
    keepLooking = True
    while (curr_time - start <= 60):
        if frontier.isEmpty():
            print("Solution not found")
            return board, nodes_generated, nodes_repeated, len(frontier), len(explored), end - start, "Not solved" 
        else:
            currNode = frontier.pop()
            moves = currNode.moves_available()
            currNode.fboxes = frozenset(currNode.boxes)
            explored.add(currNode)
            for m in moves:
                child = deepcopy(currNode)
                nodes_generated += 1
                child.move(m)
                if child not in explored:
                    if child.is_win():
                        end = time()
                        print_results(child, nodes_generated, nodes_repeated, len(
                                      frontier), len(explored), end - start)
                        return child, nodes_generated, nodes_repeated, len(
                                      frontier), len(explored), end - start, "Solved"
                    frontier.push(child)
                else:
                    nodes_repeated += 1
        curr_time = time()
