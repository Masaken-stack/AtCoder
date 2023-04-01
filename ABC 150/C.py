import itertools

# N 2<=N<=8
N = int(input())

# P,Qは大きさNの順列である
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

# Nの順列のリストを作成
perms = list(itertools.permutations(range(1,N+1)))

# 辞書順でソート
perms_sorted = sorted(perms)

# 番号を振る
for i, perm in enumerate(perms_sorted):
    if perm == P:
        a = i
    if perm == Q:
        b = i

# 差分の絶対値を出力
print(abs(a-b))