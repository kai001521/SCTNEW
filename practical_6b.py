# Practical 6B: Adaptive Resonance Theory (ART)
# Source: SCT_Practicals_1_to_8.pdf

import numpy as np
s = np.array([[1,1,0,0], [1,0,0,0], [0,0,1,1]])
b = np.full((4, 3), 0.2) # Bottom-up
t = np.ones((3, 4))      # Top-down
rho = 0.4

for k in range(len(s)):
    yin = np.dot(s[k], b) # Dot product finds net input
    J = np.argmax(yin)    # Shortcut to find winning cluster
    match = np.sum(t[J] * s[k]) / np.sum(s[k]) # Vigilance check

    if match >= rho:
        b[:, J] = (2 * t[J] * s[k]) / (1 + np.sum(t[J] * s[k]))
        t[J] = t[J] * s[k]
    print(f"Pattern {k+1} assigned to Cluster {J+1}")
