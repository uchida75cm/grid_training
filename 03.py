H, W = map(int, input().split())
stage = [list(input()) for i in range(H)]

def detect(stage, address):
    r, c = address[0], address[1]
    if (c == 0):
        res = stage[r][c+1] == '#'
        return res
    elif (c == W-1):
        res = stage[r][c-1] == '#'
        return res
    else:
        res = (stage[r][c+1] == '#' and stage[r][c-1] == '#')
        return res

for row in range(H):
    for col in range(W):
        if (detect(stage, [row, col])):
            print(str(row) + ' ' + str(col))
