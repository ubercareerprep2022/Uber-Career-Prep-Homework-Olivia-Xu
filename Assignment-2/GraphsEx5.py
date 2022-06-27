from GraphsEx1to3 import GraphWithAdjacencyList

def canFinish(numCourses, prereqs):
    courseGraph = GraphWithAdjacencyList()
    for i in range(numCourses):
        courseGraph.addNode(i)

    for p in prereqs:
        courseGraph.addEdge(p[1], p[0])
    
    visited = [False] * numCourses
    recStack = [False] * numCourses

    return not hasCycle(visited, recStack, 0 ,courseGraph)

def hasCycle(visited, recStack, key, graph):
    visited[key] = True
    recStack[key] = True
    for neighbor in graph.adjNodes[graph.getNodeByKey(key)]:
        keyNB = neighbor.data
        if visited[keyNB]:
            if recStack[keyNB]:
                return True
        else:
            return hasCycle(visited, recStack, keyNB, graph)
    recStack[key] = False
    return False

print(canFinish(2, [[1,0], [0, 1]]))