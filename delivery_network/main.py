from graph import *

data_path = "/home/onyxia/work/ensae-prog23/input/"
filename = "network.1.in"


g = kruskal(graph_from_file(data_path + filename))
for i in range (3):
    print(g[i])




