with open('1.txt') as f:
    lines = f.readlines()

array = []
for line in lines:
    array.append(line.strip("\n"))
print(array)
count = 0

for i in range(len(array)+1): 
    if array[i-3:i] and array[i-4:i-1]:
        sum1 = sum([int(x) for x in array[i-3:i]])
        sum2 = sum([int(x) for x in array[i-4:i-1]])
        if sum1 > sum2:
            count += 1
print(count)