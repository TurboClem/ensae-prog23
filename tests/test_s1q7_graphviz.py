# on a essayé 2-3 trucs pour graphviz, mais on a pas encore trop compris la doc
from graph import graph_from_file
import graphviz
data_path = "/home/onyxia/work/ensae-prog23/input/"


def visualisation (network) :

    w = graph_from_file(data_path + network)

    viz = graphviz.Digraph(comment = "Joli graphe")
    for node in w.nodes :
        viz.node(str(node), str(node))

     for edge in w.graph :
        for liste in w.graph[edge] :
            viz.edge(str(edge),str(liste[0]))
   
    return viz.source()​