
from queue import Queue
# BFS:
#_____
def get_all_neighbors(G, S):
    candidates = G[S][:]

    neighbors = []
    # Find ones
    for i in range(len(candidates)):
        if candidates[i] == 1 and i != S:
            neighbors.append(i)
    return neighbors

Q = Queue()
visited = []
def traverseBFSRecursive(S, G):
    if not S in visited:
        #print S
        visited.append(S)
        neighbors = get_all_neighbors(G, S)


        # Queue all neighbors
        for neighbor in neighbors:
            Q.put(neighbor)
        if not Q.empty():
            next_node = Q.get(block=True)
            traverseBFSRecursive(next_node, G)
        else:
            return
    else:
        if not Q.empty():
            next_node = Q.get(block=True)
            traverseBFSRecursive(next_node, G)
        else:
            return
def traverseBFS(G):
    S = 0
    traverseBFSRecursive(S, G)

def getConnectedComponentBFS(G):
    N = len(G)

    for node in range(N):

        if not node in visited:
            print('Cluster starts at ', node)
            traverseBFSRecursive(node, G)


# DFS
St = []
visited = []
def traverseDFSRecursive(S, G):
    if not S in visited:
        print(S)
        visited.append(S)
        neighbors = get_all_neighbors(G, S)
        for neighbor in neighbors:
            if not neighbor in visited:
                St.append(neighbor)

        if len(St)  > 0:
            next_node = St.pop()
            traverseDFSRecursive(next_node, G)
        else:
            return
    else:
        return

def traverseDFS(G):
    S = 0
    traverseDFSRecursive(S, G)

def getConnectedComponentDFS(G):
    N = len(G)

    for node in range(N):

        if not node in visited:
            print('Cluster starts at ', node)
            traverseDFSRecursive(node, G)

#G = [[1,0,1],[0,1,0],[1,0,1]]
#traverseBFS(G)
#getConnectedComponent(G)

G = [[1,1,1,0,0],[1,1,0,1,0],[1,0,1,0,0],[0,1,0,1,0],[0,0,0,0,1]]
print(traverseDFS(G))
#getConnectedComponentDFS(G)
