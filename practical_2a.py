# Practical 2A: McCulloch-Pitts (AND/NOT)
# Source: SCT_Practicals_1_to_8.pdf

x1 = [int(x) for x in input("Enter x1 values (space-separated): ").split()]
x2 = [int(x) for x in input("Enter x2 values (space-separated): ").split()]

# Excitatory (w1=1, w2=1)
yin_ex = [a + b for a, b in zip(x1, x2)]
print("Excitatory Yin:", yin_ex)

# Inhibitory (w1=1, w2=-1)
yin_in = [a - b for a, b in zip(x1, x2)]
print("Inhibitory Yin:", yin_in)

# Thresholding (theta = 1)
Y = [1 if y >= 1 else 0 for y in yin_in]
print("Output Y:", Y)
