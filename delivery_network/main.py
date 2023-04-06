from graph import *

data_path = "/home/onyxia/work/ensae-prog23/input/"
filename = "network.4.in"

t0 = time.perf_counter()
g = graph_from_file(data_path + filename)
t1 = time.perf_counter()
print("graph_from_file prend : ", t1-t0)

g = kruskal(g)

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

#print(g[2][15870], g[2][28162])


print("kruskal fait")
print(get_path(*g, 27591, 39067))
print("fini !")

"""
for i in range (1, 3, 1):
    print(g[i])
"""
