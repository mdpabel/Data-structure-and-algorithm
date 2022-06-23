class Graph:
    def __init__(self, gDict) -> None:
        if gDict is None:
            self.gDict = {}
        self.gDict = gDict

    def addEdges(self, vertex, edge):
        if vertex in self.gDict:
            self.gDict[vertex].append(edge)
        else:
            self.gDict[vertex] = [edge]


graph_elements = {
    'a': [2, 3],
    'b': [1, 2],
    'c': [1, 2, 4],
    'd': [1, 3]
}

graph = Graph(graph_elements)

graph.addEdges('a', 4)

print(graph.gDict)
