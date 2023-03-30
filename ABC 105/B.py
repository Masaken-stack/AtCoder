N = int(input())
result = 'No'

# 4と7の組み合わせでNを割り切れるかどうかを判定する
for i in range(N // 4 + 1):
    for j in range(N // 7 + 1):
        if 4 * i + 7 * j == N:
            result = 'Yes'  
            break

print(result)