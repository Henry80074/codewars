with open('5.txt') as f:
    lines = f.readlines()

array = []
for line in lines:
    item = line.strip("\n")
    if item:
        array.append(item)

pairs = [item.strip().split("->") for item in array]

coord_pairs = [[[int(x) for x in item.split(",")] for item in pair] for pair in pairs]

print(coord_pairs)
h_v_lines = []
for pair in coord_pairs:
    for i in pair[0]:
        if i in pair[1]:
            h_v_lines.append(pair)

route = {}

for item in h_v_lines:
    x1, x2 = item[0][0], item[1][0]
    y1, y2 = item[0][1], item[1][1]
    sort_x = sorted([x1, x2])
    sort_y = sorted([y1, y2])
    coord_x = [i for i in range(sort_x[0], sort_x[1]+1)]
    coord_y = [i for i in range(sort_y[0], sort_y[1]+1)]
    for x in coord_x:
        for y in coord_y:
            pair = (x,y)
            try:
                route[pair] += 1
            except:
                route[pair] = -1


coord_list = [cood for cood, occurrences in route.items() if occurrences >= 2]
print(len(coord_list))