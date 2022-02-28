X, Y, N = map(int, input().split())

current = [Y, X]
direction = 'N'
command = {'NL': [0, -1, 'W'], 'NR': [0, 1, 'E'],
           'EL': [-1, 0, 'N'], 'ER': [1, 0, 'S'],
           'SL': [0, 1, 'E'], 'SR': [0, -1, 'W'],
           'WL': [1, 0, 'S'], 'WR': [-1, 0, 'N']}

def get_next(current, command, D):
    n_command = command[D + input()]
    distance = n_command[:2]
    next_direction = n_command[2]
    next_position = list(map(lambda a, b: a + b, current, distance))
    next_position.append(next_direction)
    return next_position

for _ in range(N):
    result = get_next(current, command, direction)
    print(result[1], result[0])
    current = [result[0], result[1]]
    direction = result[2]
