N,A,B = map(int, input().split())

result = 0
for i in range(1, N + 1):
    # 各桁を足し合わせる
    digit_sum = sum(map(int, str(i)))
    if A <= digit_sum <= B:
        result += i

print(result)
