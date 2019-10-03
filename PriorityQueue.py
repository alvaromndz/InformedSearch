import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item):
        heapq.heappush(self._queue, (item.priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def isempty(self):
        return len(self._queue) == 0

    def find(self, node):
        for i in self._queue:
            node_in_queue = i[-1]
            if node.state == node_in_queue.state:
                return True
        return False

    # get node with the same state
    def get_node(self, node):
        for i in self._queue:
            node_in_queue = i[-1]
            if node.state == node_in_queue.state:
                return node_in_queue
        return None

    def delete(self, node):
        for i in self._queue:
            node_in_queue = i[-1]
            if node.state == node_in_queue.state:
                self._queue.remove(i)
                break
