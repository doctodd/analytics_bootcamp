# A starter kit for the graph/matrix exercise
import collections

def adjlist(adj_list):
    """
    Read in adj list and store in form of dict mapping node
    name to list of outgoing edges. Preserve the order you find
    for the nodes.
    """
    adj = collections.OrderedDict() # keep stuff in order read from string
    # adj is an ordered dict, need to extract key and values from data, then assign

    s = adj_list.strip('\n')  # Clean up the data.
    list1 = s.split('\n')  # Convert data from a string to a list of strings.

    # Make a loop over len(list1), for each line, split it into key (string) and value (list).
    for word in list1:
        list2 = word.split(':')
        i = 1
        for word2 in list2:
            if i == 1:  # First item in the line (before the ':') is the key.
                word2 = word2.strip(':')
                key = word2
                i = i + 1
            else:  # Second item in the line (after the ':', is the value (list).
                word2 = word2.strip(' ')
                value = word2.split(', ')
        adj[key] = value  # Add the key/value pair to the OrderedDict.

    return adj

def adjmatrix(adj):
    """
    From an adjacency list, return the adjacency matrix with entries in {0,1}.
    The order of nodes in adj is assumed to be same as they were read in.
    """
    n = len(adj)
    A = [[0] * n for i in range(n)]  # Initialize matrix with all 0's
    keylist = []

    for key in adj:  # Create a list of all the keys so we know the order
        keylist.append(key)

    for key in adj:  # Loop through list and if the keylist value is in the adj list, set A = 1
        for i in keylist:
            if i in adj[key]:
                A[keylist.index(key)][keylist.index(i)] = 1

    return A

def nodes(adj, start_node):
    """
    Walk every node in graph described by adj list starting at start_node
    using a breadth-first search.  Return a list of all nodes found (in
    any order). Include the start_node.
    """
    nodes = []  # list of all the connected nodes
    visited = set()  # set of connected nodes (to eliminate duplicates
    work = set()  # working set of connected nodes that haven't been tested yet

    visited.add(start_node)  # Add start_node to visited set
    for connected_node in adj[start_node]:
        work.add(connected_node)  # Add each connected node to working set

    while len(work) > 0:
        current = work.pop()
        visited.add(current)
        for other_node in adj[current]:
            if other_node not in visited:  # if other_node is already in visited, ignore it
                work.add(other_node)

    nodes = list(visited)  # convert set to list
    return nodes

def gendot(adj):
    """
    Return a string representing the graph in Graphviz DOT format
    with all p->q edges. Parameter adj is an adjacency list.
    """
    dot = "digraph g {\n"
    dot += "  rankdir=LR;\n"

    for key in adj:
        list = adj[key]
        while len(list) > 0:
            dot += "  %s -> %s;\n" % (key, list.pop(0))

    dot += "}\n"
    return dot
