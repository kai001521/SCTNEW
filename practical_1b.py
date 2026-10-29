# Practical 1B: Binary and Bipolar Sigmoidal Function
# Source: SCT_Practicals_1_to_8.pdf

import math
inputs = [float(x) for x in input("Enter inputs separated by space: ").split()]
weights = [float(w) for w in input("Enter weights separated by space: ").split()]

# Shortcut for summation: sum(x*w for x,w in zip(inputs, weights))
ynet = sum(x * w for x, w in zip(inputs, weights))
print("Net input:", round(ynet, 3))

# Binary Sigmoid
binary = 1 / (1 + math.exp(-ynet))
print("Binary:", round(binary, 3))

# Bipolar Sigmoid
bipolar = (2 / (1 + math.exp(-ynet))) - 1
print("Bipolar:", round(bipolar, 3))
