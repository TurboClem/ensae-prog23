from graph import *


data_path = "/home/onyxia/work/ensae-prog23/input/"
file_name = "network.00.in"

g = graph_from_file(data_path + file_name)
print(g)
print(path_existence(g, 1, 3))
print(g.get_path_with_power(1, 4, 15))
print(good_path(g, [1,2,3], 15))