import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    xa=np.asarray(x, dtype=float)
    ya=np.asarray(y, dtype=float)
    ans=np.sqrt(np.sum(np.square(xa-ya)))
    return float(ans)
    pass