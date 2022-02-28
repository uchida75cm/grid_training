stage_info = list(input().split())
H, W, Y, X, mv_cnt = map(int, stage_info)
stage = [list(input()) for row in range(H)]

curr_p = [Y, X]
curr_d = 'N'

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

for _ in range(mv_cnt):
    mv_d = input()
    cmd = command[curr_d+mv_d]
    if (test_direction(stage, curr_p[0], curr_p[1], cmd[2])):
        curr_p = list(map(lambda a, b: a + b, curr_p, cmd[:2]))
        curr_d = cmd[2]
        print('{0} {1}'.format(curr_p[0], curr_p[1]))
    else:
        print('Stop')
        break
