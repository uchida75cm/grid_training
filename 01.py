H, W, N = map(int, input().split())

stage = [0] * H
for i in range(H):
    stage[i] = list(input())

points = [0] * N
for i in range(N):
    points[i] = list(map(int, input().split()))

for point in points:
    print(stage[point[0]][point[1]])
