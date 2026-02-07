# qf_population_update.py

import numpy as np
from qf_entangle_beam import qf_entangle_beam

def qf_population_update(fields, adjacency, strength=0.1, constraint=None):
    """
    Population-level update operator for HECM v0.3.0.

    Parameters
    ----------
    fields : list of np.ndarray
        List of coherence fields in the population.
    adjacency : 2D array-like
        Symmetric adjacency matrix defining beam connections.
    strength : float
        Base entanglement strength for all beams.
    constraint : callable or None
        Optional global constraint applied after updates.

    Returns
    -------
    new_fields : list of np.ndarray
        Updated population fields.
    """

    n = len(fields)
    new_fields = fields.copy()

    # Apply pairwise entanglement across the network
    for i in range(n):
        for j in range(i + 1, n):
            if adjacency[i][j] != 0:
                new_i, new_j = qf_entangle_beam(
                    new_fields[i],
                    new_fields[j],
                    strength=adjacency[i][j] * strength
                )
                new_fields[i] = new_i
                new_fields[j] = new_j

    # Apply optional global constraint
    if constraint is not None:
        new_fields = [constraint(f) for f in new_fields]

    return new_fields
