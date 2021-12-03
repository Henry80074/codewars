with open(r'C:\Users\3henr\Desktop\codewars\advent\3\3.txt') as f:
    lines = f.readlines()

array = []
for line in lines:
    array.append(line.strip("\n"))

counter = {0: 0, 1: 0, 2: 0, 3: 0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
for i in array:
    for bit in range(len(i)):
        if int(i[bit]) == 1: 
            counter[bit] += 1
        if int(i[bit]) == 0: 
            counter[bit] -= 1

num1 = ""
for i in counter.values():
    if i < 0:
        num1 += "0"
    if i > 0:
        num1 += "1"

num2 = ""
for i in num1:
    if i == "0":
        num2 += "1"
    if i == "1":
        num2 += "0"

ans1 = int(num1, 2) * int(num2, 2)

num = 0
def findC(array, num):
    new_array = []
    while len(array) > 1:
        zero = 0
        one = 0
        for item in array:
            if item[num] == "0":
                zero += 1
            else:
                one += 1
        if zero <= one:
            for item in array:
                if item[num] == "0":
                    new_array.append(item)
        if zero > one:
            for item in array:
                if item[num] == "1":
                    new_array.append(item)    
        num += 1
        return findC(new_array, num)
    return array

def findO(array, num):
    new_array = []
    while len(array) > 1:
        zero = 0
        one = 0
        for item in array:
            if item[num] == "0":
                zero += 1
            else:
                one += 1
        if zero > one:
            for item in array:
                if item[num] == "0":
                    new_array.append(item)
        if zero <= one:
            for item in array:
                if item[num] == "1":
                    new_array.append(item)    
        num += 1
        return findO(new_array, num)
    return array

val1 = findO(array, num)[0] 
val2 = findC(array, num)[0] 

ans2 =int(val1, 2) * int(val2, 2)
print(ans2)