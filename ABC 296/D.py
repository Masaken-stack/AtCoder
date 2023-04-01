from math import sqrt
N, M = map(int, input().split())
if N*N < M:
    print(-1)
    exit()
ans = N*N
for a in range((M+N-1) // N, int(sqrt(M)) + 2):
    ans = min(ans, (M+a-1) // a * a)
    if ans == M:
        break
print(ans)