from graph import *

data_path = "/home/onyxia/work/ensae-prog23/input/"

def catalogue(numero):
    catalogue = {}
    with open(data_path + f"trucks.{numero}.in", "r", encoding = "utf-8") as file:
        nb_trucks = int(file.readline().split()[0])
        for i in range (nb_trucks):
            power, price = map(write_number, file.readline().split())
            catalogue[numero, i] = (power, price)
    return catalogue


def data_routes(numero):
    data = {}
    with open(data_path + f"routes.{numero}.in", "r", encoding = "utf-8") as file:
        nb_trajets = int(file.readline().split()[0])
        for i in range(nb_trajets):
            node1, node2, utility = map(write_number, file.readline().split())
            data[numero, i] = (0, utility, node1, node2)
    with open(data_path + f"routes.{numero}.out", "r", encoding = "utf-8") as file:
        for i in range(nb_trajets):
            power = list((map(write_number, file.readline().split())))[0]
            data[numero, i] = (power, data[numero, i][1], data[numero, i][2], data[numero, i][3])
    return data


def stupid(truck_nb, routes_nb):
    catalog = catalogue(truck_nb)
    data = data_routes(routes_nb)

    optimized = []

    for trajet in data.keys():
        for key in catalog.keys():
            power_trajet, utility, node1, node2 = data[trajet]
            power_truck, price = catalog[key]
            if power_trajet <= power_truck :
                optimized += [[(key, trajet), utility/price]]

    optimized.sort(key = lambda x : x[1], reverse = True)

    results = []
    i = 0
    budget = 0
    while i < len(optimized) and budget <= 25*(10**9):
        (key, trajet) = optimized[i][0]
        power_truck, price = catalog[key]
        power_trajet, utility, node1, node2 = data[trajet]
        i += 1
        budget += price
        if budget <= 25*(10**9):
            results += [(f"camion {key[1]}", (node1, node2), utility)]

    return (results)


for i in range(1, 11):
    print(f"On commence {i}")
    stupid(2, i)

# Pour trucks 0, on peut faire tourner sur toutes les routes.
# Pour trucks 1, on peut faire tourner sur toutes les routes.
# Pour trucks 2, c'est plus compliqué dès la deuxième route.