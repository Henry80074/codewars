with open('8.txt') as f:
    array = []
    for lines in f.readlines():
        array.append(lines)

clean_lines = []
for item in array:
    line = item.rstrip().split("|")
    clean_lines.append(line)
print(clean_lines)
numbers = []

for code in clean_lines:
    code_dict = {}
    output = code[0].split()
    end = code[1].split()
    for item in output:
        num = None
        if len(set(item)) == 2:
            num = 1
            code_dict[1] = set(item)
        elif len(set(item)) == 3:
            num = 7
            code_dict[7] = set(item)
        elif len(set(item)) == 4:
            num = 4
            code_dict[4] = set(item)
        elif len(set(item)) == 7:
            num = 8
            code_dict[8] = set(item)
        elif num:
            numbers.append(num)
    for x in output:
        if len(x) == 5 and code_dict[1].issubset(x):
            code_dict[3] = set(x)
            break
    code_dict[9] = code_dict[4].union(code_dict[3])
    for x in output:
        middles = code_dict[3] - code_dict[1]
        if len(x) == 6 and middles.issubset(set(x)) and set(x) != code_dict[9]:
            code_dict[6] = set(x)
            break
    for x in output:
        if len(x) == 6 and set(x) != code_dict[9] and set(x) != code_dict[6]:
            code_dict[0] = set(x)
            break
    code_dict[5] = code_dict[9].intersection(code_dict[6])
    for x in output:
        if len(x) == 5 and set(x) != code_dict[5] and set(x) != code_dict[3]:
            code_dict[2] = set(x)
            break
    num_list = []
    for i in end:
        num = list(code_dict.keys())[list(code_dict.values()).index(set(i))]
        num_list.append(num)
    strings = [str(integer) for integer in num_list]
    a_string = "".join(strings)
    an_integer = int(a_string)
    numbers.append(an_integer)
print(sum(numbers))