# Practical 3B: Delta Rule
# Source: SCT_Practicals_1_to_8.pdf

import numpy as np
x = np.array([1.0, 1.0, 1.0])
w = np.array([0.1, 0.2, 0.3])
target = np.array([1.0, 1.0, 1.0])
alpha = 0.9

while True:
    actual = x * w
    if np.array_equal(target, actual): break
    # Delta Rule formula applied to all weights at once
    w = w + alpha * (target - actual) * x
    print("Weights:", w)
