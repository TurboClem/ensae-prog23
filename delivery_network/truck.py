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
def stupid(truck_nb, routes_nb):
    catalogue = catalogue(truck_nb)
    
