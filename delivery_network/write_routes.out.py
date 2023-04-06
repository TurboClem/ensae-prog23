from graph import *

with open(filename, "r", encoding = "utf-8") as file:
    line0 = file.readline().split()
    if len(line0) == 2:
        n, m = map(int, line0)
        g = Graph(range(1, n+1))
    else :
        m = int(line0[0])
        g = Graph()

    for _ in range(m):
        edge = list(map(write_number, file.readline().split()))
        if len(edge) == 3:
            node1, node2, power_min = edge
            g.add_edge(node1, node2, power_min) # will add dist=1 by default
        elif len(edge) == 4:
            node1, node2, power_min, dist = edge
            g.add_edge(node1, node2, power_min, dist)
        else:
            raise Exception("Format incorrect")
return g
