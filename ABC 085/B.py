N = int(input())
d = [int(input()) for _ in range(N)]

# 重複を除いたリストの長さを出力
ans = len(list(set(d)))
print(ans)