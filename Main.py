import random

from Node import Node
from PriorityQueue import PriorityQueue


def astar(state):
    # initialize the frontier
    frontier = PriorityQueue()
    node0 = Node(state, None)
    frontier.push(node0)

    while True:
        solution = []

        if frontier.isempty():
            print("Failure. There is no solution!")
            return None

        leafnode = frontier.pop()
        if leafnode.state == goal_state:
            print("GOAL!")
            solution.append(leafnode.state)
            while leafnode.parent is not None:
                leafnode = leafnode.parent
                solution.append(leafnode.state)
            return solution

        # add child and traverse the children of leafnode
        for i in range(2, len(leafnode.state)):
            childstate = leafnode.flip(i)
            childnode = Node(childstate, leafnode)
            leafnode.add_child(childnode)
            childnode.calculate_priority()

            if not frontier.find(childnode):
                frontier.push(childnode)
            else:
                node_in_queue = frontier.get_node(childnode)
                if node_in_queue.priority > childnode.priority:
                    frontier.delete(node_in_queue)
                    frontier.push(childnode)


def ucs(state):
    # initialize the frontier
    frontier = PriorityQueue()
    node0 = Node(state, None)
    frontier.push(node0)

    while True:
        solution = []

        if frontier.isempty():
            print("Failure. There is no solution!")
            return None

        leafnode = frontier.pop()
        if leafnode.state == goal_state:
            print("GOAL!")
            solution.append(leafnode.state)
            while leafnode.parent is not None:
                leafnode = leafnode.parent
                solution.append(leafnode.state)
            return solution

        # add child and traverse the children of leafnode
        for i in range(2, len(leafnode.state)):
            childstate = leafnode.flip(i)
            childnode = Node(childstate, leafnode)
            leafnode.add_child(childnode)
            childnode.calculate_priority()
            childnode.priority = childnode.backCost

            if not frontier.find(childnode):
                frontier.push(childnode)
            else:
                node_in_queue = frontier.get_node(childnode)
                if node_in_queue.priority > childnode.priority:
                    frontier.delete(node_in_queue)
                    frontier.push(childnode)


cake_state = [1, 2, 3, 4, 5]
goal_state = [1, 2, 3, 4, 5, 6]
random.shuffle(cake_state)
cake_state.append(6)

print(ucs(cake_state)[::-1])