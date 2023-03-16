import sys 
sys.path.append("delivery_network/")

from graph import time_estimator

# Avec routes 1 on obtient environ 2E-2 secs pour l'ensemble des trajets
# Avec routes 2 on obtient plus de 4000h pour l'ensemble des trajets
# Avec routes 3 on obtient plus de 20 000h pour l'ensemble des trajets
# Avec routes 4 on obtient plus de 20 000h pour l'ensemble des trajets
# Avec routes 5 on obtient plus de 30 000h pour l'ensemble des trajets
# Avec routes 6 on obtient plus de 200 000 h pour l'ensemble des trajets
# Avec routes 7 on obtient plus de 200 000 h pour l'ensemble des trajets
# Avec routes 8 on obtient plus de 200 000 h pour l'ensemble des trajets
# Avec routes 9 on obtient plus de 200 000 h pour l'ensemble des trajets
# Avec routes 10 on obtient plus de 200 000 h pour l'ensemble des trajets

for i in range (1, 11, 1):
    print(f"Avec la route {i}, on obtient {time_estimator(nb_essais = 1, numero = i, arbre = True)} secs pour déterminer l'ensemble des trajets")