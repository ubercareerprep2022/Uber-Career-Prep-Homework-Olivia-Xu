from collections import deque

class GraphNode:
    def __init__(self, data):
        self.data = data

class GraphWithAdjacencyList:
    def __init__(self):
        self.adjNodes = {}
    
    def getKeys(self):
        return [node.data for node in self.adjNodes.keys()]

    def getNodeByKey(self, key):
        for node in self.adjNodes.keys():
            if node.data == key:
                return node

    # Assuming there cannot be duplicates
    def addNode(self, key):
        if key in self.getKeys():
            exit('This node already exits in this graph.')
        newNode = GraphNode(key)
        self.adjNodes[newNode] = []

    def removeNode(self, key):
        toBeRemoved = GraphNode(key)
        if toBeRemoved not in self.adjNodes:
            exit('Cannot find this node in this graph.')
        del self.adjNodes[toBeRemoved]
        for node, list in self.adjNodes:
            if toBeRemoved in list:
                del self.adjNodes[node][toBeRemoved]

    # Assuming the graph is directed, and so the edge goes from node1 to node2
    def addEdge(self, node1, node2):
        if node1 not in self.getKeys() or node2 not in self.getKeys():
            exit('Cannot add an edge between non-existing node(s).')
        self.adjNodes[self.getNodeByKey(node1)].append(self.getNodeByKey(node2))

    def removeEdge(self, node1, node2):
        nodeOne = GraphNode(node1)
        nodeTwo = GraphNode(node2)
        if nodeOne not in self.adjNodes or nodeTwo not in self.adjNodes:
            exit('Cannot remove an edge between non-existing node(s).')
        if nodeOne in self.adjNodes[nodeTwo]:
            self.adjNodes[nodeTwo].remove(nodeOne)
        if nodeTwo in self.adjNodes[nodeOne]:
            self.adjNodes[nodeOne].remove(nodeTwo)

    def getAdjNodes(self, key):
        keyNode = GraphNode(key)
        if keyNode not in self.adjNodes:
            exit('Cannot find this node in this graph.')
        return self.adjNodes[keyNode]

    def DFS(self, key):
        
        if key not in self.getKeys():
            exit('Cannot find this node in this graph.')
        currNode = self.getNodeByKey(key)
        visited = {currNode}

        def DEF_helper(graph, currNode, visited):
            print(currNode.data, end='  ')
            visited.add(currNode)
            for node in graph[currNode]:
                if node not in visited:
                    DEF_helper(graph, node, visited)

        DEF_helper(self.adjNodes, currNode, visited)

    def BFS(self, key):
        if key not in self.getKeys():
            exit('Cannot find this node in this graph.')
        currNode = self.getNodeByKey(key)
        visited = {currNode}
        print(currNode.data, end="  ")
        nextLevel = deque(self.adjNodes[currNode])
        while len(nextLevel) > 0:
            length = len(nextLevel)
            for i in range(length):
                currNode = nextLevel.popleft()
                if currNode not in visited:
                    print(currNode.data, end='  ')
                    nextLevel += self.adjNodes[currNode]
                    visited.add(currNode)

# Construct the graph from the example

graph = GraphWithAdjacencyList()

for num in [2, 0, 1, 3]:
    graph.addNode(num)

graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(2, 1)
graph.addEdge(0, 2)
graph.addEdge(0, 1)
graph.addEdge(3, 3)

graph.DFS(2)
print()
graph.BFS(2)