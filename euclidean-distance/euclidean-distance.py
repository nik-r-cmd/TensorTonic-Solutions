import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    xa=np.asarray(x, dtype=float)
    ya=np.asarray(y, dtype=float)
    return float(np.linalg.norm(xa-ya))
    pass