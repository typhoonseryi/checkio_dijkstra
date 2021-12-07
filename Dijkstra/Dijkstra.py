from Heap import Heap


class Vertex:
    def __init__(self, name="Unknown", dist=float("inf"), prev=None, done=False):
        self.name = name
        self.dist = dist
        self.prev = prev
        self.done = done


class PathFinder:
    def __init__(self, edges = []):
        self.edges = edges

    def dijkstra(self, s):
        s.dist = 0
        h = Heap()
        h.insert((0, s))
        while not h.is_empty:
            dist_tov = h.pop()
            weight, v = dist_tov
            if not v.done:
                v.done = True
                print((weight, v.name))
                for _, w, d in [e for e in self.edges if e[0] == v]:
                    c = v.dist + d
                    if c < w.dist:
                        w.prev = v
                        w.dist = c
                        h.insert((c, w))

    def bfs(self):
        pass


if __name__ == "__main__":

    print("Example 1")

    node1 = Vertex(name="1")
    node2 = Vertex(name="2")
    node3 = Vertex(name="3")
    node4 = Vertex(name="4")
    edges = [
        (node1, node2, 1),
        (node1, node4, 4),
        (node2, node3, 1),
        (node4, node3, 3)
    ]
    p = PathFinder(edges)
    p.dijkstra(node1)

    print("Example 2")

    node0 = Vertex(name="0")
    node1 = Vertex(name="1")
    node2 = Vertex(name="2")
    node3 = Vertex(name="3")
    node4 = Vertex(name="4")
    node5 = Vertex(name="5")
    node6 = Vertex(name="6")
    edges = [
        (node0, node2, 3),
        (node0, node3, 17),
        (node0, node4, 4),
        (node0, node6, 6),
        (node1, node0, 2),
        (node2, node6, 1),
        (node4, node0, 4),
        (node5, node3, 1),
        (node6, node5, 1)
    ]
    p = PathFinder(edges)
    p.dijkstra(node1)

