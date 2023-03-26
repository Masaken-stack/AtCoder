n = int(input())
a = list(map(int, input().split()))

count = 0
# all関数、リストaの要素が全て2で割り切れる場合Ture
while all(i % 2 == 0 for i in a):
    # リストaに全ての要素を２で割った値を挿入
    a = [i // 2 for i in a]
    count += 1

print(count)
