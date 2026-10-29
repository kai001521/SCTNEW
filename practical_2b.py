# Practical 2B: XOR using Multilayer Network
# Source: SCT_Practicals_1_to_8.pdf

import numpy as np
w11, w12, w21, w22 = 1, -1, -1, 1 # Standard weights for XOR
v1, v2, theta = 1, 1, 1

x1 = np.array([0, 0, 1, 1])
x2 = np.array([0, 1, 0, 1])

# Hidden Layer
z1 = (x1*w11 + x2*w21 >= theta).astype(int)
z2 = (x1*w12 + x2*w22 >= theta).astype(int)
print("Hidden (z1, z2):", z1, z2)

# Output Layer
y = (z1*v1 + z2*v2 >= theta).astype(int)
print("XOR Output:", y)
