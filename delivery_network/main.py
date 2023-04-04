from graph import *

data_path = "/home/onyxia/work/ensae-prog23/input/"
filename = "network.2.in"

t0 = time.perf_counter()
g = graph_from_file(data_path + filename)
t1 = time.perf_counter()
print("graph_from_file prend : ", t1-t0)

g = kruskal(g)
#for i in range (3):
    #print(g[i])
