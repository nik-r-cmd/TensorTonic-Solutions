import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    aa=np.asarray(a, dtype=float)
    ba=np.asarray(b, dtype=float)
    dot=np.dot(aa, ba)
    x=np.linalg.norm(aa)*np.linalg.norm(ba)
    if x==0:
        return 0.0
    return float(dot/x)
    pass