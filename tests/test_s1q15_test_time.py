import sys 
sys.path.append("delivery_network/")

from graph import time_estimator

# En prenant le nombre d'essais de chemin à 10
# Avec routes 1 on obtient environ 3E-3 secs pour l'ensemble des trajets
# Avec routes 2 on obtient environ 6h pour l'ensemble des trajets
# Avec routes 3 on obtient environ 20h pour l'ensemble des trajets
# Avec routes 4 on obtient environ 17h pour l'ensemble des trajets
# Avec routes 5 on obtient environ 8h pour l'ensemble des trajets
# Avec routes 6 on obtient plus de h pour l'ensemble des trajets
# Avec routes 7 on obtient plus de h pour l'ensemble des trajets
# Avec routes 8 on obtient plus de h pour l'ensemble des trajets
# Avec routes 9 on obtient plus de h pour l'ensemble des trajets
# Avec routes 10 on obtient plus de h pour l'ensemble des trajets

for i in range (1, 11, 1):
    print(f"Avec la route {i}, on obtient {time_estimator(nb_essais = 10, numero = i, arbre = True)} secs pour déterminer l'ensemble des trajets")

