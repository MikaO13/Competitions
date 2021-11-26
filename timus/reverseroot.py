from sys import stdin
from math import sqrt
nums = []

for line in stdin:
    for word in line.split():
        nums.append(float(word))

nums.reverse()

for num in nums:
    print("%.4f" % sqrt(num))