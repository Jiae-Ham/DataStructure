from collections import deque

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjList = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'F'],
    'E': ['C', 'G', 'H'],
    'F': ['D'],
    'G': ['E', 'H'],
    'H': ['E', 'G']
}
# 깊이 우선 탐색 (DFS)
def dfs(graph, start, visited=set()):
    visited.add(start)
    print(start, end=' - ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 너비 우선 탐색 (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' - ')

        for nbr in graph[vertex]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)

# 결과 출력
print("DFS:")
dfs(adjList, 'A')
print("\nBFS:")
bfs(adjList, 'A')

def find_connected_components(graph):
    visited = set()
    connected_components = []

    for start in graph:
        if start not in visited:
            queue = deque([start])
            visited.add(start)
            components = [start]

            while queue:
                vertex = queue.popleft()
                for nbr in graph[vertex]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)
                        components.append(nbr)

            connected_components.append(components)
    return connected_components

# 연결 컴포넌트 출력
components = find_connected_components(adjList)
for idx, component in enumerate(components):
    print(f"\nComponent {idx + 1}: {' - '.join(component)}")


def find_spanning_tree(graph, start):
    visited = set()
    tree_edges = []

    def dfs(current):
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                tree_edges.append((current, neighbor))
                dfs(neighbor)

    dfs(start)
    return tree_edges

# 스패닝 트리 엣지 출력
spanning_tree_edges = find_spanning_tree(adjList, 'A')
print("Spanning Tree Edges:")
for edge in spanning_tree_edges:
    print(f"{edge[0]} - {edge[1]}")
