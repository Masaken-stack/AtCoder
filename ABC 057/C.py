import math
N = int(input())

# f(A,B) = max(len(str(A)), len(str(B)))
def f(a, b):
    return max(len(str(a)), len(str(b)))

# N = A * B = sqrt(N) * sqrt(N) = sqrt(N)^2
# f(A,B)の最小値を求めるため、Aの地域をNの平方根までとする
ans = float('inf')
for a in range(1, int(math.sqrt(N))+1):
    if N % a == 0:
        b = N // a
        ans = min(ans, f(a, b))

print(ans)