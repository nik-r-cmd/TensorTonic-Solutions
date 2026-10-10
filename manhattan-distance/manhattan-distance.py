import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    xa = np.asarray(x, dtype=float)
    ya = np.asarray(y, dtype=float)
    
    return float(np.linalg.norm(xa - ya, ord=1))
    
    pass