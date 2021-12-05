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

diag_lines = [x for x in coord_pairs if x not in h_v_lines]
route = {}

print(diag_lines)
path = []
for d_line in diag_lines:
    dx1, dx2 = d_line[0][0], d_line[1][0]
    dy1, dy2 = d_line[0][1], d_line[1][1]
    negpos1 = 1
    negpos2 = 1
    if dx1 > dx2:
        negpos1 = -1
    if dy1 > dy2:
        negpos2 = -1
    coord_dx = [i for i in range(dx1, dx2 + 1, negpos1)]
    coord_dy = [i for i in range(dy1, dy2 + 1, negpos2)]
    path.append(list(map(list, zip(coord_dx, coord_dy))))

for item in h_v_lines:
    x1, x2 = item[0][0], item[1][0]
    y1, y2 = item[0][1], item[1][1]
    sort_x = sorted([x1, x2])
    sort_y = sorted([y1, y2])
    coord_x = [i for i in range(sort_x[0], sort_x[1]+1)]
    coord_y = [i for i in range(sort_y[0], sort_y[1]+1)]
    for x in coord_x:
        for y in coord_y:
            pair = [x,y]
            try:
                route[str(pair)] += 1
            except:
                route[str(pair)] = -1
for pc in path:
    for coord in pc:
        try:
            route[str(coord)] += 1
        except:
            route[str(coord)] = -1


coord_list = [cood for cood, occurrences in route.items() if occurrences >= 2]
print(len(coord_list))