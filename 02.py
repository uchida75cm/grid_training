H, W, N = map(int, input().split())
S = [list(input()) for _ in range(H)]
for _ in range(N):
  y, x = map(int, input().split())
  S[y][x] = '#'
for line in S:
    print(''.join(line))
