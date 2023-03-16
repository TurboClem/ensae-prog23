import sys
import time
import random

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
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

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
        self.nodes = list(self.nodes) # Evite l'erreur d'ajout de villes textuelles ("Paris") lorsque self.nodes = range(,)

        if not self.graph:
            output = "The graph is empty"  

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


    def connected_components_first_try(self):
        """
        On crée une liste connected_comp. Elle contient des ensembles définis de la sorte :
            Chaque élément de connected_comp correspond à un noeud.
            Chaque élément contient ce noeud et tous les noeuds qui lui sont reliés par une arrête.

        Ensuite on utilise la fonction récursive reduction_ensembles sur cette liste.
            reduction_ensemble prend en entrée une liste d'ensembles.
            Elle unit les éléments d'intersection non vide de la liste prise en argument.
            Elle renvoie la liste des composantes connectées.
        """ 
        connected_comp = []
        for n in self.nodes:
            l = set()
            for k in self.graph[n]:
                l.add(k[0])
            l.add(n)
            connected_comp.append(l)
            
        return set_reduction(connected_comp)
    
    def connected_components(self):
        con_comp = [{self.nodes[0]}]
        for node in self.nodes:
            indice = -1
            nb_con_comp = len(con_comp)
            for i in range(nb_con_comp):
                if node in con_comp[i]:
                    indice = i
            if indice == -1 :
                con_comp += [{node}]
                indice = nb_con_comp
            print(indice)
            print("avant", con_comp)
            for neighbor, power, distance in self.graph[node]:
                con_comp[indice].add(neighbor)
                print(con_comp)
        return set_reduction(con_comp)


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
    

    def get_path_with_power_first_try(self, source, dest, p):
        # On laisse ce code ici car il répondait à la Q3, avant qu'on ne s'intéresse à la distance.
        # On l'a ensuite adapté pour la Q5, avant de penser à l'algorithme de Dijkstra que nous avons utilisé dans get_path_with_power
        """ 
        On fait un parcours en largeur depuis la source.
        On réalise une liste de tous les chemins possibles depuis la source.
        Initalement, le seul chemin parcouru  est [source]
        A chaque étape, on a k chemins. 
            Pour tous ces k chemins, on prend le bout du chemin.
            On trouve ses voisins qui n'ont pas déjà été visités lors du chemin.
            On remplace le k-ième chemin par les nouveaux qui sont ce même chemin étendu à chacun des voisins.
        Dès le moment où on rencontre la destination, on vérifie que le chemin est franchissable par le camion (puissance), et on le stocke.
        Enfin, on choisit dans ce stock le chemin de distance la plus courte.
        """
        if path_existence(self, source, dest) == None:
            return None
    
        path = [[source]] # On initialilse : le seul chemin parcouru est le noeud source
        path_1 = []
        path_2 = path

        path_bank = []

        while path_1 != path_2 :
            n0, n = 0, 0
            path_1 = [i for i in path]

            for i in range(len(path)):
                n0 += n
                # on étend tous les chemins parcourus à leurs voisins
                new_path = extend_path(self,path[n0])
                n = len(new_path)
                if n > 0:
                    del path[n0]

                for j in range(n):
                    if path == []:
                        path = [new_path[j]]
                    else:
                        path.insert(n0+j,new_path[j])
                for j in path[n0:n0+n+1]:
                    # Si le chemin passe par la destination, on a trouvé un chemin qui convient
                    # On l'ajoute donc à notre banque de chemins
                    gpath = good_path(self, j, p)
                    if j[-1] == dest and gpath[0] and j not in path_bank:
                        path_bank.append((j, gpath[1], gpath[2]))
                        
            path_2 = [i for i in path]
        
        if path_bank == []:
            return(None)
        
        """
        coolpath = path_bank[0]
        for i in path_bank:
            if coolpath[2] > i[2]:
                coolpath = i
        """
        return(path_bank)


    def get_path_with_power(self, source, destination, power):
        """
        On utilise l'algorithme de Dijkstra
        """
        # On vérifie que source et destination sont bien reliables.
        # Si on s'occupe des networks on met ça
        """
        con_comp = path_existence(self, source, destination)
        if con_comp == None:
            return None
        unvisited = list(con_comp)
        """
        # Si on s'occupe des routes on met ça (le grpahe est alors connexe)
        unvisited = self.nodes[:]

        dmax = sys.maxsize # On définit la distance de tous les points à la source comme étant "infinie" (maxsize donc)
        node_distance = dict([(n, dmax) for n in unvisited])
        node_distance[source] = 0
        previous_node = {} #Va stocker pour chaque noeud, le noeud qui le précède dans le chemin le plus court vers la source

        # On parcourt tous les noeuds de la composante connectée
        while unvisited != []:
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
                    previous_node[neighbor[0]] = nearest_node
            unvisited.remove(nearest_node)
        path = [destination]
        i = destination
        while i != source:
            if i not in previous_node.keys():
                return None
            j = previous_node[i]
            path.insert(0, j)
            i = j
        return path
            

    def min_power(self, source, destination):
        """
        Should return path, min_power. 
        """
        """
        # Si aucun chemin n'existe, on renvoie None
        if path_existence(self, source, destination) == None:
            return None

        path = None
        i = -1
        while path == None:
            i+= 1
            path = self.get_path_with_power(source, destination, i)
        return i, path
        """
        """
        paths = self.get_path_with_power_first_try(source, destination, sys.maxsize)
        liste_puissance = [i[1] for i in paths]
        pmin = min(liste_puissance)
        path = paths[liste_puissance.index(pmin)][0]
        return pmin, path

        #liste_routes = turbo_fonction(src, dest)
        #for chemin in liste_routes :
        #    liste_puissance.append(chemin[len(chemin) - 1])
        """
        path = self.get_path_with_power(source, destination, sys.maxsize)
        if path == None:
            return None, None
        pmax = 0
        for i in range(len(path)-1):
            for j in self.graph[path[i]]:
                if j[0] == path[i+1]:
                    if j[1] > pmax:
                        pmax = j[1]
        pmin = 0
        while pmax - pmin > 1:
            path = self.get_path_with_power(source, destination, pmin + (pmax-pmin)//2)
            if path == None:
                pmin = pmin + (pmax-pmin)//2
            else :
                pmax = pmin + (pmax-pmin)//2

        if pmax - pmin == 1 :
            if path == None:
                return pmax, self.get_path_with_power(source, destination, pmax)
        return pmax, path
    

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
        if len(line0) == 2:
            n, m = map(int, line0)
            g = Graph(range(1, n+1))
        else :
            m = int(line0[0])
            g = Graph()

        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g




#Pour connected_components_set :
def duplicated_components(l):
    for i in l:
        for j in l:
            if i.intersection(j) != set() and i != j:
                return True
    return False

def set_reduction(l):
    if duplicated_components(l) == False :
        return l
    else:
        for i in l:
            for j in l:
                if i.intersection(j) != set() and i!=j:
                    c = l
                    if i in c:
                        c.remove(i)
                    c.remove(j)
                    c.append(i.union(j))
                    l = set_reduction(c)
    return l

#Pour get_path_with_power_first_try
def xor(a, b):
    return ((a and not b) or (b and not a))

def path_existence(g, src, dest):
    for c in g.connected_components_set():
        if src in c and dest in c :
            return c
    return None

def extend_path(g, path):
    """
    Renvoie la liste des extensions du chemin.
    Les extensions rallongent d'un noeud non déjà visité.
    Si on arrive à une extrémité, on renvoie une liste contenant le chemin initial.
    """
    neighbor = [g.graph[path[-1]][i][0] for i in range(len(g.graph[path[-1]]))]
    E = set(neighbor)-set(neighbor).intersection(set(path))
    if E == set():
        new_paths = [path]
    else:
        new_paths = [path + [i] for i in E]
    return new_paths

def good_path(g, path, p):
    """
    Renvoie un couple booléen, entier, entier.
    Le booléen reflète la capacité du camion à passer le chemin path.
    Le premier entier est la puissance minimale nécessaire à un camion pour parcourir le chemin
    Le second entier est la distance du chemin.
    """
    condition = True
    pmax = 0
    distance = 0
    for i in range(len(path)-1):
        for j in g.graph[path[i]]:
            if j[0] == path[i+1]:
                if j[1] > p:
                    condition = False
                elif j[1] > pmax:
                    pmax = j[1]
                distance += j[2]
    return condition, pmax, distance


# Commandes pour graphviz :
"""
def graphviz(g):
    from graphviz import Digraph
    g = Digraph(g)
    print(g.source)
    return 
"""

# Estimation du temps moyen de calcul :
def time_estimator(nb_essais, numero, arbre = True):
    """
    Mesure pour le fichier routes.numero.in le temps de calcul moyen d'un trajet
    """
    data_path = "/home/onyxia/work/ensae-prog23/input/"
    g = graph_from_file(data_path + f"network.{numero}.in")
    if arbre :
        g = kruskal(g)
    total = 0
    with open(data_path + f"routes.{numero}.in", "r", encoding = "utf-8") as file:
        nb_trajets = int(file.readline().split()[0])
        for _ in range(min(nb_essais, nb_trajets)):
            trajet = file.readline().split()
            node1 = int(trajet[0])
            node2 = int(trajet[1])
            if arbre :
                t0 = time.perf_counter()
                new_min_power(g, node1, node2)
                t1 = time.perf_counter()
            else :
                t0 = time.perf_counter()
                g.min_power(node1, node2)
                t1 = time.perf_counter()

            total += t1 - t0
    mean_time = total/min(nb_trajets, nb_essais)
    return (mean_time * nb_trajets)
    """
    Pour route 5, on trouve un temps de calcul moyen par trajet de 10min 40sec, soit plus d'1,5 millions d'heures
    pour l'ensemble des trajets. C'est bien trop.
    """

# Pour kruskal
def initial_node(previous_node,node):
    """
    Trouve le noeud initial d'un noeud (c'est à dire le noeud à partir duquel a été créé la composante connexe)
    Il permettra d'indicer cette composante.
    """
    if previous_node[node] != node:
        previous_node[node] = initial_node(previous_node,previous_node[node])
    return previous_node[node]
    
def union(previous_node,rank,node1,node2):
    """
    Unit node 1 à node 2 en les faisant devenir clef/valeur l'un de l'autre dans previous_node.
    Actualise également le rang.
    """
    i1 = initial_node(previous_node,node1)
    i2 = initial_node(previous_node,node2)
    if i1 == i2: 
        return None
    if rank[i2] < rank[i1]:
        previous_node[i2] = i1
    else:
        previous_node[i1]=i2
        if rank[i1] == rank[i2]:
            rank[i2] += 1
    return None

def kruskal(g):
    print('y')
    g_mst = Graph()
    edges = []
    previous_node = {}  # Noeud précédent. Permettra de remonter au noeud initial de chaque composante connexe avec initial_node
                        # Le noeud initial permet d'indicer la composante connexe.
    rank = {}           # Le rang nous permettra de lier des gros arbres avec des petits
    print('z')
    for node in g.nodes:
        previous_node[node] = node
        rank[node] = 0
    # Chaque noeud a comme noeud initial lui même, et comme rang 0
    print('a')
    for node in g.graph:
        for edge in g.graph[node]:
            edges.append((node,edge[0],edge[1]))
    edges.sort(key = lambda x : x[2]) # Permet de trier la liste par rapport à la troisième valeur des sous liste de la liste edge
    print('b')
    for edge in edges:
        if initial_node(previous_node,edge[0]) != initial_node(previous_node,edge[1]):
        # Si les bouts d'une arrête nne sont pas déjà dans la même composante connexe, alors on les unit.
            g_mst.add_edge(edge[0],edge[1],edge[2])
            union(previous_node,rank,edge[0],edge[1])
    print('c')
    return g_mst

# Pour new_min_power
def power(self,node1,node2):
    neighbors = self.graph[node1]
    n = len(neighbors)
    k = 0
    while neighbors[k][0] != node2 and k < n:
        k += 1
    if k == n:
        return None
    return neighbors[k][1]


def get_path(g, source, dest):
    # On s'autorise ici à renvoyer le chemin et la puissance minimale du chemin, ce qu'on ne pouvait pas faire
    # avant avec les tests imposés pour get_path_with_power
    #con_comp = path_existence(g, source, dest)
    #if con_comp == None:
    #    return None

    visited = set()
    previous_nodes = {}
    following = [source]

    while following != []:
        node = following[0]
        del following[0] 
        if node in visited:
            continue                # Passe directement à la prochaine étape du while
        visited.add(node)
        for node2, p, d in g.graph[node]:
            if node2 in visited:
                continue
            else:
                following.append(node2)
                previous_nodes[node2] = node
    path = [dest]
    node = dest
    p_min = 0
    while node != source:
        p_min = max(p_min,power(g, node, previous_nodes[node]))
        node = previous_nodes[node]
        path.insert(0, node)
    return path, p_min


def new_min_power(g, source, dest):
    #con_comp = path_existence(g, source, dest)
    #if con_comp == None:
    #    return None
    g = kruskal(g)
    return get_path(g, source, dest)