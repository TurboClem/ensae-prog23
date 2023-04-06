from graph import *


data_path = "/home/onyxia/work/ensae-prog23/input/"
filename = "network.00.in"
g = graph_from_file(data_path + filename)

g.graph_viz(00, 8, 10, 11)


print(g.min_power(1, 3))
