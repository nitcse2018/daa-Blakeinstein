def bfs(adjacencyList, start):
    queue = [start]
    visited = set(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for i in adjacencyList[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

def dfs(adjacencyList, start, visited = set()):
    visited.add(start)
    print(start, end =" ")
    for i in adjacencyList[start]:
        if i not in visited:
            dfs(adjacencyList, i, visited)
            
if __name__=="__main__":
    adjacencyMatrix = [
        [1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0]
    ]

    adjacencyList = {
        'A': ['A', 'C', 'D'],
        'B': ['C'],
        'C': ['A', 'B'],
        'D': ['A', 'D', 'E'],
        'E': ['D'],
    }
    
    bfs(adjacencyList, 'A')
    print('\n\n')
    dfs(adjacencyList, 'A')
    print('\n\n') 
    