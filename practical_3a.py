# Practical 3A: Hebb’s Rule
# Source: SCT_Practicals_1_to_8.pdf

X = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
Y = [1, -1, -1, -1]
w = [0, 0]

for i in range(len(X)):
    # Update weight: w + (x * y)
    w = [w[j] + (X[i][j] * Y[i]) for j in range(len(w))]
    print(f"Iteration {i+1}: {w}")
