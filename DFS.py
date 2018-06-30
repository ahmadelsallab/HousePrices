


# DFS
def get_all_neighbors(G, S):
    candidates = G[S][:]

    neighbors = []
    # Find ones
    for i in range(len(candidates)):
        if candidates[i] == 1 and i != S:
            neighbors.append(i)
    return neighbors

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

        if len(St) > 0:
            next_node = St.pop()
            traverseDFSRecursive(next_node, G)
        else:
            return
    else:
        return

def traverseDFS(G):
    S = 0
    traverseDFSRecursive(S, G)


G = [[1,1,1,0,0],[1,1,0,1,0],[1,0,1,0,0],[0,1,0,1,0],[0,0,0,0,1]]
print(traverseDFS(G))
#getConnectedComponentDFS(G)
