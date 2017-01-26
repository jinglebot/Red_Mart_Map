"""
    This program gives the path of nodes from neighbors with the highest value
    with no comparison done.
    To get the longest path, find all possible paths from peak to bottom.
"""

# open file find highest value/values, find max value
# search to get next node for all 8 directions(NW, N, NE, W, E, SW, S, SE)
# do recursion

import csv

# CREATE A TUPLE
def tuple(x, y):
    return x, y

#print tuple(5, 6)

def get_tuple(tuple_xy):
    x, y = tuple_xy
    return x, y


# CREATE A GRID
def create_graph(G, L, x, y):
    # grid graph dictionary with nodes in tuples as coordinates and a value for altitude
    # G = {(1,1): 1000, (1,2): 998, ...}
    # x = width of the grid, range(w), node1
    # y = height of the grid, range(h), node2

    # initialize G
    for a in x:
        for b in y:
            G[tuple(a, b)] = 0
    t = 0
    for n in G:
            G[n] = L[t]
            t = t + 1
    #print G
    return G

### READ DATA FILE
##def read_file(filename):
##    G = []
##    tsv = csv.reader(open(filename, 'r+'), delimiter = ' ')
##    for line in tsv:
##        G = G + line
##     
##    for elem in G:
##        #if elem == None:
##        print elem
##        #line = line.strip('\n')
##        #G = G + line
##        #for line in G:
##    print G
##
##    return G

#create_graph(G, L, range(3), range(3))

# FIND STARTING POINT == NODE WITH HIGHEST VALUE
def find_peak(G):
    maxpt = 0
    for coord in G:
        if G[coord] > maxpt:
            maxpt = G[coord]
            maxcoord = coord
    #print "max coord", maxcoord, maxpt
    return maxcoord

#print find_peak(G)

# FIND END POINT == NODE WITH LOWEST VALUE
def find_bottom(G):
    minpt = 0
    mincoord = 0, 0
    for coord in G:
        if G[coord] < minpt:
            minpt = G[coord]
            mincoord = coord
    #print "min coord", mincoord, minpt
    return mincoord

#print find_peak(G)

# FIND NEIGHBORS OF A NODE
def find_neighbors(G, peak):
    neighbors = {}
    next_peak = 0
    x, y = get_tuple(peak)
    for p in range(x-1, x+2):
        for q in range(y-1, y+2):
            if tuple(p, q) in G:
                if tuple(p, q) != peak:
                    neighbors[tuple(p, q)] = G[tuple(p, q)]
    return neighbors

#print find_neighbors(G, peak)

# FIND NEXT HIGHEST VALUE, NEXT PATH
# If considering a list of highest values,
# change vars next_peak and next_peak_val to a dict
def find_next_peak(N, G, peak):
    next_peak = 0,0
    next_peak_val = 0
    for n in N[peak]:
        if N[peak][n] <= G[peak]:
            if N[peak][n] > next_peak_val:
                next_peak = n
                next_peak_val = N[peak][n]
    return next_peak, next_peak_val

# FIND A PATH
# start at peak and from neighbors of peak, find next peak
# put in path, recurse
# if next peak == bottom, end by returning complete path
def find_path(N, G, path, bottom, peak):
    if peak == bottom:
        return path
    next_peak, val = find_next_peak(N, G, peak)
    print next_peak, val
    path.append(next_peak)
    return find_path(N, G, path, bottom, next_peak)

# FIND THE LONGEST PATH
def find_longest_path():
    G = {}
    #L = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    N = {}
    filename = 'temp.txt'
    L = read_file(filename)
    return L
    """
    x = range(3)
    y = range(3)
    create_graph(G, L, x, y)
    #Start from the highest peak
    peak = find_peak(G)
    #End at the lowest part
    bottom = find_bottom(G)
    #Find neighbors
    print "N:"
    for node in G:
        N[node] = find_neighbors(G, node)
        print node, N[node]
    #Find next peaks
    print "Next peaks:"
    for node in G:
        print node, G[node], find_next_peak(N, G, node)
    #Find path
    print "Path:"
    path = [peak]
    find_path(N, G, path, bottom, peak)
    return path
    """

print find_longest_path()

