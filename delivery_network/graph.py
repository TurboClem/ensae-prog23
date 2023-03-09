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


    def connected_components(self):
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
    

    def get_path_with_power(self, source, dest, p):
        if path_existence(self, source, dest) == None:
            return None
    
        path = [[source]]
        path_1 = []
        path_2 = path

        while path_1 != path_2 :
            n0, n = 0, 0
            path_1 = path

            for i in range(len(path)):
                n0 += n
                new_path = extend_path(self,path[n0])
                n = len(new_path)

                del path[n0]
                for j in range(n):
                    if path == []:
                        path = [new_path[j]]
                    else:
                        path.insert(n0+j,new_path[j])
                    print(path)

                for j in path[n0:n0+n+1]:
                    if j[-1] == dest and good_path(self, j, p):
                        return(j)
            path_2 = path

        return(None)


    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        raise NotImplementedError


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
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
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
                    c.remove(i)
                    c.remove(j)
                    c.append(i.union(j))
                    l = set_reduction(c)
    return l

#Pour get_path_with_power
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
    condition = True
    for i in range(len(path)-1):
        for j in g.graph[path[i]]:
            if j[0] == path[i+1] and j[1] > p:
                condition = False
    return condition
