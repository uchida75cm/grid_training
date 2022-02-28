H, W = map(int, input().split())
stage = [list(input()) for row in range(H)]

for y in range(H):
    for x in range(W):
        if y == 0 or stage[y-1][x] == "#":
            if y == H - 1 or stage[y+1][x] == "#":
                print(y, x)
