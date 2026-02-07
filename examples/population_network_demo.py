# examples/population_network_demo.py

import numpy as np
from qf_population_update import qf_population_update

# Four simple coherence fields
fields = [
    np.array([0.1, 0.3, 0.5, 0.7]),
    np.array([0.7, 0.5, 0.3, 0.1]),
    np.array([0.2, 0.4, 0.6, 0.8]),
    np.array([0.8, 0.6, 0.4, 0.2])
]

# Simple adjacency matrix (undirected)
adjacency = [
    [0, 1, 0.5, 0],
    [1, 0, 0.5, 1],
    [0.5, 0.5, 0, 1],
    [0, 1, 1, 0]
]

# Optional global constraint: normalize each field
def normalize(field):
    return field / np.linalg.norm(field)

print("Initial fields:")
for i, f in enumerate(fields):
    print(f"Field {i}:", f)

# Apply population update
new_fields = qf_population_update(
    fields,
    adjacency,
    strength=0.2,
    constraint=normalize
)

print("\nAfter population update:")
for i, f in enumerate(new_fields):
    print(f"Field {i}:", f)
