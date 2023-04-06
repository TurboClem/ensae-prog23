import sys 
sys.path.append("delivery_network/")

from graph import time_estimator


# Au début, pour route 5, on trouve un temps de calcul moyen par trajet de 10min 40sec, soit plus d'1,5 millions d'heures
# pour l'ensemble des trajets. C'est bien trop.

# En prenant le nombre d'essais de chemin à 10
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


# Maintenant, on arrive à ces résultats :

#Le temps d'exécution de graph_from_file pour 1 est : 0.00039565982297062874
#Le temps d'exécution de Kruskal pour 1 est : 0.0003715776838362217
#Avec la route 1, on obtient 0.0004162359982728958 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 2 est : 0.42153272312134504
#Le temps d'exécution de Kruskal pour 2 est : 1.0222180499695241
#Avec la route 2, on obtient 0.1573729943484068 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 3 est : 0.8512480151839554
#Le temps d'exécution de Kruskal pour 3 est : 1.4704720242880285
#Avec la route 3, on obtient 27.05862465593964 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 4 est : 1.0548750790767372
#Le temps d'exécution de Kruskal pour 4 est : 2.0790683259256184
#Avec la route 4, on obtient 28.65197527129203 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 5 est : 1.118838959839195
#Le temps d'exécution de Kruskal pour 5 est : 2.811459498014301
#Avec la route 5, on obtient 4.537270399741828 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 6 est : 1.0982548827305436
#Le temps d'exécution de Kruskal pour 6 est : 2.83025613008067
#Avec la route 6, on obtient 26.84126812731847 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 7 est : 1.2138134678825736
#Le temps d'exécution de Kruskal pour 7 est : 2.8640354089438915
#Avec la route 7, on obtient 27.116631025914103 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 8 est : 1.261315643787384
#Le temps d'exécution de Kruskal pour 8 est : 2.8951145610772073
#Avec la route 8, on obtient 22.670592742506415 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 9 est : 1.2360173696652055
#Le temps d'exécution de Kruskal pour 9 est : 2.7909739180468023
#Avec la route 9, on obtient 20.256559880450368 secs pour déterminer l'ensemble des trajets

#Le temps d'exécution de graph_from_file pour 10 est : 1.2830187031067908
#Le temps d'exécution de Kruskal pour 10 est : 2.6913598920218647
#Avec la route 10, on obtient 27.31225882144645 secs pour déterminer l'ensemble des trajets

# Estimation du temps moyen de calcul :
def time_estimator(nb_essais, numero, arbre = True):
    """
    Mesure pour le fichier routes.numero.in le temps de calcul moyen d'un trajet
    """
    data_path = "/home/onyxia/work/ensae-prog23/input/"
    t0 = time.perf_counter()
    g = graph_from_file(data_path + f"network.{numero}.in")
    t1 = time.perf_counter()
    print(f"Le temps d'exécution de graph_from_file pour {numero} est : {t1 - t0}")
    if arbre :
        t0 = time.perf_counter()
        g = kruskal(g)
        t1 = time.perf_counter()
        print(f"Le temps d'exécution de Kruskal pour {numero} est : {t1 - t0}")
    total = 0
    with open(data_path + f"routes.{numero}.in", "r", encoding = "utf-8") as file:
        nb_trajets = int(file.readline().split()[0])
        for _ in range(min(nb_essais, nb_trajets)):
            trajet = file.readline().split()
            node1 = int(trajet[0])
            node2 = int(trajet[1])
            utility = write_number(trajet[2])
            if arbre :
                t0 = time.perf_counter()
                new_min_power(*g, node1, node2)
                t1 = time.perf_counter()
            else :
                t0 = time.perf_counter()
                g.min_power(node1, node2)
                t1 = time.perf_counter()

            total += t1 - t0
    mean_time = total/min(nb_trajets, nb_essais)
    return (mean_time * nb_trajets)


# Si on veut voir tous les trajets, on prend (nb_essai > nb_trajets)
for i in range (1, 11, 1):
    print(f"Avec la route {i}, on obtient {time_estimator(nb_essais = 1000000, numero = i, arbre = True)} secs pour déterminer l'ensemble des trajets")