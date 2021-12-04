
import copy
draw = [31,88,35,24,46,48,95,42,18,43,71,32,92,62,97,63,50,2,60,58,74,66,15,87,57,34,14,3,54,93,75,22,45,10,56,12,83,30,8,76,1,78,82,39,98,37,19,26,81,64,55,41,16,4,72,5,52,80,84,67,21,86,23,91,0,68,36,13,44,20,69,40,90,96,27,77,38,49,94,47,9,65,28,59,79,6,29,61,53,11,17,73,99,25,89,51,7,33,85,70]

with open(r'C:\Users\3henr\Desktop\codewars\advent\4\4.txt') as f:
    lines = f.readlines()

array = []
for line in lines:
    item = line.strip("\n")
    if item:
        array.append(item)

boards = [array[i:i+5] for i in range(0, len(array), 5)]
sort_boards = []

for board in boards:
    for i in board:
        sort_boards.append((i.split()))
comp = [sort_boards[i:i+5] for i in range(0, len(sort_boards), 5)]
comp_copy = copy.deepcopy(comp)
winners = []

def column(matrix, i):
    return [r[i] for r in matrix]
ans = []
seen = []
winner = None

for num in draw:
    for board in comp:
        for i in range(len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == str(num):
                    board[i][j] = "*"
    for n in range(len(comp)):
        board = comp[n]
        for i in range(len(board)):
            row = board[i]
            col = column(board, i)
            if set(row) == set("*") or set(col) == set("*"):
                winner = copy.deepcopy(comp[n])
                if board not in winners and comp_copy[n] not in seen:
                    seen.append(comp_copy[n])
                    #print(board, "position: ", n, "number:", num)
                    ans.append(copy.deepcopy(board))
print(ans.pop())


