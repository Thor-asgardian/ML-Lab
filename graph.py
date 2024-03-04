class Node:
    def _init_(self, data):
        self.data = data
        self.edges = []

    def add_edge(self, node):
        self.edges.append(node)


class Graph:
    def _init_(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def traverse(self, start_node):
        visited = []

        def dfs(node):
            visited.append(node)
            for edge in node.edges:
                if edge not in visited:
                    dfs(edge)

        dfs(start_node)

        return visited


if _name_ == "_main_":
    graph = Graph()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)

    node1.add_edge(node2)
    node2.add_edge(node3)

    visited = graph.traverse(node1)

    print(visited)
