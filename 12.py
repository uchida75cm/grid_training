stage_info = list(input().split())
H, W, Y, X = map(int, stage_info[:4])
D = stage_info[4]
M = stage_info[5]
stage = [list(input()) for row in range(H)]

command = {'NL': [0, -1, 'W'], 'NR': [0, 1, 'E'],
           'EL': [-1, 0, 'N'], 'ER': [1, 0, 'S'],
           'SL': [0, 1, 'E'], 'SR': [0, -1, 'W'],
           'WL': [1, 0, 'S'], 'WR': [-1, 0, 'N']}

def test_direction(stage, y, x, d):
    if   d == 'N':
        return y != 0 and stage[y-1][x] != '#'
    elif d == 'E':
        return x != W-1 and stage[y][x+1] != '#'
    elif d == 'S':
        return y != H-1 and stage[y+1][x] != '#'
    elif d == 'W':
        return x != 0 and stage[y][x-1] != '#'

if (test_direction(stage, Y, X, command[D+M][2])):
    print('Yes')
else:
    print('No')
