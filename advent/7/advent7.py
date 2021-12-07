from statistics import mode, mean, median
import numpy as np
import math

with open('7.txt') as f:
    lines = f.read()

array = [int(x) for x in lines.split(",")]
l1 = array
mean = round(mean(array))-1
print(mean)
total_fuel = 0
for i in l1:
    fuel = 0
    cost = 0
    while i != mean:
        cost += 1
        if i < mean:
            i += 1
        if i > mean:
            i -= 1
        fuel += cost
    total_fuel += fuel

print(total_fuel)
