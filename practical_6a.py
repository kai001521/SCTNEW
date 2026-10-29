# Practical 6A: Kohonen Self-Organizing Map
# Source: SCT_Practicals_1_to_8.pdf

import numpy as np
x = np.array([[0,0,1,1], [1,0,0,0], [0,1,1,0], [0,0,1,1]])
w = np.array([[0.2, 0.9], [0.4, 0.7], [0.6, 0.5], [0.8, 0.3]])
alpha = 0.5

for k in range(4):
    # Calculate distance for both output neurons
    D = np.sum((w - x[k].reshape(4, 1))**2, axis=0)
    J = np.argmin(D) # Find winning neuron (shortcut for if D[0] < D[1])
    print(f"Pattern {k+1}: Winner is Neuron {J+1}")
    # Weight Update formula
    w[:, J] = w[:, J] + alpha * (x[k] - w[:, J])
