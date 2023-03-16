from graph import Graph, graph_from_file

data_path = "/home/onyxia/work/ensae-prog23/input/"
file_name = "network.04.in"
g = graph_from_file(data_path + file_name)
# Avec routes 1 on obtient environ 6E-3 secs pour l'ensemble des trajets
# Avec routes 2 on obtient plus de 8000h pour l'ensemble des trajets
# Avec routes 3 on obtient un peu moins de 50 000h pour l'ensemble des trajets
# Avec routes 4 on obtient un peu moins de 50 000h pour l'ensemble des trajets
# Avec routes 5 on obtient plus de 30 000h pour l'ensemble des trajets
# Avec routes 6 on obtient plus de 200 000 h pour l'ensemble des trajets
# On s'arrête là parce que c'est long et on a compris
print(g)
print(g.get_path_with_power(1,4,99999))