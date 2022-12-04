#!/usr/bin/env python3

class Graph():
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance
    
    def print_path(self, initial, end):
        visited, paths = self.prim(initial)
        full_path = []

        while end != initial:
            full_path.append(end)
            end = paths[end]

        full_path.append(initial)
        full_path.reverse()

        print('Path: {}'.format(full_path))
        print('Cost: {}'.format(visited[full_path[-1]]))


    def prim(self, initial):
        visited = {initial: 0}
        path = {}

        nodes = set(self.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
                weight = current_weight + self.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path

if __name__ == '__main__':
    graph = Graph()

    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')
    graph.add_node('G')

    graph.add_edge('A', 'B', 2)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('C', 'E', 1)
    graph.add_edge('D', 'E', 1)
    graph.add_edge('D', 'F', 3)
    graph.add_edge('E', 'F', 2)
    graph.add_edge('E', 'G', 2)
    graph.add_edge('F', 'G', 2)

    graph.print_path('A', 'G')