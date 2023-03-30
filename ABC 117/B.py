N = int(input())
L = list(map(int, input().split()))

# 一番長い辺が他の N−1 辺の長さの合計よりも真に短い場合に限り、条件を満たす N 角形が描ける。
# N角形が描けるかどうかを判定する
if max(L) < (sum(L) - max(L)):
    print("Yes")
else:
    print("No")
