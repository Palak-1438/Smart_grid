# smart_grid_flow.py
from collections import deque
import grid_data
from visualization import visualize_grid

# -------------------------------
# Build super-source and super-sink
# -------------------------------
graph = dict(grid_data.graph)  # Make a copy

# Add SuperSource connecting to all generators
graph['SuperSource'] = {s: float('inf') for s in grid_data.sources}

# Add SuperSink connecting from all loads
for s in grid_data.sinks:
    graph[s]['SuperSink'] = float('inf')

# -------------------------------
# Maximum Flow (Edmonds-Karp)
# -------------------------------
def bfs(residual, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    while queue:
        u = queue.popleft()
        for v in residual[u]:
            if v not in visited and residual[u][v] > 0:
                parent[v] = u
                visited.add(v)
                if v == sink:
                    return True
                queue.append(v)
    return False

def edmonds_karp(graph, source, sink):
    residual = {u: dict(v) for u, v in graph.items()}
    parent = {}
    max_flow = 0
    
    while bfs(residual, source, sink, parent):
        # Find minimum capacity along path
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual[parent[s]][s])
            s = parent[s]
        
        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            if v not in residual:
                residual[v] = {}
            residual[v][u] = residual[v].get(u, 0) + path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

# -------------------------------
# Run Maximum Flow Analysis
# -------------------------------
max_flow = edmonds_karp(graph, 'SuperSource', 'SuperSink')
print("Maximum Power Flow from Generators to Loads:", max_flow)

# -------------------------------
# Visualize the Grid
# -------------------------------
visualize_grid(graph)
