A, B, K = map(int, input().split())

divisors = []
for i in range(1, 101):
    if (A % i == 0) and (B % i == 0):            
        divisors.append(i)

# K番目に大き物を出力するので末尾から数える
print(divisors[-K])