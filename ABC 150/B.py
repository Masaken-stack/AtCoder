N = int(input())
S = input()

count = 0
ABC = "ABC"
# Sが連続した文字列として含むABCの個数を出力する
for i in range(N - 2):
    if S[i:i + 3] == ABC:
        count += 1

print(count)
