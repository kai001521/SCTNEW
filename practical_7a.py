# Practical 7A: Membership Operators
# Source: SCT_Practicals_1_to_8.pdf

l1, l2 = [2, 3, 4, 5], [6, 6, 8, 6]
print("Overlapping" if any(i in l1 for i in l2) else "Not Overlapping")
