import math
class Graph:

    def __init__(self,vertices):
        self.v = vertices
        self.graph = []

    def edges(self,u,v,w):
        self.graph.append([u,v,w])

    def BellmanFord(self, source):

        dist = [math.inf]* self.v
        dist[source] = 0

        for i in range(self.v - 1):
            for sources,dest, weights in self.graph:
                if dist[dest] > dist[sources] + weights:
                    dist[dest] = dist[sources] + weights

        for sources,dest,weights in self.graph:
            if dist[dest] > dist[sources] + weights:
                print("graph has negative weight cycle")
                return (-1)

        return dist

#taking values from geeks for geeks
g = Graph(5)
g.edges(0,1,-1)
g.edges(0, 2, 4)
g.edges(1, 2, 3)
g.edges(1, 3, 2)
g.edges(1, 4, 2)
g.edges(3, 2, 5)
g.edges(3, 1, 1)
g.edges(4, 3, -3)

y = g.BellmanFord(0)
print(y)
