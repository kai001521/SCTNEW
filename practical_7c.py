# Practical 7C: Fuzzy Membership Functions (Fuzzification)
# Source: SCT_Practicals_1_to_8.pdf

def fuzzify(x, a, b, c):
    if x <= a or x >= c: return 0.0
    if x == b: return 1.0
    return (x - a) / (b - a) if x < b else (c - x) / (c - b)

for temp in [5, 18, 25, 37, 45]:
    cold = fuzzify(temp, 0, 10, 20)
    comf = fuzzify(temp, 15, 25, 35)
    hot = fuzzify(temp, 30, 40, 50)
    print(f"{temp}°C -> Cold: {cold:.2f}, Comf: {comf:.2f}, Hot: {hot:.2f}")
