from graph import representation, graph_from_file


data_path = "/home/onyxia/work/ensae-prog23/input/"


"""a = [(1, 2)]
for i in a:
    (b,c) = i
print(b,c)"""


"""
t0 = time.perf_counter()
g = graph_from_file(data_path + filename)
t1 = time.perf_counter()
print("graph_from_file prend : ", t1-t0)

g = kruskal(g)
"""
"""
#print(g[2].items())
for (k, l) in g[2].items():
    if l[0] == 15870:
        print(k, " pour 15870")
    if l[0] == 28162:
        print(k, " pour 28162")
#print(15870 in g[2].values())
"""

"""
d = {}
d[2] = [3, 4]
d[3] = []
d[2] = []
print(d.values())
#for n in d.values():
#    print (n)
"""


"""
print("kruskal fait")
print(get_path(*g, 27591, 39067))
print("fini !")
"""
"""
for i in range (1, 3, 1):
    print(g[i])
"""
"""
    def representation_graph(network):
    import graphviz
    g = graph_from_file(data_path + network)
    graphique = graphviz.Digraph("Réseau", comment = "Représentation du réseau")
    for node in g.nodes :
        graphique.node(str(node), str(node))
    graphique.attr(rankdir = "LR")
    for element in g.graph :
        for component in g.graph[element]:
            graphique.edge(str(element), str(component[0]))
    return graphique


display(representation_graph("network.00.in"))

"""

g = graph_from_file(data_path + "network.00.in")
representation(g, "ooooooh")