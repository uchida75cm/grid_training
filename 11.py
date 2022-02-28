stage_info = list(input().split())
H, W, Y, X = map(int, stage_info[:4])
D = stage_info[4]
stage = [list(input()) for row in range(H)]

def test_direction(stage, y, x, d):
    if   d == 'N':
        return y != 0 and stage[y-1][x] != '#'
    elif d == 'E':
        return x != W-1 and stage[y][x+1] != '#'
    elif d == 'S':
        return y != H-1 and stage[y+1][x] != '#'
    elif d == 'W':
        return x != 0 and stage[y][x-1] != '#'

if (test_direction(stage, Y, X, D)):
    print('Yes')
else:
    print('No')
