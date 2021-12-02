with open(r'C:\Users\3henr\Desktop\codewars\advent\2\2.txt') as f:
    lines = f.readlines()

directions = {"depth": 0, "forward": 0, "aim":0}
array = []
for line in lines:
    array.append(line.strip("\n"))
print(array)
new_array = []
for i in array:
    i = i.split(" ")
    new_array.append(i)

for item in new_array:
    if item[0] == "up":
        directions["aim"] -= int(item[1])
    if item[0] == "down":
        directions["aim"] += int(item[1])
    if item[0] == "forward":
        directions["forward"] += int(item[1])
        directions["depth"] += directions["aim"] * int(item[1])

print(directions["depth"] * directions["forward"])