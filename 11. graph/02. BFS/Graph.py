from collections import deque


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

    def bfs(self, start):
        queue = deque()
        visited = set()

        queue.append(start)
        visited.add(start)

        while queue:
            item = queue.popleft()
            print(item)
            for neighbor in self.gDict[item]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


graph_elements = {
    3: [2, 4, 5],
    4: [0, 3, 5],
    5: [3, 4, 6],
    1: [2, 0],
    2: [1, 3],
    0: [1, 4],
    6: [5]
}

graph = Graph(graph_elements)

graph.bfs(1)
