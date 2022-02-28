H, W = map(int, input().split())
stage = [list(input()) for row in range(H)]

for y in range(H):
    for x in range(W):
        if (stage[y][x] == '#'):
            print(y, x)
