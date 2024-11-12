from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Function to create the graph from user input
def create_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        neighbors = input(f"Enter the neighbors of {node} (separated by space): ").split()
        graph[node] = neighbors
    return graph

# Example usage:
graph = create_graph()
start_node = input("Enter the starting node: ")
print("BFS traversal starting from", start_node, ":")
bfs(graph, start_node)
