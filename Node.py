class Node:
    def __init__(self, state, parent):
        self.children = []
        self.state = state
        self.parent = parent
        self.backCost = 0
        self.foreCost = 0
        self.priority = 0

    def add_child(self, child):
        self.children.append(child)

    def backward_cost(self):
        if self.parent is None:
            self.backCost = 0
        else:
            self.backCost = self.parent.backCost + 1
        return self.backCost

    # heuristic function
    def forward_cost(self):
        for i in range(len(self.state)-1):
            if abs(self.state[i+1] - self.state[i]) != 1:
                self.foreCost += 1
        return self.foreCost

    # priority in the queue
    def calculate_priority(self):
        self.priority = self.backward_cost() + self.forward_cost()

    # flip in the position. if position = 1, then flip the top one cake; if position = 2, then flip the top 2 cake.
    def flip(self, position):
        if position <= 1 or position > len(self.state):
            return None
        else:
            return self.state[position - 1::-1] + self.state[position:len(self.state)]
