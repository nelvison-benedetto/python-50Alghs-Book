
graph = {
    'Amin' : {'Wasim','Nick','Mike'},
    'Wasim' : {'Imran','Amin'},
    'Imran' : {'Wasim','Faras'},
    'Faras' : {'Imran'},
    'Mike' : {'Amin'},
    'Nick' : {'Amin'}
}

def BFS(graph,start):  ##BFS (Breadth-First Search) ricerca per ampiezza, parte da root, espora prima i nodi del livello vicino, poi si sposta sul livello inferiore.
    visited = set()  #è un insieme
    queue = [start]
    while queue:
        node = queue.pop(0)  #rimuove primo elem FIFO (è O(n), su dataset big meglio collections.deque O(1)) 
        if node not in visited:
            visited.add(node)
            neighbours = graph[node]
            unvisited_neighbours = [neighbour for neighbour in neighbours
                                    if neighbour not in visited]
            queue.extend(unvisited_neighbours)
    return visited

def DFS(graph, start, visited=None): #DFS(Depth-First Search) ricerca in profondita, raggiunge il nodo foglia piu lontano, poi si sposta su ramo successivo
    #INFO about pre-order, in-order,post-order,level-traversal
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        DFS(graph,next,visited)
    return visited


start_node = 'Amin'
print( BFS(graph,start_node) )
print( DFS(graph,start_node) )

