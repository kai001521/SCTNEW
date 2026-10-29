# Practical 5: Hopfield Network
# Source: SCT_Practicals_1_to_8.pdf

import numpy as np
x = np.array([[1, 1, 1, -1]])
w = np.dot(x.T, x)
np.fill_diagonal(w, 0) # Removes self-connections instantly
print("Weight Matrix:\n", w)

y = np.array([1, 1, 1, -1]) # Input pattern to test
# Update one neuron at a time (asynchronous)
for j in range(4):
    yin = x[0][j] + np.dot(w[:, j], y)
    y[j] = 1 if yin > 0 else (-1 if yin < 0 else y[j])
print("Final Pattern:", y)
