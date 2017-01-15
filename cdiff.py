import numpy as np

def gradient(y, x=None):
    """
    Weighted central difference rule. Works on data with irregular spacing.
    
    Parameters:
    y   : (numpy array) data
    x   : (numpy array) x-values
    """
    if x is None:
        x = np.arange(len(y))
    
    x = x.astype(float)
    y = y.astype(float)
    
    #dx = np.diff(x)
    #fwd = np.diff(y)
    
    #d = np.zeros_like(y)
    #d[:-1] += fwd / dx
    #d[1:] += fwd / dx
    
    #d[1:-1] /= dx[:-1] + dx[1:]
    #d[0] /= x[1] - x[0]
    #d[-1] /= x[-1] - x[-2]
    
    dx = np.diff(x)
    fwd = np.diff(y) / dx
    
    d = np.zeros_like(y)
    d[1:-1] += fwd[1:] * dx[:-1]
    d[1:-1] += fwd[:-1] * dx[1:]
    d[0] += fwd[0]
    d[-1] += fwd[-1]
    
    d[1:-1] /= dx[:-1] + dx[1:]
    #d[0] /= x[1] - x[0]
    #d[-1] /= x[-1] - x[-2]
    
    
    return d