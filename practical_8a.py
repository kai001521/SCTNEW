# Practical 8A: Basic Fuzzy Arithmetic
# Source: SCT_Practicals_1_to_8.pdf

A = [0.0, 0.3, 0.6, 0.3, 0.0]
B = [0.0, 0.0, 0.3, 0.6, 1.0]

union = [max(a, b) for a, b in zip(A, B)]
intersect = [min(a, b) for a, b in zip(A, B)]
complement = [1 - a for a in A]

print("Union:", union)
print("Intersection:", intersect)
print("Complement of A:", complement)
