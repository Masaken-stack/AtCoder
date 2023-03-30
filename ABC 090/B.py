A,B = map(int, input().split())

count = 0
# A以上B以下の整数のうち、回文数の個数を求める
for i in range(A, B + 1):
    # iを文字列に変換して、逆順にする
    if str(i) == str(i)[::-1]:
        count += 1

print(count)
