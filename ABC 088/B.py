N = int(input())
a = list(map(int, input().split()))

# リストaを降順にソートする
a.sort(reverse=True)

Alice_score = 0
Bob_score = 0
anser = 0

# AliceとBobが交互に数が最大になるようにカードを取っていく
for count in range(N):
    if count % 2 == 0:
        Alice_score += a[count]
    else:
        Bob_score += a[count]

anser = Alice_score - Bob_score
print(anser)