def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

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
print("DFS traversal starting from", start_node, ":")
dfs(graph, start_node)
