Y, X, N = map(int, input().split())
current = [Y, X]
command = {'N': [-1, 0], 'E': [0, 1], 'S': [1, 0], 'W': [0, -1]}

for move in range(N):
    current = list(map(lambda a, b: a + b, current, command[input()]))
    print(' '.join(map(str, current)))
