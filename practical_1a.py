# Practical 1A: Simple Linear Neural Network (Ramp Function)
# Source: SCT_Practicals_1_to_8.pdf

x = float(input("x: ")); b = float(input("bias: ")); w = float(input("weight: "))
ynet = w * x + b
# Shortcut for Ramp Function: max(0, min(1, ynet))
output = max(0, min(1, ynet))
print("Net input:", ynet, "| Output:", output)
