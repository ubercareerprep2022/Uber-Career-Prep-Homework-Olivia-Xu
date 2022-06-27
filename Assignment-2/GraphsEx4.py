from collections import deque

class UndirectedGraph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, key):
        self.nodes[key] = []

    def addEdge(self, node1, node2):
        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)

    def minNumberOfEdges(self, node1, node2):
        distance = 1
        queue = deque()
        queue.append(node1)
        visited = set()
        while len(queue) > 0:
            length = len(queue)
            for i in range(length):
                currNode = queue.popleft()
                if currNode not in visited:
                    visited.add(currNode)
                    if node2 in self.nodes[currNode]:
                        return distance
                    queue += self.nodes[currNode]
            distance += 1

graph = UndirectedGraph()

for num in range(0, 7):
    graph.addNode(num)

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(0, 4)
graph.addEdge(1, 2)
graph.addEdge(2, 5)
graph.addEdge(3, 4)
graph.addEdge(4, 5)
graph.addEdge(4, 6)

print(graph.minNumberOfEdges(1, 5))
print(graph.minNumberOfEdges(6, 1))
