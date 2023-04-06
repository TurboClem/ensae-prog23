import time
import sys
import random
from graphviz import Graph as gr


class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        # self.nodes = list(self.nodes) 
        # Evite l'erreur d'ajout de villes textuelles ("Paris") à self.nodes = range(,)
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. 
        Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.nodes :
            self.nodes += [node1]
            self.nb_nodes += 1
            self.graph[node1] = []
        
        if node2 not in self.nodes :
            self.nodes += [node2]
            self.nb_nodes += 1
            self.graph[node2] = []
            
        self.graph[node1] += [(node2, power_min, dist)]
        self.graph[node2] += [(node1, power_min, dist)]
        self.nb_edges += 1

        return


    def connected_components(self):
        """
        Returns a list of the graph's connected components 
        """ 
        connected_comp = []
        visited = set()
        
        for node in self.nodes:
            if node not in visited:
                component = set()
                neighborhood(self, node, component, visited)
                connected_comp.append(component)
        
        return connected_comp


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}


        Notons V le nombre de noeuds, E le nombre d'arrêtes.
        Guettons voir la complexité de l'algorithme.

        Regardons d'abord connected_components:
            Dans le pire des cas pour cette partie là de l'algorithme, tous les noeuds sont reliés entre eux.
            Alors on fait dans le pire des cas E*V opérations.
        
        Regardons maintenant reduction_ensembles :
        En exécutant reduction_ensembles, on fait d'abord len(l)**2 opérations, mais comme len(l) diminue de 1 à chaque fois,
            On fait SUM{i=1,E}(i**2) = E*(E+1)*(2*E+1)/2 = O(E**2) opérations
        Ensuite, dans le pire des cas, on parcourt à chaque fois deux fois la liste. 
                C'est à dire que i va jusqu'a len(l)-1 et j jusqu'à len(l) à chaque fois.
                Donc on fait SUM{i=1,E}(i*(i-1)) = O(E**3) opérations
        Alors on fait O(E***3) opérations

        Finalement, l'algorithme est de complexité O( max(E**3, E*V) ) 
        """
        return set(map(frozenset, self.connected_components()))


    def get_path_with_power(self, source, destination, power):
        """
        On utilise l'algorithme de Dijkstra
        """
        # On vérifie que source et destination sont bien reliables.
        # Si on s'occupe des networks on met ça
        # con_comp = path_existence(self, source, destination)
        # if con_comp == None:
        #    return None
        #unvisited = list(con_comp)
        
        # Si on s'occupe des routes on met ça (le graphe est alors connexe)
        unvisited = set(self.nodes[:])

        dmax = sys.maxsize # On définit la distance de tous les points à la source comme étant "infinie" (maxsize donc)
        node_distance = dict([(n, dmax) for n in unvisited])
        node_distance[source] = 0
        previous = {} #Va stocker pour chaque noeud, le noeud qui le précède dans le chemin le plus court vers la source

        # On parcourt tous les noeuds de la composante connectée
        while unvisited != set():
            # On trouve le noeud le plus proche de la source : nearest_node
            nearest_node = None
            for node in unvisited:
                if nearest_node == None:
                    nearest_node = node
                elif node_distance[node] < node_distance[nearest_node]:
                    nearest_node = node
            # On parcourt les voisins du nearest_node
            for neighbor in self.graph[nearest_node]:
                # On regarde si le voisin est plus proche de la source en passant par nearest_node que par l'ancien chemin
                new_distance = node_distance[nearest_node] + neighbor[2]
                if new_distance < node_distance[neighbor[0]] and neighbor[1] <= power:
                    node_distance[neighbor[0]] = new_distance
                    previous[neighbor[0]] = nearest_node
            unvisited.remove(nearest_node)
        path = [destination]
        i = destination
        while i != source:
            if i not in previous.keys():
                return None
            j = previous[i]
            path.insert(0, j)
            i = j
        return path
            

    def min_power(self, source, destination):
        """
        Returns min_power and the path relied with this min_power
        """
        path = self.get_path_with_power(source, destination, sys.maxsize)
        if path == None:
            return None, None
        pmax = 0
        # On récupère la puissance minimal nécessaire à un trajet faisable (donc en prenant un camion de puissance maxsize)
        for i in range(len(path)-1):
            for j in self.graph[path[i]]:
                if j[0] == path[i+1]:
                    if j[1] > pmax:
                        pmax = j[1]
        pmin = 0
        # On fait le choix de rester sur des puissances entières (c'est arbitraire)
        while pmax - pmin > 1: # A chaque fois on prend le quotient dans la division par 2, donc la parité peut changer
            path = self.get_path_with_power(source, destination, pmin + (pmax-pmin)//2)
            if path == None:
                pmin = pmin + (pmax-pmin)//2
            else :
                pmax = pmin + (pmax-pmin)//2

        if pmax - pmin == 1 :
            if path == None:
                return pmax, self.get_path_with_power(source, destination, pmax)
        return pmax, path
    
    def graph_viz(self, numero,  dep, dest, power):
        """
        Show the graph, highlighting the optimal path
        """
        data_path = "/home/onyxia/work/ensae-prog23/input/"
        filename = f"network.{numero}.in"


        graphe = gr(format='png', engine="circo") # on creer un graph
        trajet=self.get_path_with_power(dep, dest, power)
        key=self.graph.keys() # on récupere tous les sommets
        sauv=[]
        print("trajet=", trajet)

        for i in key: # on creer tous les sommets
            print(i)
            if i==dep: # si le sommet considéré est le départ
                print("le depart=", i)
                graphe.node(f"{i}",f"{i} \n départ", color="red")   # si le sommet est le départ, on le met en rouge
                for voisin in self.graph[i]:
                    print("le voisin est=", voisin)
                    print("trajet[1]=", trajet[1])
                                              
                    if voisin[0] not in sauv: # si le voisin n'as pas déja étét traité
                        print("entrée dans la boucle")
                        if voisin[0]==trajet[1]:
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}", color="red")
                            print("on met en rouge")
                        else: 
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")

            
            elif i == dest: # si le sommet considéré est l'arrivée
                graphe.node(f"{i}",f"{i} \n arrivée", color="red")  
                for voisin in self.graph[i]:
                    if voisin[0] not in sauv: # si le voisin n'as pas déja étét traité
                        if voisin[0]==trajet[-2]:
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}", color="red")
                        else: 
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")


            elif i in trajet: # si le voisin considéré est dans le trajet
                print("position du voisin dans trajet=", i)
                graphe.node(f"{i}",f"{i} ", color="orange")
                rang=trajet.index(i)
                for voisin in self.graph[i]:
                    if voisin[0] not in sauv: # si le voisin n'as pas déja étét traité
                        if voisin[0]==trajet[rang+1] or voisin[0]==trajet[rang-1]:
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}", color="red")
                            print("on met en rouge")
                        else: 
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")


            else: # sinon
                graphe.node(f"{i}",f"{i}")
                for voisin in self.graph[i]:
                    if voisin[0] not in sauv: # si le voisin n'as pas déja étét traité
                        graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")
            
            sauv.append(i)


        graphe.render(data_path + f"graphviz.dot")
        print(graphe)

        return()
    

def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    g: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r", encoding = "utf-8") as file:
        line0 = file.readline().split()
        #if len(line0) == 2:
        n, m = map(int, line0)
        g = Graph(range(1, n+1))
        #else : 
        #    m = int(line0[0])
        #    g = Graph()

        for _ in range(m):
            edge = list(map(write_number, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g



# Pour graph from file :
def write_number(a):
    """
    Writes string numbers as integers if they are, as floats if they are
    """
    a = float(a)
    return (int(a) if a == int(a) else a)


#Pour connected_components :
def neighborhood(g, node, component, visited):
    visited.add(node)
    component.add(node)
    for neighbor in g.graph[node]:
        if neighbor[0] not in visited:
            neighborhood(g, neighbor[0], component, visited)


# Estimation du temps moyen de calcul :
def time_estimator(nb_essais, numero, arbre = True):
    """
    Measure, for a file routes.numero.in the calculous time for min_power over the whole file 
    based on the calculous of nb_essais paths. When nb_essais >= nb_paths, we just calculate 
    all the paths. If arbre == True, we execute kruskal.
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
        print(f"Le temps d'exécution de kruskal pour {numero} est : {t1 - t0}")
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
                new_min_power(*g, node1, node2) # We use *g because kruskal returns graph, previous
                t1 = time.perf_counter()
            else :
                t0 = time.perf_counter()
                g.min_power(node1, node2)
                t1 = time.perf_counter()

            total += t1 - t0
    mean_time = total/min(nb_trajets, nb_essais)
    return (mean_time * nb_trajets)


# Pour kruskal
def initial_node(initial,node):
    """
    Takes as input initial (dictionnary) and node (int)
    Finds for the input node his initial_node (ie the node from which the connected component was created)
    """
    if initial[node] != node:
        initial[node] = initial_node(initial,initial[node])
    return initial[node]
    
def union(initial,rank,node1,node2):
    """
    Unites node1 to node2.
    Belonging to differents tree, union enable the tree to unite and it updates the dictionnary initial.
    We unite the biggest tree to the smallest (with rank)
    """
    i1 = initial_node(initial,node1)
    i2 = initial_node(initial,node2)
    if i1 == i2: 
        return None
    if rank[i2] < rank[i1]:
        initial[i2] = i1
    else:
        initial[i1]=i2
        if rank[i1] == rank[i2]:
            rank[i2] += 1
    return None

def kruskal(g):
    """ 
    Takes as input a graph. 
    Returns the most optimal tree that can be made from the input graph, regarding to power on the edges.
    Also returns the dictionnary of previous node when taking "1" for initial node.
    """
    g_mst = Graph(nodes = g.nodes)
    edges = []
    initial = {}        # Permettra de remonter au noeud initial de chaque composante connexe avec initial_node
                        # Le noeud initial permet d'indicer la composante connexe.
    rank = {}           # Le rang nous permettra de lier des gros arbres avec des petits
        
    # Chaque noeud a comme noeud initial lui même, et comme rang 0
    t0 = time.perf_counter()
    for node in g.nodes:
        if g.graph[node] != []:
            initial[node] = node
            rank[node] = 0
    for node in g.graph:
        for edge in g.graph[node]:
            edges.append((node,edge[0],edge[1])) # edges devient la liste des arrêtes notées (node1, node2, power)
    t1 = time.perf_counter()
    print("parcourt du graphe : ", t1-t0)
    edges.sort(key = lambda x : x[2]) # Permet de trier la liste par rapport à la troisième valeur des sous liste de la liste edge
    t2 = time.perf_counter()
    for edge in edges:
        if initial_node(initial,edge[0]) != initial_node(initial,edge[1]):
        # Si les bouts d'une arrête ne sont pas déjà dans la même composante connexe, alors on les unit.
            g_mst.add_edge(edge[0],edge[1],edge[2])
            union(initial,rank,edge[0],edge[1])
    t3 = time.perf_counter()
    print("parcourt des arrêtes : ", t3-t2)
    t4 = time.perf_counter()
    previous = dfs(g_mst, 1) 
    # On prend un noeud au hasard, ne sachant pas vraiment comment trouver un noeud central.
    t5 = time.perf_counter()
    print("get_previous prend : ", t5 - t4)

    return g_mst, previous


# Pour get_previous
def dfs(g, node, previous= {}, father = 0, c = 0, p = 0):
    """
    Return the dictionnary of the previous nodes, starting with the node initial node in argument
    As we consider the graph to be related it works.
    We use thus a depth first search.
    """
    previous[node] = (father, c, p)
    for son, power, distance in g.graph[node]:
        if son != father:
            dfs(g, son, previous, father = node, c = c+1, p = power)
    return previous


def get_path(g, previous, source, dest):
    """
    Takes as input a graph, the dictionnary, a dictionnary of previous nodes for a initial node, 
    source and destination for one journey.
    Returns the path and min power to link those two nodes.
    """
    # Les graphes sont connexes, donc pas besoin de vérifier qu'ils appartienent à la même composante
    power = {0}
    condition = previous[dest][1] < previous[source][1]
    if condition:     # on veut toujours partir du point le plus loin du noeud mère.
        source, dest = dest, source

    path1, node1 = [dest], dest
    path2, node2 = [source], source

    while previous[node1][1] > previous[node2][1]: # on met node 1 et node 2 à même hauteur (= distance au noeud initial)
        node1, new_power = previous[node1][0], previous[node1][2]
        path1.insert(0,node1)
        power.add(new_power)
    # Maintenant node1 et node 2 sont à même hauteur ; on les fait bouger simultanément
    while node1 != node2:
        node1, new_power = previous[node1][0], previous[node1][2]
        path1.insert(0,node1)
        power.add(new_power)

        node2, new_power = previous[node2][0], previous[node2][2]
        power.add(new_power)
        if node2 != node1:
            path2 += [node2]

    path = path2 + path1
    min_power = max(power)
    if condition : # On renverse la liste si au départ la source était plus haute que la destination
        path.reverse()

    return path, min_power


def new_min_power(g, previous, source, dest):
    """
    Takes as input a graph, the dictionnary, a dictionnary of previous nodes for a initial node, 
    source and destination for one journey.
    This function is actually quite unnecessary because everything is done in get_path.
    We made it to follow the statement of work. 
    """
    return get_path(g, previous, source, dest)[1]
    





