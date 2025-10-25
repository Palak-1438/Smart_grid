# grid_data.py

# Graph: Nodes = Generators(G), Substations(S), Loads(L)
graph = {
    'G1': {'S1': 15, 'S2': 10},  # Generators
    'G2': {'S1': 5, 'S3': 10},
    'S1': {'L1': 10, 'L2': 10},  # Substations
    'S2': {'L2': 5},
    'S3': {'L3': 10},            # Substations
    'L1': {},                     # Loads
    'L2': {},
    'L3': {}
}

# Define generators (sources) and loads (sinks)
sources = ['G1', 'G2']
sinks = ['L1', 'L2', 'L3']
