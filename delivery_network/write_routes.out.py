from graph import *

data_path = "/home/onyxia/work/ensae-prog23/input/"

def write_routes_out(numero):

    powers = []

    g = kruskal(graph_from_file(data_path + f"network.{numero}.in"))
    with open(data_path + f"routes.{numero}.in", "r", encoding = "utf-8") as file:
        nb_trajets = int(file.readline().split()[0])
        for _ in range (nb_trajets):
            node1, node2, utiliy = map(write_number, file.readline().split())
            powers.append(new_min_power(*g, node1, node2))


    with open(data_path + f"routes.{numero}.out", "w", encoding = "utf-8") as file:
        for power in powers:
            file.write(f"{power}\n")


for i in range (1, 11):
    write_routes_out(i)