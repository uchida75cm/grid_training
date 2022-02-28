Y, X, N = map(int, input().split())
# Y, X, N = 38, 47, 27 # 50 38
# Y, X, N = -28, -4, 59 # -3 -24
# Y, X, N = 72, -13, 38 # -16 73

current = [Y, X]
command = [[-1, 0], [0, 1], [1, 0], [0, -1]]
D = 1

def add(list1, list2):
    return list(map(lambda a, b: a + b, list1, list2))

def products(limit):
    count = 0
    flg = 0
    flgs = []
    while True:
        count += 1
        for _ in range(2):
            flg += count
            if (flg >= limit):
                return flgs
            flgs.append(flg)

products = products(N)

for i in range(1, N+1):
    current = add(current, command[D % 4])
    if (i in products):
        D += 1
    if (i == N):
        print(current[1], current[0])
