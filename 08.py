Y, X, D = input().split()

current = [int(Y), int(X)]
command = {'NL': [0, -1], 'NR': [0, 1],
           'EL': [-1, 0], 'ER': [1, 0],
           'SL': [0, 1], 'SR': [0, -1],
           'WL': [1, 0], 'WR': [-1, 0]}

current = list(map(lambda a, b: a + b, current, command[D + input()]))
print(' '.join(map(str, current)))
