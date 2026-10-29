# Practical 4: Backpropagation
# Source: SCT_Practicals_1_to_8.pdf

import numpy as np
import math

# Initial values
x = np.array([0.1, 0.2]); v1 = np.array([0.6, -0.3]); v2 = np.array([-0.1, 0.4])
w = np.array([-0.2, 0.4, 0.1]); b = np.array([0.3, 0.5]); alpha = 0.25

# 1. Forward Pass
zin = b + x[0]*v1 + x[1]*v2
z = 1 / (1 + np.exp(-zin)) # Sigmoid
yin = w[0] + z[0]*w[1] + z[1]*w[2]
y = 1 / (1 + math.exp(-yin))

# 2. Backward Pass
dk = (1 - y) * y * (1 - y) # Output error
dw = alpha * dk * np.append(1, z) # Output weight change

din = dk * w[1:]
d = din * z * (1 - z) # Hidden error
dv = alpha * d[:, None] * x # Hidden weight change

# 3. Update Weights
w_new = w + dw
v1_new = v1 + dv[0]
v2_new = v2 + dv[1]
print("Output y:", round(y, 4))
print("New w:", w_new, "\nNew v1:", v1_new, "\nNew v2:", v2_new)
