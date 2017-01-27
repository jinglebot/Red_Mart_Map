"""
    This program gives a path from the highest value to the lowest.
    There is no comparison with other paths done yet. It still needs more tweaking.
"""
# CREATE A TUPLE
def tuple(x, y):
    return x, y

#print tuple(5, 6)

def get_tuple(tuple_xy):
    x, y = tuple_xy
    return x, y

# CREATE A GRID
def create_graph(G, L, x, y):
    # Create grid graph dictionary with tuples as area coordinates and values as altitude measurements
    # G = {(1,1): 1000, (1,2): 998, ...}
    # x = width of the grid, range(w)
    # y = height of the grid, range(h)

    # Initialize G
    for b in range(y):
        for a in range(x):
            G[tuple(a, b)] = L.pop(0)
            #print a, b, G[tuple(a, b)]

    # Print like a grid
    for b in range(y):
        for a in range(x):
            print G[tuple(a, b)],
        print '\n'

    return G

# READ DATA FILE
def read_file(filename):
    L = []
    tsv = open(filename, 'r+').readlines()

    # The first line in the file gives the dimensions of the map.
    first_line = tsv.pop(0)
    mid = first_line.find(' ', 0)
    x = int(first_line[0:mid])
    y = int(first_line[mid+1:])
    #print first_line, x, y, x*y

    # Save data to a list
    for line in tsv:
        line = line.strip('\n')
        for elem in line:
            if elem != ' ':
                L.append(int(elem))
    #print L

    return L, x, y

# FIND STARTING COORDINATES == HIGHEST VALUE
# This function returns only one maximum value.
# If there are duplicate maximum values, this function gets the last one in the loop.
def find_peak(G):
    maxpt = 0
    for coord in G:
        if G[coord] > maxpt:
            maxpt = G[coord]
            maxcoord = coord
    #print "max coord", maxcoord, maxpt
    return maxcoord

# FIND END COORDINATES == LOWEST VALUE
# This function returns only one minimum value.
# If there are duplicate minimum values, this function gets the last one in the loop.
def find_bottom(G):
    minpt = G[0, 0]
    mincoord = 0, 0
    for coord in G:
        if G[coord] < minpt:
            minpt = G[coord]
            mincoord = coord
    #print "min coord", mincoord, minpt
    return mincoord

# FIND AREA NEIGHBORS
def find_neighbors(G, peak):
    """
    # I wasn't sure if I could include NE, NW, SE, SW
    neighbors = {}
    x, y = get_tuple(peak)
    for p in range(x-1, x+2):
        for q in range(y-1, y+2):
            if tuple(p, q) in G:
                if tuple(p, q) != peak:
                    neighbors[tuple(p, q)] = G[tuple(p, q)]
    """
    neighbors = {}
    x, y = get_tuple(peak)
    N = x, y-1
    S = x, y+1
    E = x+1, y
    W = x-1, y
    directions = [N, E, S, W]
    for d in directions:
        if d in G:
                if d != peak:
                    neighbors[d] = G[d]
    
    return neighbors

# FIND NEXT HIGHEST VALUE, NEXT PATH
# If considering a list of highest values,
# change vars next_peak and next_peak_val to a dict
def find_next_peak(N, G, peak):
    next_peak = None
    next_peak_val = None
    for n in N[peak]:
        if N[peak][n] < G[peak]:
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
    if not next_peak == None:
        path.append(next_peak)
    else:
        return path
    return find_path(N, G, path, bottom, next_peak)

# FIND THE LONGEST PATH
def find_longest_path():
    G = {}
    N = {}
    filename = 'temp.txt'
    L, x, y = read_file(filename)
    create_graph(G, L, x, y)
    #Start from the highest peak
    peak = find_peak(G)
    print "peak", peak, G[peak]
    #End at the lowest part
    bottom = find_bottom(G)
    #Find neighbors
    print "N:"
    for area in G:
        N[area] = find_neighbors(G, area)
        print area, N[area]
    #Find next peaks
    print "Next peaks:"
    for area in G:
        print area, G[area], find_next_peak(N, G, area)
    #Find path
    print "Path:"
    P = {}
    P[peak] = G[peak]
    path = [peak]
    find_path(N, G, path, bottom, peak)
    return path
    """
    #print find_neighbors(G, peak)
    #return G
    
    """

print find_longest_path()

