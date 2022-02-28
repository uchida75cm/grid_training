H, W = map(int, input().split())
stage = [list(input()) for row in range(H)]

for y in range(H):
    for x in range(W):
        left  = x == 0     or stage[y][x-1] == "#"
        right = x == W - 1 or stage[y][x+1] == "#"
        above = y == 0     or stage[y-1][x] == "#"
        below = y == H - 1 or stage[y+1][x] == "#"
        if (left and right and above and below):
            print(y, x)
