import sys 
sys.path.append("delivery_network/")

from graph import *

# Estimation du temps moyen de calcul :
# Si on veut voir tous les trajets, on prend (nb_essai > nb_trajets)
for i in range (1, 11, 1):
    print(f"Avec la route {i}, on obtient {time_estimator(nb_essais = 1000000, numero = i, arbre = True)} secs pour déterminer l'ensemble des trajets")

# En prenant le nombre d'essais de chemin à 10, avant d'avoir le dictionnaire previous
# Avec routes 1 on obtient environ 3E-3 secs pour l'ensemble des trajets
# Avec routes 2 on obtient environ 7h pour l'ensemble des trajets
# Avec routes 3 on obtient environ 17h pour l'ensemble des trajets
# Avec routes 4 on obtient environ 17h pour l'ensemble des trajets
# Avec routes 5 on obtient environ 8h pour l'ensemble des trajets
# Avec routes 6 on obtient environ 37h pour l'ensemble des trajets
# Avec routes 7 on obtient environ 39h pour l'ensemble des trajets
# Avec routes 8 on obtient environ 41h pour l'ensemble des trajets
# Avec routes 9 on obtient 40 40h pour l'ensemble des trajets
# Avec routes 10 on obtient plus de h pour l'ensemble des trajets


# Une fois le dictionnaire previous créé, on arrive à ces résultats :

#Le temps d'exécution de graph_from_file pour 1 est : 0.00039565982297062874
#Le temps d'exécution de kruskal pour 1 est : 0.0003715776838362217
#Avec la route 1, on obtient 0.0004162359982728958 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 2 est : 0.42153272312134504
#Le temps d'exécution de kruskal pour 2 est : 1.0222180499695241
#Avec la route 2, on obtient 0.1573729943484068 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 3 est : 0.8512480151839554
#Le temps d'exécution de kruskal pour 3 est : 1.4704720242880285
#Avec la route 3, on obtient 27.05862465593964 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 4 est : 1.0548750790767372
#Le temps d'exécution de kruskal pour 4 est : 2.0790683259256184
#Avec la route 4, on obtient 28.65197527129203 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 5 est : 1.118838959839195
#Le temps d'exécution de kruskal pour 5 est : 2.811459498014301
#Avec la route 5, on obtient 4.537270399741828 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 6 est : 1.0982548827305436
#Le temps d'exécution de kruskal pour 6 est : 2.83025613008067
#Avec la route 6, on obtient 26.84126812731847 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 7 est : 1.2138134678825736
#Le temps d'exécution de kruskal pour 7 est : 2.8640354089438915
#Avec la route 7, on obtient 27.116631025914103 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 8 est : 1.261315643787384
#Le temps d'exécution de kruskal pour 8 est : 2.8951145610772073
#Avec la route 8, on obtient 22.670592742506415 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 9 est : 1.2360173696652055
#Le temps d'exécution de kruskal pour 9 est : 2.7909739180468023
#Avec la route 9, on obtient 20.256559880450368 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 10 est : 1.2830187031067908
#Le temps d'exécution de kruskal pour 10 est : 2.6913598920218647
#Avec la route 10, on obtient 27.31225882144645 secs pour déterminer l'ensemble des trajets