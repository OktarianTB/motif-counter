import networkx as nx
import numpy as np
import itertools

# Original work here https://gist.github.com/tpoisot/8582648
# modified to take in any motif and updated to Python 3

def get_motif_count_directed(graph, motif):
    """Counts motifs in a directed graph
    :param gr: A ``DiGraph`` object representing G
    :param mo: A ``DiGraph`` object representing the motif
    :returns: A ``int`` with the number of occurences of the motif
    This function is actually rather simple. It will extract all (nb of nodes in motif)-grams from
    the original graph, and look for isomorphisms.
    """
    count = 0
    nodes = graph.nodes()

    # basically list all possibilities of group of nodes with the same number of nodes as the motif
    node_list = [nodes] * motif.number_of_nodes()
    groups = list(itertools.product(*node_list))
    groups = [group for group in groups if len(list(set(group))) == motif.number_of_nodes()]
    groups = map(list, map(np.sort, groups))
    u_groups = []
    [u_groups.append(group) for group in groups if not u_groups.count(group)]

    for group in u_groups:
        sub_graph = graph.subgraph(group)
        if nx.is_isomorphic(sub_graph, motif):
            count += 1

    print(count)
    return count

def get_motif_count_undirected(graph, motif):
    directed_graph = graph.to_directed()
    directed_motif = motif.to_directed()
    return get_motif_count_directed(directed_graph, directed_motif)
    

G = nx.Graph([(0,1), (0,2), (0,3), (1,3), (1,2), (2,3), (1,4), (2,5), (3,4), (3,5), (4,5), (3,6), (4,6), (5,6), (2,7), (5,7), (7,8), (8,9)])

motif_A = nx.Graph([(0,1), (0,2), (1,2), (1,3), (2,3)])
motif_B = nx.Graph([(0,1), (0,2), (1,2), (2,3), (2,4)])
motif_C = nx.Graph([(0,1), (0,2), (0,3), (1,3), (1,2), (2,3)])

get_motif_count_undirected(G, motif_A)
get_motif_count_undirected(G, motif_B)
get_motif_count_undirected(G, motif_C)






