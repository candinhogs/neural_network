import numpy as np

def softmax(z: np.array):
    prob = sum([np.exp(z[i-1]) for i in range(len(z))])
    return [np.exp(a)/prob for a in z]
