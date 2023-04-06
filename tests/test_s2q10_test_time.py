#import sys 
#sys.path.append("delivery_network/")

from graph import time_estimator

for i in range (1, 11, 1):
    print(time_estimator(nb_essais = 1, numero = i, arbre = False))

# Test pour les graphes, avant d'avoir construit des arbres.
# Avec routes 1 on obtient environ 6E-3 secs pour l'ensemble des trajets
# Avec routes 2 on obtient plus de 8000h pour l'ensemble des trajets
# Avec routes 3 on obtient un peu moins de 50 000h pour l'ensemble des trajets
# Avec routes 4 on obtient un peu moins de 50 000h pour l'ensemble des trajets
# Avec routes 5 on obtient plus de 30 000h pour l'ensemble des trajets
# Avec routes 6 on obtient plus de 200 000 h pour l'ensemble des trajets
# On s'arrête là parce que c'est long et on a compris


