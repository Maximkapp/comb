class Graph:
    def __init__(self):
        self.vertex_map = {}  # Словарь для отображения вершин в индексы
        self.edges = []       # Список рёбер

    def add_edge(self, vertex1, vertex2, weight):
        # Преобразуем имена вершин в индексы
        if vertex1 not in self.vertex_map:
            self.vertex_map[vertex1] = len(self.vertex_map)
        if vertex2 not in self.vertex_map:
            self.vertex_map[vertex2] = len(self.vertex_map)

        v1_index = self.vertex_map[vertex1]
        v2_index = self.vertex_map[vertex2]

        self.edges.append(Edge(v1_index, v2_index, weight))

    def kruskal(self):
        mst = []
        uf = UnionFind(len(self.vertex_map))  # Количество уникальных вершин

        # Сортировка рёбер по весу
        sorted_edges = sorted(self.edges, key=lambda e: e.weight)

        for edge in sorted_edges:
            u = uf.find(edge.vertex1)
            v = uf.find(edge.vertex2)

            if u != v:
                mst.append(edge)
                uf.union(u, v)

        return mst


class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


if __name__ == "__main__":
    graph = Graph()

    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 3)
    graph.add_edge("B", "C", 2)
    graph.add_edge("C", "D", 4)
    graph.add_edge("B", "D", 5)

    mst = graph.kruskal()

    print("Минимальное остовное дерево:")
    for edge in mst:
        print(f"{edge.vertex1} - {edge.vertex2}: {edge.weight}")